from django import forms
from django.forms import widgets

from webapp.models import Tag, Projects


class TagForms(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['summary', 'description', 'status', 'type']
        widgets = {
            'type': forms.CheckboxSelectMultiple,
            'status': forms.CheckboxSelectMultiple}
        error_messages = {
            'summary': {
                'required': 'Please enter',
                'min_length': 'So short'
            }
        }

    def clean(self):
        cleaned_data = super().clean()
        summary = cleaned_data.get('summary')
        description = cleaned_data.get('description')
        if summary == description:
            raise forms.ValidationError('Summary and Description same')
        return cleaned_data


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['name', 'description']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=150, required=False, label='Search')
