from django.forms import ModelForm
from .models import Widget
from django import forms

class AddWidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']