from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.urls import reverse, path
from django.utils.html import format_html

from nighthawk2 import settings
from .models import AcceptedMarker, MarkerProposal, Image

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

    list_display = (
        '__str__',
        'captured_in_years'
    )

    inlines = [
        ImageInline,
    ]


class MarkerProposalAdmin(MarkerAdmin):
    def changelist_view(self, request, extra_context=None):
        default = MarkerAdmin.list_display
        if request.user.has_perm('markers.accept_markerproposal'):
            self.list_display = default + (
                'accept_button',
            )
        else:
            self.list_display = default
        return super().changelist_view(request, extra_context)

    def accept_button(self, obj):
        return format_html('<a class="button" href="#" style="text-decoration: none">Přijmout</a>')

    accept_button.short_description = 'možnosti'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<int:proposal_id>/accept/',
                 self.admin_site.admin_view(self.accept_proposal),
                 name='accept'),
        ]
        return my_urls + urls

    def accept_proposal(self, request, proposal_id):
        if not request.user.has_perm('markers.accept_markerproposal'):
            raise PermissionDenied

        proposal = MarkerProposal.objects.get(pk=proposal_id)

        if request.method == 'GET':
            context = {
                'opts': MarkerProposal._meta,
                'proposal_name': proposal,
                'proposal_id': proposal.pk
            }

            return TemplateResponse(request, 'admin/markers/markerproposal/accept.html', context)

        elif request.method == 'POST':
            accepted_marker = AcceptedMarker.objects.create(
                title=proposal.title,
                lat=proposal.lat,
                lng=proposal.lng,
                description=proposal.description
            )

            Image.objects.filter(marker=proposal).update(marker=accepted_marker)
            proposal.delete()

            self.message_user(request, "Bod byl přijat.")
            return HttpResponseRedirect(reverse('admin:markers_acceptedmarker_change', args=[accepted_marker.pk]))

        else:
            # Method not allowed
            return HttpResponse(status=405)


admin.site.register(AcceptedMarker, MarkerAdmin)
admin.site.register(MarkerProposal, MarkerProposalAdmin)
