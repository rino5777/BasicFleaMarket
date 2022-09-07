from .models import Ads
from django import forms
from django.forms import inlineformset_factory


class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = '__all__'
        widgets = {'author': forms.HiddenInput}



#AIFormSet = inlineformset_factory(Ads,  fields='__all__')
