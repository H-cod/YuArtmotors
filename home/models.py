from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.

choices = (
    ('inner', 'inner'),
    ('engine', 'engine'),
    ('vehicle', 'vehicle')
)


def detail_image_upload(instance, filename):
    return f'01_car/details/{instance.brand}/{filename}'


class CarDetail(TimeStampedModel, models.Model):
    """CarDetail model """

    detail_name = models.CharField(max_length=150)
    detail_type = models.CharField(max_length=20, choices=choices)
    brand = models.ForeignKey('CarBrand', on_delete=models.CASCADE)
    price = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to=detail_image_upload)
    description = models.TextField(null=True, blank=True)
    count = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.brand} {self.detail_name}'

    class Meta:
        verbose_name = 'Детали машыны'
        verbose_name_plural = 'Детали машын'


def car_image_upload(instance, filename):
    return f'/cars/{instance.brand}/{filename}'


class CarBrand(TimeStampedModel, models.Model):
    """CarBrand model for Cars"""

    brand_name = models.CharField(max_length=255)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = "Бренд машины"
        verbose_name_plural = "Бренды машин"


class Cars(TimeStampedModel, models.Model):
    """Car model Implementation"""

    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    year = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    photo = models.ImageField()

    def __str__(self):
        return f'{self.brand} {self.name}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Машыны'


class Service(models.Model):
    """Model For Service dynamic addition"""

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'


class PhotosServices(models.Model):
    """Photo model for services"""

    photo = models.ImageField(null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    is_general = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'фото для Сервиса'
        verbose_name_plural = 'фото для Сервис'
