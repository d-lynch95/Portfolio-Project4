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
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    # This code prevents double bookings or bookings in the past
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        if date < date.today():
            raise forms.ValidationError(
                    "This date cannot be selected as it has already passed"
                )
        if Post.objects.filter(Q(date=date) & Q(time=time)).exists():
            raise forms.ValidationError(
                "This appointment time is not available. Please select another"
                )
        return cleaned_data


    # Allow users to submit the form and use datepicker
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.fields['date'].widget.attrs['class'] = 'datepicker'
        self.fields['date'].widget.attrs['autocomplete'] = 'off'


# class EditApptForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('name', 'phone', 'email', 'date', 'time',)
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'})
#         }