from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'file_attachment']
        widgets = {
            'details': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Describe your issue...'}),
        }
