from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.

choices = (
    ('inner', 'inner'),
    ('engine', 'engine'),
    ('vehicle', 'vehicle')
)

hand_drive_choices = (
    ('Left', 'Left'),
    ('Right', 'Right')
)

transmission_choices = (
    ('Automatic', 'Automatic'),
    ('Manual', 'Manual'),
    ('CVT', 'CVT')

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
    return f'cars/{instance.brand}/{filename}'


class CarBrand(TimeStampedModel, models.Model):
    """CarBrand model for Cars"""

    brand_name = models.CharField(max_length=255)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = "Бренд машины"
        verbose_name_plural = "Бренды машин"


def car_image_list_upload(instance, filename):
    return f'cars/list/{filename}'


class CarPhotoList(models.Model):
    """Car photo list, max_count 8"""

    photo = models.ImageField(upload_to=car_image_list_upload)
    car = models.ForeignKey('Cars', on_delete=models.CASCADE,
                            related_name='photo_list', blank=True, null=True)

    def __str__(self):
        return 'фото'

    class Meta:
        verbose_name = 'фото для Автомобилья'
        verbose_name_plural = 'фото для Машыны'


class Cars(TimeStampedModel, models.Model):
    """Car model Implementation"""

    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    mileage = models.IntegerField()
    year = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    hand_drive = models.CharField(max_length=10,
                                  choices=hand_drive_choices, default='Left')
    description = models.TextField()
    engine = models.CharField(max_length=155, default='Gasoline')
    color = models.CharField(max_length=155)
    transmission = models.CharField(max_length=155, choices=transmission_choices,
                                    default='Automatic')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    photo = models.ImageField(upload_to=car_image_upload)

    def __str__(self):
        return f'{self.brand} {self.name}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Машыны'

