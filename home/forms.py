from django import forms
from .models import feedback

class FeedbackForm(forms.ModelForm):
    class = feedback
    field = ['comment']

    widget = {
        'comment':forms.Textarea(attrs = {'row':5,'placeholder':'enter your feedback..'})
    }


    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        field = ['name','email','message']