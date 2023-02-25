from django.db import models


# Create your models here.
class GuestBook(models.Model):
    choices = [
        ('active', 'Активно'),
        ('blocked', 'Заблокировано')
    ]
    author_name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Имя Автора")
    author_email = models.EmailField(max_length=300, null=False, blank=False, verbose_name="Почта Автора")
    text = models.TextField(max_length=200, null=False, blank=False, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время Создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время Редактирования")
    status = models.CharField(max_length=40, null=False, blank=False, verbose_name='Статус', choices=choices,
                              default='active')

    def __str__(self):
        return f"{self.author_name} - {self.status}"
