# Generated by Django 4.0.3 on 2022-09-20 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_carphotolist_options_cars_color_cars_engine_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='photo_list',
        ),
        migrations.AddField(
            model_name='carphotolist',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo_list', to='home.cars'),
        ),
    ]
