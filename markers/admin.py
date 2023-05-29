import json

from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.urls import reverse, path
from django.utils.html import format_html

from nighthawk2 import settings
from .models import AcceptedMarker, MarkerProposal, Image
from .serializers import MarkerProposalSerializer

admin.site.site_header = settings.SITE_NAME
admin.site.site_title = settings.SITE_NAME


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    min_num = 2


class MarkerAdmin(admin.ModelAdmin):
    def captured_in_years(self, obj):
        images = Image.objects.filter(marker=obj).order_by('year')
        return ', '.join([str(image.year) for image in images])

    captured_in_years.short_description = "v letech"

    def created_by_username(self, obj):
        if obj.created_by:
            return obj.created_by.username
        else:
            return "není známo"

    created_by_username.short_description = "vytvořeno uživatelem"

    def get_list_filter(self, request):
        if request.user.has_perm('markers.accept_markerproposal'):
            return *self.list_filter, 'created_by'
        return self.list_filter

    list_display = (
        '__str__',
        'captured_in_years',
        'created_by_username'
    )

    inlines = [
        ImageInline,
    ]


class MarkerProposalAdmin(MarkerAdmin):
    def changelist_view(self, request, extra_context=None):
        default = (*MarkerAdmin.list_display, 'ready')
        if request.user.has_perm('markers.accept_markerproposal'):
            self.list_display = default + (
                'accept_button',
            )
        else:
            self.list_display = default
        return super().changelist_view(request, extra_context)

    def get_queryset(self, request):
        queryset = super(MarkerProposalAdmin, self).get_queryset(request)
        if request.user.has_perm('markers.accept_markerproposal'):
            return queryset
        return queryset.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        super(MarkerProposalAdmin, self).save_model(request, obj, form, change)

    def accept_button(self, obj):
        return format_html('<a class="button" href="{}" style="text-decoration: none">Přijmout</a>',
                           reverse('admin:accept', args=[obj.pk]))

    accept_button.short_description = 'možnosti'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<int:proposal_id>/accept/',
                 self.admin_site.admin_view(self.accept_proposal),
                 name='accept'),
            path('<int:proposal_id>/preview/',
                 self.admin_site.admin_view(self.preview),
                 name='preview'),
            path('<int:proposal_id>/preview-raw/',
                 self.admin_site.admin_view(self.preview_raw),
                 name='preview_raw'),
        ]
        return my_urls + urls

    def preview(self, request, proposal_id):
        if request.method != "GET":
            # Method not allowed
            return HttpResponse(status=405)

        proposal = MarkerProposal.objects.get(pk=proposal_id)
        context = {
            **self.admin_site.each_context(request),
            'opts': MarkerProposal._meta,
            'proposal': proposal,
            'proposal_id': proposal.pk,
            'title': f'Náhled bodu {proposal.title}'
        }

        return TemplateResponse(request, 'admin/markers/markerproposal/preview.html', context)

    def preview_raw(self, request, proposal_id):
        if request.method != "GET":
            # Method not allowed
            return HttpResponse(status=405)

        proposal = MarkerProposal.objects.get(pk=proposal_id)
        context = {
            'proposal_json': json.dumps(MarkerProposalSerializer(proposal).data)
        }

        return TemplateResponse(request, 'admin/markers/markerproposal/preview_raw.html', context)

    def accept_proposal(self, request, proposal_id):
        if not request.user.has_perm('markers.accept_markerproposal'):
            raise PermissionDenied

        proposal = MarkerProposal.objects.get(pk=proposal_id)

        if request.method == 'GET':
            context = {
                **self.admin_site.each_context(request),
                'opts': MarkerProposal._meta,
                'proposal': proposal,
                'proposal_id': proposal.pk,
                'title': f'Schválení bodu {proposal.title}'
            }

            return TemplateResponse(request, 'admin/markers/markerproposal/accept.html', context)

        elif request.method == 'POST':
            accepted_marker = AcceptedMarker.objects.create(
                title=proposal.title,
                lat=proposal.lat,
                lng=proposal.lng,
                description=proposal.description,
                created_by=proposal.created_by,
            )

            Image.objects.filter(marker=proposal).update(marker=accepted_marker)
            proposal.delete()

            self.message_user(request, "Bod byl přijat.")
            return HttpResponseRedirect(reverse('admin:markers_acceptedmarker_change', args=[accepted_marker.pk]))

        else:
            # Method not allowed
            return HttpResponse(status=405)

    list_filter = ('ready',)


admin.site.register(AcceptedMarker, MarkerAdmin)
admin.site.register(MarkerProposal, MarkerProposalAdmin)
