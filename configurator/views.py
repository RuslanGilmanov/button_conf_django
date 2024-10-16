from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .forms import StandButtonForm, PresselForm
from .models import (
    ContactType,
    ButtonBody,
    IlluminationVoltage,
    IlluminationColor,
    SurroundType,
    SurroundColor,
    SurroundForm,
    Pressel,
    PresselType,
    PresselLegend,
    PresselFinish,
    PresselPolycarbonateColour
)
from .conf_specific_data.pressel_data_process import (search_in_pressel_dict,
                                                      get_pressel_finish,
                                                      get_polycarbonate_colour,
                                                      get_pressel_legend)

from .conf_specific_data.three_part_kit_components import get_contact_type


def index(request):
    context = {
        'title': 'Home page',
        # 'buttons': 'buttons'
    }
    return render(request, 'configurator/index.html', context)


def standard_button(request):

    if request.method == 'POST':
        form = StandButtonForm(request.POST)
        if form.is_valid():
            selected_body = form.cleaned_data['button_body']
            selected_contact = form.cleaned_data['contact_type']
            selected_led_color = form.cleaned_data['led_color']
            selected_led_voltage = form.cleaned_data['led_voltage']
            selected_surround_type = form.cleaned_data['surround_type']
            selected_surround_color = form.cleaned_data['surround_color']
            selected_surround_form = form.cleaned_data['surround_form']
            # button_body = ButtonBody.objects.filter(body=selected_body).first()
            # contact_type = ContactType.objects.filter(contact=selected_contact).first()
            # led_color = IlluminationColor.objects.filter(led_color=selected_led_color).first()
            # led_voltage = IlluminationVoltage.objects.filter(voltage=selected_led_voltage).first()
            # surround_type = SurroundType.objects.filter(surround=selected_surround_type).first()
            # surround_color = SurroundColor.objects.filter(surround_color=selected_surround_color).first()
            # surround_form = SurroundForm.objects.filter(surround_form=selected_surround_form).first()

            butt_code = f"DEW KIT " \
                        f"{selected_body}" \
                        f"{selected_contact}" \
                        f"{selected_led_color}"\
                        f"{selected_led_voltage}" \
                        f"{selected_surround_type}" \
                        f"{selected_surround_color}" \
                        f"{selected_surround_form}"

            context = {
                'title': 'Standard button',
                'form': form,
                'button_code': butt_code
            }

            return render(request, 'configurator/standard_button.html', context)

        else:
            print(form.errors)

    else:
        form = StandButtonForm()
    

        context = {
            'title': 'Standard button',
            'form': form,
        }
        return render(request, 'configurator/standard_button.html', context)


def load_contact_types(request):
    body = request.GET.get("button_body")
    contacts = get_contact_type(body)
    return render(request, 'configurator/contact_options.html', {"contacts": contacts})


def load_colors(request):
    led_volt_id = request.GET.get("led_voltage")
    try:
        led_voltage = IlluminationVoltage.objects.get(id=led_volt_id)
        led_colors = led_voltage.led_colors.all()
        return render(request, 'configurator/led_color_options.html', {"led_colors": led_colors})

    except IlluminationVoltage.DoesNotExist:
        return JsonResponse({'error': 'LED Voltage not found'})


# def get_contact_type(request):
#     button_body = request.GET.get('button_body')
#     # Perform logic to retrieve pressel types based on the selected button_body
#     if button_body == 1 or button_body == 2 or button_body == 3:
#         contact_types = {"0": "Select contact type", "1": "2 x N/O", "2": "2 x N/C", "3": "1 x N/O 1 x N/C"}
#         return JsonResponse(contact_types)
#     elif button_body == '4':
#         contact_types = {'5': "1 x N/O (Micro AMP)"}
#         return JsonResponse(contact_types)
#     else:
#         # If no contact types are available, return a suitable response, e.g., a 400 Bad Request.
#         return HttpResponseBadRequest("Invalid button body selection")


def load_legends(request):
    pressel_type = request.GET.get('type')
    pressel_finish = request.GET.get('pressel_finish')
    polycarb_color = request.GET.get('polycarbonate_color')
    pressel_legends = get_pressel_legend(pressel_type, pressel_finish, polycarb_color)
    return render(request, 'configurator/pressel_legend_options.html', {"pressel_legends": pressel_legends})
    

def load_finish(request):
    pressel_type = request.GET.get('type')
    finishes = get_pressel_finish(pressel_type)
    return render(request, 'configurator/pressel_finish_options.html', {"pressel_finishes": finishes})


def load_polycarb_color(request):
    pressel_type = request.GET.get('type')
    pressel_finish = request.GET.get('pressel_finish')
    polycarb_colors = get_polycarbonate_colour(pressel_type, pressel_finish)
    return render(request, 'configurator/pressel_polycarb_color_options.html', {"pressel_polycarb_colors": polycarb_colors})


def select_pressel(request):
    pressel_code = None

    if request.method == 'POST':
        form = PresselForm(request.POST)

        if form.is_valid():
            selected_pressel_type = form.cleaned_data['type']
            selected_pressel_finish = form.cleaned_data['pressel_finish']
            selected_polycarbonate_color = form.cleaned_data['polycarbonate_color']
            selected_pressel_legend = form.cleaned_data['pressel_legend']

            pressel_code = search_in_pressel_dict(
                pressel_type=selected_pressel_type,
                polycarb_color=selected_polycarbonate_color,
                pressel_finish=selected_pressel_finish,
                pressel_legend=selected_pressel_legend,
            )
        else:
            form = PresselForm()
    
    else:
        form = PresselForm()

    context = {
        'title': 'Pressel Selection Page',
        'form': form,
        'pressel_code': pressel_code
    }

    return render(request, 'configurator/pressel_selection.html', context)
