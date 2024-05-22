# Generated by Django 5.0.4 on 2024-05-22 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_tag_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tags', to='webapp.projects', verbose_name='Проект'),
        ),
    ]