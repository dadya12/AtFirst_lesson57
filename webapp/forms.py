from django import forms
from django.forms import widgets

from webapp.models import Type, Status


class TagForms(forms.Form):
    summary = forms.CharField(label='Краткое описание', max_length=100, required=True)
    description = forms.CharField(label='Описание', max_length=400, required=False, widget=widgets.Textarea())
    status = forms.ModelMultipleChoiceField(queryset=Status.objects.all(), label='Статус', required=True)
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Тип', required=True)

    def clean_summary(self):
        summary = self.cleaned_data['summary']
        if len(summary) < 5:
            raise forms.ValidationError('Слишком короткий')
        return summary

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 30:
            raise forms.ValidationError('Слишком кароткий')
        return description
