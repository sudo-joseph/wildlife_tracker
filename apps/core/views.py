from django.shortcuts import render
from django.http import HttpResponse
from django import forms 


class IncidentReport(forms.Form):
    reporter = forms.CharField(max_length=20)
    email = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)

    location_address = forms.CharField(max_length=120)
    date_incident = forms.CharField(max_length=20)
    date_reported = forms.CharField(max_length=20)
    date_update = forms.CharField(max_length=20)
    description = forms.CharField(max_length=20)


def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)

def add_new(request):
    if request.method == 'POST':
        form = IncidentReport(request.POST)
        if form.is_valid():
            return HttpResponse("<h1>Thank you for the report!</h1>")
    else:
        form = IncidentReport()

    context = {
        'form': form,
    }

    return render(request, 'pages/add_report.html', context)
