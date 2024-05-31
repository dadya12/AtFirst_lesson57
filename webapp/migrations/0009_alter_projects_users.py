# Generated by Django 5.0.4 on 2024-05-31 08:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_projects_users'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи'),
        ),
    ]