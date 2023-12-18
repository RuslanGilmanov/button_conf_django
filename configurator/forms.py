from django import forms
from .models import (
    ButtonBody,
    ContactType,
    IlluminationColor,
    IlluminationVoltage,
    SurroundType,
    SurroundColor,
    SurroundForm,
    Pressel
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


class PresselForm(forms.ModelForm):
    pressel_type = forms.ModelChoiceField(
    queryset=Pressel.objects.values('type').distinct(),
    widget=forms.Select(attrs={"hx-get": "load_pressel_legend/", "hx-target": "#id_pressel_legend"}))

    class Meta:
        model = Pressel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Access the values of the queryset
        pressel_type_values = Pressel.objects.values_list('type', flat=True).distinct()

        # Update the choices for the pressel_type field
        self.fields['pressel_type'].queryset = pressel_type_values

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     # Populate fields with distinct querysets
    #     self.fields['type'].queryset = Pressel.objects.values('type').distinct()
    #     self.fields['legend'].queryset = Pressel.objects.values('legend').distinct()
    #     self.fields['pressel_stock_code'].queryset = Pressel.objects.values('pressel_stock_code').distinct()
    #     self.fields['pressel_finish'].queryset = Pressel.objects.values('pressel_finish').distinct()
    #     self.fields['polycarbonate_colour'].queryset = Pressel.objects.values('polycarbonate_colour').distinct()
