# Generated by Django 4.1.7 on 2023-02-25 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200, verbose_name='Имя Автора')),
                ('author_email', models.EmailField(max_length=300, verbose_name='Почта Автора')),
                ('text', models.TextField(max_length=200, verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время Создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время Редактирования')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=40, verbose_name='Статус')),
            ],
        ),
    ]