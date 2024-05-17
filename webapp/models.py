from django.db import models


class Tag(models.Model):
    summary = models.CharField(verbose_name='Краткое описание', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=400, blank=False, null=False)
    status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.CASCADE)
    type = models.ForeignKey('webapp.Type', related_name='type', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')


class Status(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)

    def __str__(self):
        return f'{self.name}'


class Type(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)

    def __str__(self):
        return f'{self.name}'
