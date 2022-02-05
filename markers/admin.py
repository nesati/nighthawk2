from django.contrib import admin
from .models import AcceptedMarker, MarkerProposal, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 2


class MarkerAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(AcceptedMarker, MarkerAdmin)
admin.site.register(MarkerProposal, MarkerAdmin)
