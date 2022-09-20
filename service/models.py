from django.db import models


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
