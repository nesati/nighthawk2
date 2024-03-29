# Generated by Django 4.0.2 on 2022-02-05 16:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='název')),
                ('lat', models.DecimalField(decimal_places=4, max_digits=6, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='zeměpisná šířka')),
                ('lng', models.DecimalField(decimal_places=4, max_digits=7, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='zeměpisná délka')),
                ('description', models.TextField(verbose_name='popis')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='rok')),
                ('source_name', models.CharField(max_length=100, verbose_name='název zdroje')),
                ('source_url', models.URLField(verbose_name='adresa zdroje')),
                ('media', models.ImageField(upload_to='', verbose_name='obrázek')),
                ('marker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markers.marker')),
            ],
        ),
    ]
