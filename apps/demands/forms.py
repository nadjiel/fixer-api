from django import forms

from .models import Demand


class DemandForm(forms.ModelForm):
    class Meta:
        model = Demand
        fields = "__all__"
