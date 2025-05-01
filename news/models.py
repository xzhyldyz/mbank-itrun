from django.db import models

class ServiceHomepage(models.Model):
    title = models.CharField(max_length=100)
    little_text = models.TextField(max_length=100)
    img = models.ImageField(upload_to= 'service')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Сервис'
        verbose_name = 'сервис'


class SliderHomepage(models.Model):
    title = models.CharField(max_length=100)
    little_text = models.TextField(max_length=100)
    img = models.ImageField(upload_to= 'sliders')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Слайдер'
        verbose_name = 'слайдер'

class News(models.Model):
    title = models.CharField(
        max_length=50, verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
        )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'новость'
        