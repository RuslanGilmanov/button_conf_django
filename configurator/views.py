from django.shortcuts import render
from django.http import HttpResponse
from .forms import StandardButtonForm, BUTTON_BODIES
from .models import ButtonBody, PresselType


def index(request):
    context = {
        'title': 'Home page',
        'buttons': 'buttons'
    }
    return render(request, 'configurator/home.html', context)


def standard_button(request):

    if request.method == 'POST':
        form = StandardButtonForm(request.POST)

        if form.is_valid():
            selected_body = form.cleaned_data['button_body']
            selected_pressel = form.cleaned_data['pressel_type']
            selected_contacts = form.cleaned_data['contact_arr']

            # button_body_code = dict(BUTTON_BODIES).get(selected_body)
            butt_code = f"DEW BUT {selected_body}{selected_pressel}{selected_contacts}"
            context = {
                'title': 'Standard button',
                'form': form,
                'button_code': butt_code
            }

            return render(request, 'configurator/standard_button.html', context)
    else:
        form = StandardButtonForm()

    context = {
        'title': 'Standard button',
        'form': form
    }
    return render(request, 'configurator/standard_button.html', context)
