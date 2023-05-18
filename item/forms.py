from django import forms

class ProductFilterForm(forms.Form):
    category = forms.CharField(required=False)
