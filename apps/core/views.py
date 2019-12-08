from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import json

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


def map(request):
    reports = [{'lat': '37.844170',
                'lon': '-122.275153',
                'sometext': 'number 1',
                },
               {'lat': '37.871459',
                'lon': '-122.242401',
                'sometext': 'number 2',
                },
               {'lat': '37.835747',
                'lon': '-122.237114',
                'sometext': 'number 3',
                },
               {'lat': '37.831025',
                'lon': '-122.295640',
                'sometext': 'number 4',
                },
               ]
    context = {'reports': reports
               }

    return render(request, 'pages/map.html', context)

def report(request):

    reports = [{'lat': '37.844170',
                'lon': '-122.275153',
                'sometext': 'number 1',
                },
               {'lat': '37.871459',
                'lon': '-122.242401',
                'sometext': 'number 2',
                },
               {'lat': '37.835747',
                'lon': '-122.237114',
                'sometext': 'number 3',
                },
               {'lat': '37.831025',
                'lon': '-122.295640',
                'sometext': 'number 4',
                },
               ]
    context = {'reports': reports
               }
    if request.method == 'POST':
        print(json.loads(request.body))

    return render(request, 'pages/map.html', context)

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
