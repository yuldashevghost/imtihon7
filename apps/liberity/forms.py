from django import forms

from apps.liberity.models import Category, Item
from apps.users.models import User


class ItemForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Item
        fields = ['name', 'image', 'author', 'avatar', 'body', 'price', 'category']
