from django import forms
from .models import (
    ButtonBody,
    ContactType,
    IlluminationColor,
    IlluminationVoltage,
    SurroundType,
    SurroundColor,
    SurroundForm
)


class StandardButtonForm(forms.Form):
    button_body = forms.ModelChoiceField(
        queryset=ButtonBody.objects.all(),
        widget=forms.Select(attrs={"hx-get": "load_contact_types/", "hx-target": "#id_contact_type"}))
    contact_type = forms.ModelChoiceField(queryset=ContactType.objects.none())
    # pressel_type = forms.ModelChoiceField(choices=PRESSEL_TYPES, label='Pressel type')
    # led_voltage = forms.ModelChoiceField(choices=LED_VOLTAGE, label='LED voltage')
    # led_color = forms.ModelChoiceField(choices=LED_COLOR, label='LED color')
    # surround_type = forms.ModelChoiceField(choices=SURROUND_TYPE, label='Surround type')
    # surround_color = forms.ModelChoiceField(choices=SURROUND_COLOR, label='Surround color')
    # pressel_finish = forms.ModelChoiceField(choices=PRESSEL_FINISH, label='Pressel finish')
    # mould_color = forms.ModelChoiceField(choices=PRESSEL_MOULD_COLOR, label='Mould color')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "button_body" in self.data:
            body_id = int(self.data.get("button_body"))
            button_body = ButtonBody.objects.get(id=body_id)
            self.fields["contact_type"].queryset = button_body.contact_types.all()

