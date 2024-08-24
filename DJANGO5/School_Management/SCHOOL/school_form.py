from django import forms
from .models import School
class school_form(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'