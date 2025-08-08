from django import forms
from .models import feedback

class FeedbackForm(forms.ModelForm):
    class = feedback
    field = ['comment']

    widget = {
        'comment':forms.Textarea(attrs = {'row':5,'placeholder':'enter your feedback..'})
    }