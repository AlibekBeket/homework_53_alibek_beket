from django.db import models


# Create your models here.
class ToDo(models.Model):
    choices = [
        ('new', 'Новая'),
        ('in progress', 'В процессе'),
        ('made', 'Сделано')
    ]
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=40, null=False, blank=False, verbose_name='Статус', choices=choices,
                              default='new')
    created_at = models.DateField(verbose_name='Дата выполнения', blank=True, null=True)

    def __str__(self):
        return f"{self.description} - {self.status}"
