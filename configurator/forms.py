from django import forms
from .models import (
    ButtonBody,
    ContactType,
    IlluminationColor,
    IlluminationVoltage,
    SurroundType,
    SurroundColor,
    SurroundForm,
    Pressel,
    PresselType,
    PresselLegend,
    PresselFinish,
    PresselPolycarbonateColour
)


class StandardButtonForm(forms.Form):
    button_body = forms.ModelChoiceField(
        queryset=ButtonBody.objects.all(),
        widget=forms.Select(attrs={"hx-get": "load_contact_types/", "hx-target": "#id_contact_type"}))
    contact_type = forms.ModelChoiceField(queryset=ContactType.objects.none())
    led_voltage = forms.ModelChoiceField(
        queryset=IlluminationVoltage.objects.all(),
        widget=forms.Select(attrs={"hx-get": "load_colors/", "hx-target": "#id_led_color"}))
    led_color = forms.ModelChoiceField(queryset=IlluminationColor.objects.none())
    surround_type = forms.ModelChoiceField(queryset=SurroundType.objects.all())
    surround_color = forms.ModelChoiceField(queryset=SurroundColor.objects.all())
    surround_form = forms.ModelChoiceField(queryset=SurroundForm.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "button_body" in self.data and "led_color" in self.data:
            body_id = int(self.data.get("button_body"))
            button_body = ButtonBody.objects.get(id=body_id)
            led_id = int(self.data.get("led_voltage"))
            led_voltage = IlluminationVoltage.objects.get(id=led_id)
            self.fields["contact_type"].queryset = button_body.contact_types.all()
            self.fields["led_color"].queryset = led_voltage.led_colors.all()


class PresselForm(forms.Form):
    pressel_type = forms.ModelChoiceField(
        queryset=PresselType.objects.all(),
        widget=forms.Select(attrs={"hx-get": "load_legend/", "hx-target": "#id_legend"}))
    legend = forms.ModelChoiceField(queryset=PresselLegend.objects.none())
    pressel_finish = forms.ModelChoiceField(queryset=PresselFinish.objects.none())
    polycarbonate_colour = forms.ModelChoiceField(queryset=PresselPolycarbonateColour.objects.none())

    # pressel_legend = forms.ModelChoiceField(
    #     queryset=Pressel.objects.values_list('legend', flat=True).distinct())
    # pressel_finish = forms.ModelChoiceField(
    #     queryset=Pressel.objects.values_list('pressel_finish', flat=True).distinct())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

