from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .forms import StandButtonForm, PresselForm
from .conf_specific_data.pressel_data_process import (
    search_in_pressel_dict,
    get_pressel_finish,
    get_polycarbonate_colour,
    get_pressel_legend
    )
from .conf_specific_data.three_part_kit_components import (
    get_contact_type,
    get_led_color
    )


def index(request):
    context = {
        'title': 'Home page',
    }
    return render(request, 'configurator/index.html', context)


def standard_button(request):

    button_code = None

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

            button_code = f"DEW KIT " \
                        f"{selected_body}" \
                        f"{selected_contact}" \
                        f"{selected_led_color}"\
                        f"{selected_led_voltage}" \
                        f"{selected_surround_type}" \
                        f"{selected_surround_color}" \
                        f"{selected_surround_form}"

        else:
            form = StandButtonForm()

    else:
        form = StandButtonForm()
    
    context = {
            'title': 'Standard button',
            'form': form,
            'button_code': button_code
        }
    
    return render(request, 'configurator/standard_button.html', context)


def load_contact_types(request):
    body = request.GET.get("button_body")
    contacts = get_contact_type(body)
    return render(request, 'configurator/contact_options.html', {"contacts": contacts})


def load_colors(request):
    led_volt = request.GET.get("led_voltage")
    led_colors = get_led_color(led_volt)
    return render(request, 'configurator/led_color_options.html', {"led_colors": led_colors})


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