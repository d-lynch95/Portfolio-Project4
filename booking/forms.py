from django import forms
from .models import Post
from datetime import datetime
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.widgets import HiddenInput

# Create from to accept users appointments
class ApptForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'phone', 'email', 'date', 'time', 'slug',)
        widgets = {
            'slug': HiddenInput(),
        }


    # Allow users to submit the form and use datepicker
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.fields['date'].widget.attrs['class'] = 'datepicker'
        self.fields['date'].widget.attrs['autocomplete'] = 'off'
