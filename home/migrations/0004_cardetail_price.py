# Generated by Django 4.0.3 on 2022-03-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_cardetail_description_cardetail_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetail',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
