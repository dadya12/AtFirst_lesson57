from django import forms
from django.forms import widgets

from webapp.models import Type, Status


class TagForms(forms.Form):
    summary = forms.CharField(label='Краткое описание', max_length=100, required=True)
    description = forms.CharField(label='Описание', max_length=400, required=False, widget=widgets.Textarea())
    status = forms.ModelMultipleChoiceField(queryset=Status.objects.all(), label='Статус', required=True)
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Тип', required=True)
