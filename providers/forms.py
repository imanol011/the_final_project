from django import forms
from providers.models import Provider

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'