from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
from .models import Category, Husband, Women


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 empty_label='Категория не выбрана', label='Категории')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(),
                                     required=False, empty_label='Не замужем', label='Муж')

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'husband', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'rows': '5', 'cols': '50'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина не должна превышать 50 символов')

        return title


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')


