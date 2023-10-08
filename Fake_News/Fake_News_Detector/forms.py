from django import forms
from django.core import validators

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Paste your article here...', 'required': True}),
        }
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    
