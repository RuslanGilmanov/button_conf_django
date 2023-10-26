from django import forms
from .models import (
    ButtonBody,
    ContactType,
    ButtonBodyContactType,
    IlluminationColor,
    IlluminationVoltage,
    SurroundType,
    SurroundColor,
    SurroundForm
)


class StandardButtonForm(forms.Form):
    button_body = forms.ModelChoiceField(queryset=ButtonBody.objects.all())
    contact_type = forms.ModelChoiceField(queryset=ContactType.objects.none())
    # pressel_type = forms.ModelChoiceField(choices=PRESSEL_TYPES, label='Pressel type')
    # led_voltage = forms.ModelChoiceField(choices=LED_VOLTAGE, label='LED voltage')
    # led_color = forms.ModelChoiceField(choices=LED_COLOR, label='LED color')
    # surround_type = forms.ModelChoiceField(choices=SURROUND_TYPE, label='Surround type')
    # surround_color = forms.ModelChoiceField(choices=SURROUND_COLOR, label='Surround color')
    # pressel_finish = forms.ModelChoiceField(choices=PRESSEL_FINISH, label='Pressel finish')
    # mould_color = forms.ModelChoiceField(choices=PRESSEL_MOULD_COLOR, label='Mould color')

