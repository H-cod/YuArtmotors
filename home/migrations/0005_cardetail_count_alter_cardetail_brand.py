# Generated by Django 4.0.3 on 2022-03-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_cardetail_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetail',
            name='count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cardetail',
            name='brand',
            field=models.CharField(choices=[('Mercedes', 'Mercedes'), ('BMV', 'BMV'), ('Chevrolet', 'Chevrolet'), ('Volkswagen', 'Volkswagen'), ('Opel', 'Opel'), ('Mitsubishi', 'Mitsubishi'), ('Audi', 'Audi'), ('Nissan', 'Nissan')], max_length=60),
        ),
    ]
