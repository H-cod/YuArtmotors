# Generated by Django 4.0.3 on 2022-03-17 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_cardetail_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Mercedes', 'Mercedes'), ('BMV', 'BMV'), ('Chevrolet', 'Chevrolet'), ('Volkswagen', 'Volkswagen'), ('Opel', 'Opel'), ('Mitsubishi', 'Mitsubishi'), ('Audi', 'Audi'), ('Nissan', 'Nissan'), ('Infinity', 'Infinity'), ('Kia', 'Kia'), ('Hyundai', 'Hyundai'), ('Suzuki', 'Suzuki'), ('Lexus', 'Lexus'), ('Subaru', 'Subaru'), ('Mazda', 'Mazda'), ('Toyota', 'Toyota')], max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('year', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='cardetail',
            name='brand',
            field=models.CharField(choices=[('Mercedes', 'Mercedes'), ('BMV', 'BMV'), ('Chevrolet', 'Chevrolet'), ('Volkswagen', 'Volkswagen'), ('Opel', 'Opel'), ('Mitsubishi', 'Mitsubishi'), ('Audi', 'Audi'), ('Nissan', 'Nissan'), ('Infinity', 'Infinity'), ('Kia', 'Kia'), ('Hyundai', 'Hyundai'), ('Suzuki', 'Suzuki'), ('Lexus', 'Lexus'), ('Subaru', 'Subaru'), ('Mazda', 'Mazda'), ('Toyota', 'Toyota')], max_length=60),
        ),
    ]
