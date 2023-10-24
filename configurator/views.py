from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .forms import StandardButtonForm, BUTTON_BODIES


def index(request):
    context = {
        'title': 'Home page',
        # 'buttons': 'buttons'
    }
    return render(request, 'configurator/index.html', context)


def standard_button(request):

    if request.method == 'POST':
        form = StandardButtonForm(request.POST)

        contacts = request.POST.get('contact_arr')
        print(contacts)

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


def get_contact_type(request):
    button_body = request.GET.get('button_body')
    # Perform logic to retrieve pressel types based on the selected button_body
    if button_body == '3' or button_body == '8' or button_body == '7':
        contact_types = {"0": "Select contact type", "1": "2 x N/O", "2": "2 x N/C", "3": "1 x N/O 1 x N/C"}
        return JsonResponse(contact_types)
    elif button_body == '4':
        contact_types = {'5': "1 x N/O (Micro AMP)"}
        return JsonResponse(contact_types)
    else:
        # If no contact types are available, return a suitable response, e.g., a 400 Bad Request.
        return HttpResponseBadRequest("Invalid button body selection")
