from django import forms
from .conf_specific_data.pressel_data_process import (
    get_pressel_types, 
    get_pressel_finish,
    get_polycarbonate_colour,
    get_pressel_legend
)
from .conf_specific_data.three_part_kit_components import (
    BUTTON_BODY,
    LED_VOLTAGE,
    SURROUND_TYPE,
    SURROUND_COLOR,
    SURROUND_FORM,
    get_contact_type,
    get_led_color   
)


class StandButtonForm(forms.Form):
    button_body = forms.ChoiceField(
        choices=BUTTON_BODY,
        label='Button body',
        widget=forms.Select(attrs={
            "hx-get": "load_contact_types/", 
            "hx-target": "#id_contact_type"})
    )
    contact_type = forms.ChoiceField(
        choices=[("", "Select contact type")],
        label='Contact type',
    )
    led_voltage = forms.ChoiceField(
        choices=LED_VOLTAGE,
        label="LED voltage",
        widget=forms.Select(attrs={
            "hx-get": "load_colors/", 
            "hx-target": "#id_led_color"})
    )
    led_color = forms.ChoiceField(
        choices=[("", "Select illumination color")],
        label='LED color'
    )
    surround_type = forms.ChoiceField(
        choices=SURROUND_TYPE,
        label="Surround type"
    )
    surround_color = forms.ChoiceField(
        choices=SURROUND_COLOR,
        label="Surround color"
    )
    surround_form = forms.ChoiceField(
        choices=SURROUND_FORM,
        label="Surround form"
    )
   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "button_body" in self.data:
            type = self.data.get("button_body")
            self.fields['contact_type'].choices = get_contact_type(type)
        if "led_voltage" in self.data:
            led_voltage = self.data.get("led_voltage")
            self.fields['led_color'].choices = get_led_color(led_voltage)


class PresselForm(forms.Form):
    type = forms.ChoiceField(
        choices=get_pressel_types(),
        label='Pressel Type',
        widget=forms.Select(attrs={
            "hx-get": "load_pressel_finish/", 
            "hx-target": "#id_pressel_finish"})
    )
    pressel_finish = forms.ChoiceField(
        choices=[('', 'Select pressel finish')],
        label='Pressel Finish',
        widget=forms.Select(attrs={
            "hx-get": "load_polycarbonate_color/", 
            "hx-target": "#id_polycarbonate_color",
            "hx-include": "[name='type']",
            })
    )
    polycarbonate_color = forms.ChoiceField(
        choices=[('', 'Select polycarbonate color')],
        label='Polycarbonate Color',
        widget=forms.Select(attrs={
            "hx-get": "load_legend/", 
            "hx-target": "#id_pressel_legend",
            "hx-include": "[name='type'], [name='pressel_finish']"})
    )
    pressel_legend = forms.ChoiceField(
        choices=[('', 'Select pressel legend')], 
        label='Pressel Legend'
        )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "type" in self.data:
            type = self.data.get("type")
            self.fields['pressel_finish'].choices = get_pressel_finish(type)
        if "type" in self.data and "pressel_finish" in self.data:
            type = self.data.get("type")
            finish = self.data.get("pressel_finish")
            self.fields['polycarbonate_color'].choices = get_polycarbonate_colour(type, finish)
        if "type" in self.data and "pressel_finish" in self.data and "polycarbonate_color" in self.data:
            type = self.data.get("type")
            finish = self.data.get("pressel_finish")
            polycarb_color = self.data.get("polycarbonate_color")
            self.fields['pressel_legend'].choices = get_pressel_legend(type, finish, polycarb_color)

