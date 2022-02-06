from django.contrib import admin
from django.core.exceptions import PermissionDenied
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

    def accept_proposal(self, request, proposal_id):
        if not request.user.has_perm('markers.accept_markerproposal'):
            raise PermissionDenied

        proposal = MarkerProposal.objects.get(pk=proposal_id)



admin.site.register(AcceptedMarker, MarkerAdmin)
admin.site.register(MarkerProposal, MarkerProposalAdmin)
