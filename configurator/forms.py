from django import forms
from .models import ButtonBody, PresselType
from .button_components_data import (
    BUTTON_BODIES,
    PRESSEL_TYPES,
    CONTACT_ARRANGEMENT
)


class StandardButtonForm(forms.Form):
    button_body = forms.ChoiceField(choices=BUTTON_BODIES, label='Button body')
    pressel_type = forms.ChoiceField(choices=PRESSEL_TYPES, label='Pressel type')
    contact_arr = forms.ChoiceField(choices=CONTACT_ARRANGEMENT, label='Contacts')

