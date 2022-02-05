from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Marker(models.Model):
    """
    Base class for a marker, includes data shared between
     :model:`markers.MarkerProposal` and
     :model:`markers.AcceptedMarker`.
    """

    title = models.CharField(verbose_name="název", max_length=100)

    lat = models.DecimalField(
        verbose_name="zeměpisná šířka",
        max_digits=6,
        decimal_places=4,  # See https://xkcd.com/2170/ for precision rationale
        validators=[
            MaxValueValidator(90),
            MinValueValidator(-90)
        ]
    )

    lng = models.DecimalField(
        verbose_name="zeměpisná délka",
        max_digits=7,
        decimal_places=4,  # See https://xkcd.com/2170/ for precision rationale
        validators=[
            MaxValueValidator(180),
            MinValueValidator(-180)
        ]
    )

    description = models.TextField(verbose_name="popis")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'bod'
        verbose_name_plural = 'body'


class Image(models.Model):
    """
    Photo of a place
    """

    year = models.IntegerField(verbose_name="rok")
    source_name = models.CharField(verbose_name="název zdroje", max_length=100)
    source_url = models.URLField(verbose_name="adresa zdroje")
    media = models.ImageField(verbose_name="obrázek")
    marker = models.ForeignKey(Marker, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marker.title} {self.year}"

    class Meta:
        verbose_name = 'obrázek'
        verbose_name_plural = 'obrázky'


class MarkerProposal(Marker):
    """
    Class for marker proposals created by students
    """

    class Meta:
        verbose_name = 'návrh bodu'
        verbose_name_plural = 'návrhy bodů'
        permissions = [
            ("accept_markerproposal", "Může přijmout návrh bodu")
        ]


class AcceptedMarker(Marker):
    """
    Class for markers accepted by admins
    """

    class Meta:
        verbose_name = 'přijatý bod'
        verbose_name_plural = 'přijaté body'
