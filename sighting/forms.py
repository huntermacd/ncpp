from django import forms
from .models import Sighting

class SightingForm(forms.ModelForm):
	class Meta:
		model = Sighting