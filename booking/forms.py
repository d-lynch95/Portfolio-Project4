from django import forms
from .models import Post
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.widgets import HiddenInput

class ApptForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'phone', 'email', 'date', 'time', 'slug',  )
        widgets = {
            'slug': HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        if Post.objects.filter(date=date).exists() and Post.objects.filter(time=time).exists():
            raise forms.ValidationError("This appointment time is not available. Please select another")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.fields['date'].widget.attrs['class'] = 'datepicker'
        self.fields['date'].widget.attrs['autocomplete'] = 'off'