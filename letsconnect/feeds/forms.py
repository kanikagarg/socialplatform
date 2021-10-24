from django import forms
from django.core.exceptions import ValidationError
from .models import Feed

class FeedForm(forms.ModelForm):
    class Meta():
        model = Feed
        fields = ['status']
        labels = {
            'status':"Write your Post Here..."
        }
        widgets= {
            "status":forms.Textarea(attrs={"class":"form-control mb-5"})
        }
        
    # cannot post an empty status
    def clean_status(self):
        status = self.cleaned_data["status"]
        if len(status)<1:
            raise ValidationError
        return status