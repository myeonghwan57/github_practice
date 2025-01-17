from dataclasses import field
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # editable field만 가능.
        fields = ["title", "content"]
