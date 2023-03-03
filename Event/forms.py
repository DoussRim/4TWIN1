from django import forms
from .models import Event
from django.forms import Textarea
from datetime import date
class FormEvent(forms.ModelForm):
    class Meta:
        model=Event
        # fields=("__all__")
        # exclude=['state']
        fields=("title","description","category",
                "evt_date","image","organizer")
        widgets={'description':Textarea(
            attrs={'cols':10,'rows':10}
        )}
        help_texts={
            'title':"Your Title here !"
        }
        error_messages={
            'title':{
                'max_length':"This event's title is too long."
            }
        }
    category=forms.ChoiceField(
            label='Category',
            widget=forms.RadioSelect,
            choices=Event.CATEGORY_EVENT
        )
    evt_date=forms.DateField(
        label="Event Date",
        initial=date.today,
        widget=forms.DateInput(
            attrs={'type':'date','class':'form-control date-input'}
        )
    )