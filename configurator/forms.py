from django import forms
from .models import ButtonBody, PresselType
from .button_components_data import (
    BUTTON_BODIES,
    PRESSEL_TYPES,
    CONTACT_ARRANGEMENT,
    LED_VOLTAGE,
    LED_COLOR,
    SURROUND_TYPE,
    SURROUND_COLOR,
    PRESSEL_FINISH,
    PRESSEL_MOULD_COLOR,

)


class StandardButtonForm(forms.Form):
    button_body = forms.ChoiceField(choices=BUTTON_BODIES, label='Button body')
    pressel_type = forms.ChoiceField(choices=PRESSEL_TYPES, label='Pressel type')
    contact_arr = forms.ChoiceField(choices=CONTACT_ARRANGEMENT, label='Contacts')
    led_voltage = forms.ChoiceField(choices=LED_VOLTAGE, label='LED voltage')
    led_color = forms.ChoiceField(choices=LED_COLOR, label='LED color')
    surround_type = forms.ChoiceField(choices=SURROUND_TYPE, label='Surround type')
    surround_color = forms.ChoiceField(choices=SURROUND_COLOR, label='Surround color')
    pressel_finish = forms.ChoiceField(choices=PRESSEL_FINISH, label='Pressel finish')
    mould_color = forms.ChoiceField(choices=PRESSEL_MOULD_COLOR, label='Mould color')

