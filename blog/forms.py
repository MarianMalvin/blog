from django import forms
from django.core.exceptions import ValidationError

from .models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_title = self.cleaned_data['title']
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug can not be "create"')
        if Tag.objects.filter(slug=new_slug).count():
            raise ValidationError(f'Title field must be unique. Tag "{new_title}" already exist.')
        return new_slug
