# Generated by Django 4.0.3 on 2022-09-13 20:19

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_service_alter_carbrand_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarPhotoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=home.models.car_image_list_upload)),
            ],
        ),
        migrations.AlterField(
            model_name='cars',
            name='photo',
            field=models.ImageField(upload_to=home.models.car_image_upload),
        ),
        migrations.DeleteModel(
            name='PhotosServices',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.AddField(
            model_name='cars',
            name='photo_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.carphotolist'),
        ),
    ]