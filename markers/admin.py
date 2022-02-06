from django.contrib import admin

from nighthawk2 import settings
from .models import AcceptedMarker, MarkerProposal, Image

admin.site.site_header = settings.SITE_NAME
admin.site.site_title = settings.SITE_NAME


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    min_num = 2


class MarkerAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(AcceptedMarker, MarkerAdmin)
admin.site.register(MarkerProposal, MarkerAdmin)
