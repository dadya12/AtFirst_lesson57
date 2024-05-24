from django.db import models


class Tag(models.Model):
    summary = models.CharField(verbose_name='Краткое описание', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=400, blank=False, null=False)
    status = models.ManyToManyField('webapp.Status', related_name='tags', blank=True, verbose_name='Статус')
    type = models.ManyToManyField('webapp.Type', related_name='tags', blank=True, verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    project = models.ForeignKey('webapp.Projects', on_delete=models.CASCADE, related_name='tags', verbose_name='Проект')

    def __str__(self):
        return f'{self.summary}'


class Projects(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=400, verbose_name='Описание')
    created_at = models.DateField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return f'{self.name}'


class Status(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)

    def __str__(self):
        return f'{self.name}'


class Type(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)

    def __str__(self):
        return f'{self.name}'
