# Generated by Django 4.0.10 on 2023-05-28 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0006_marker_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='markerproposal',
            name='ready',
            field=models.BooleanField(default=False, verbose_name='připraveno ke schválení'),
            preserve_default=False,
        ),
    ]
