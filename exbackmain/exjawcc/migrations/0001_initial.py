# Generated by Django 4.0.1 on 2022-01-27 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Площадка')),
                ('icon', models.ImageField(upload_to='platform/', verbose_name='Иконка площадки')),
                ('platform_type', models.CharField(choices=[('SER', 'Сервис'), ('SOC', 'Соц. сеть')], default='SER', max_length=3)),
            ],
            options={
                'verbose_name': 'Площадка',
                'verbose_name_plural': 'Площадки',
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('version', models.CharField(blank=True, max_length=200, null=True, verbose_name='Версия')),
                ('name', models.CharField(max_length=200, verbose_name='Исполнитель')),
                ('cover', models.ImageField(upload_to='covers/', verbose_name='Обложка')),
                ('slug', models.SlugField(max_length=32, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=160)),
                ('vision', models.BooleanField(default=True, verbose_name='Видимость')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exjawcc.platform')),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exjawcc.release')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
            },
        ),
    ]
