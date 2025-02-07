from .models import product
from django import forms

class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ["name","desc","price","quantity"]