from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .forms import StandardButtonForm, PresselForm
from .models import (
    ContactType,
    ButtonBody,
    IlluminationVoltage,
    IlluminationColor,
    SurroundType,
    SurroundColor,
    SurroundForm,
    Pressel
)
import csv


def index(request):
    context = {
        'title': 'Home page',
        # 'buttons': 'buttons'
    }
    return render(request, 'configurator/index.html', context)


def standard_button(request):

    if request.method == 'POST':
        form = StandardButtonForm(request.POST)
        if form.is_valid():
            selected_body = form.cleaned_data['button_body']
            selected_contact = form.cleaned_data['contact_type']
            selected_led_voltage = form.cleaned_data['led_voltage']
            selected_led_color = form.cleaned_data['led_color']
            selected_surround_type = form.cleaned_data['surround_type']
            selected_surround_color = form.cleaned_data['surround_color']
            selected_surround_form = form.cleaned_data['surround_form']
            button_body = ButtonBody.objects.filter(body=selected_body).first()
            contact_type = ContactType.objects.filter(contact=selected_contact).first()
            led_voltage = IlluminationVoltage.objects.filter(voltage=selected_led_voltage).first()
            led_color = IlluminationColor.objects.filter(led_color=selected_led_color).first()
            surround_type = SurroundType.objects.filter(surround=selected_surround_type).first()
            surround_color = SurroundColor.objects.filter(surround_color=selected_surround_color).first()
            surround_form = SurroundForm.objects.filter(surround_form=selected_surround_form).first()

            butt_code = f"DEW KIT " \
                        f"{button_body.body_code}" \
                        f"{contact_type.contact_code}" \
                        f"{led_voltage.volt_code}" \
                        f"{led_color.led_code}" \
                        f"{surround_type.surround_code}" \
                        f"{surround_color.sur_color_code}" \
                        f"{surround_form.form_code}"

            context = {
                'title': 'Standard button',
                'form': form,
                'button_code': butt_code
            }

            return render(request, 'configurator/standard_button.html', context)

        else:
            print(form.errors)

    else:
        form = StandardButtonForm()
        pressel_form = PresselForm()
        # print(pressel_form)

        context = {
            'title': 'Standard button',
            'form': form,
            'pressel_form': pressel_form
        }
        return render(request, 'configurator/standard_button.html', context)


def load_contact_types(request):
    body_id = request.GET.get("button_body")
    try:
        button_body = ButtonBody.objects.get(id=body_id)
        contacts = button_body.contact_types.all()
        return render(request, 'configurator/contact_options.html', {"contacts": contacts})

    except ButtonBody.DoesNotExist:
        return JsonResponse({'error': 'ButtonBody not found'})


def load_colors(request):
    led_volt_id = request.GET.get("led_voltage")
    try:
        led_voltage = IlluminationVoltage.objects.get(id=led_volt_id)
        led_colors = led_voltage.led_colors.all()
        return render(request, 'configurator/led_color_options.html', {"led_colors": led_colors})

    except IlluminationVoltage.DoesNotExist:
        return JsonResponse({'error': 'LED Voltage not found'})


def get_contact_type(request):
    button_body = request.GET.get('button_body')
    # Perform logic to retrieve pressel types based on the selected button_body
    if button_body == 1 or button_body == 2 or button_body == 3:
        contact_types = {"0": "Select contact type", "1": "2 x N/O", "2": "2 x N/C", "3": "1 x N/O 1 x N/C"}
        return JsonResponse(contact_types)
    elif button_body == '4':
        contact_types = {'5': "1 x N/O (Micro AMP)"}
        return JsonResponse(contact_types)
    else:
        # If no contact types are available, return a suitable response, e.g., a 400 Bad Request.
        return HttpResponseBadRequest("Invalid button body selection")


# def read_legends_from_scv():
#     legend_codes = []
#
#     with open('configurator/static/legends/Legend Codes_csv.csv', newline='') as csvfile:
#         csv_reader = csv.DictReader(csvfile)
#         for row in csv_reader:
#             legend_codes.append(row)
#
#     return legend_codes

def load_legends(request):
    body_id = request.GET.get("button_body")
    try:
        button_body = ButtonBody.objects.get(id=body_id)
        contacts = button_body.contact_types.all()
        return render(request, 'configurator/contact_options.html', {"contacts": contacts})

    except ButtonBody.DoesNotExist:
        return JsonResponse({'error': 'ButtonBody not found'})
