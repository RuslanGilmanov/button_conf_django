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
from .conf_specific_data.pressel_data_process import (
    get_pressel_types, 
    get_pressel_finish,
    get_polycarbonate_colour,
    get_pressel_legend
)

from .conf_specific_data.three_part_kit_components import (
    BUTTON_BODY,
    get_contact_type,
    LED_COLOR,
    LED_VOLTAGE,
    SURROUND_TYPE,
    SURROUND_COLOR,
    SURROUND_FORM
)

# class StandardButtonForm(forms.Form):
#     button_body = forms.ModelChoiceField(
#         queryset=ButtonBody.objects.all(),
#         widget=forms.Select(attrs={"hx-get": "load_contact_types/", "hx-target": "#id_contact_type"}))
#     contact_type = forms.ModelChoiceField(queryset=ContactType.objects.none())
#     led_voltage = forms.ModelChoiceField(
#         queryset=IlluminationVoltage.objects.all(),
#         widget=forms.Select(attrs={"hx-get": "load_colors/", "hx-target": "#id_led_color"}))
#     led_color = forms.ModelChoiceField(queryset=IlluminationColor.objects.none())
#     surround_type = forms.ModelChoiceField(queryset=SurroundType.objects.all())
#     surround_color = forms.ModelChoiceField(queryset=SurroundColor.objects.all())
#     surround_form = forms.ModelChoiceField(queryset=SurroundForm.objects.all())

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         if "button_body" in self.data and "led_color" in self.data:
#             body_id = int(self.data.get("button_body"))
#             button_body = ButtonBody.objects.get(id=body_id)
#             led_id = int(self.data.get("led_voltage"))
#             led_voltage = IlluminationVoltage.objects.get(id=led_id)
#             self.fields["contact_type"].queryset = button_body.contact_types.all()
#             self.fields["led_color"].queryset = led_voltage.led_colors.all()


class StandButtonForm(forms.Form):
    button_body = forms.ChoiceField(
        choices=BUTTON_BODY,
        label='Button body',
        widget=forms.Select(attrs={
            "hx-get": "load_contact_types/", 
            "hx-target": "#id_contact_type"})
    )
    contact_type = forms.ChoiceField(
        choices=[("None", "Select contact type")],
        label='Contact type'
    )
    led_voltage = forms.ChoiceField(
        choices=LED_VOLTAGE,
        label="LED voltage"
    )

    # pressel_finish = forms.ChoiceField(
    #     choices=[('None', 'Select pressel finish')],
    #     label='Pressel Finish',
    #     widget=forms.Select(attrs={
    #         "hx-get": "load_polycarbonate_color/", 
    #         "hx-target": "#id_polycarbonate_color",
    #         "hx-include": "[name='type']",
    #         })
    # )
    # polycarbonate_color = forms.ChoiceField(
    #     choices=[('None', 'Select polycarbonate color')],
    #     label='Polycarbonate Color',
    #     widget=forms.Select(attrs={
    #         "hx-get": "load_legend/", 
    #         "hx-target": "#id_pressel_legend",
    #         "hx-include": "[name='type'], [name='pressel_finish']"})
    # )
    # pressel_legend = forms.ChoiceField(
    #     choices=[('None', 'Select pressel legend')], 
    #     label='Pressel Legend'
    #     )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "button_body" in self.data:
            type = self.data.get("button_body")
            self.fields['contact_type'].choices = get_contact_type(type)
    #     if "type" in self.data and "pressel_finish" in self.data:
    #         type = self.data.get("type")
    #         finish = self.data.get("pressel_finish")
    #         self.fields['polycarbonate_color'].choices = get_polycarbonate_colour(type, finish)
    #     if "type" in self.data and "pressel_finish" in self.data and "polycarbonate_color" in self.data:
    #         type = self.data.get("type")
    #         finish = self.data.get("pressel_finish")
    #         polycarb_color = self.data.get("polycarbonate_color")
    #         self.fields['pressel_legend'].choices = get_pressel_legend(type, finish, polycarb_color)


class PresselForm(forms.Form):
    type = forms.ChoiceField(
        choices=get_pressel_types(),
        label='Pressel Type',
        widget=forms.Select(attrs={
            "hx-get": "load_pressel_finish/", 
            "hx-target": "#id_pressel_finish"})
    )
    pressel_finish = forms.ChoiceField(
        choices=[('None', 'Select pressel finish')],
        label='Pressel Finish',
        widget=forms.Select(attrs={
            "hx-get": "load_polycarbonate_color/", 
            "hx-target": "#id_polycarbonate_color",
            "hx-include": "[name='type']",
            })
    )
    polycarbonate_color = forms.ChoiceField(
        choices=[('None', 'Select polycarbonate color')],
        label='Polycarbonate Color',
        widget=forms.Select(attrs={
            "hx-get": "load_legend/", 
            "hx-target": "#id_pressel_legend",
            "hx-include": "[name='type'], [name='pressel_finish']"})
    )
    pressel_legend = forms.ChoiceField(
        choices=[('None', 'Select pressel legend')], 
        label='Pressel Legend'
        )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically populate finish and legend based on selection
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

