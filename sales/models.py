from django.db import models

class Actions(models.Model):
    name = models.CharField('Заголовок', max_length=150)
    foto = models.ImageField('Фото', upload_to='actions')
    actual = models.BooleanField('Актуальность', default=True)

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.name