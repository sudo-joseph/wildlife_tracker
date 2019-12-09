from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from .models import Report
import json
import time

class IncidentReport(forms.Form):
    reporter = forms.CharField(max_length=20)
    email = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    location_address = forms.CharField(max_length=120)
    date_incident = forms.CharField(max_length=20)
    date_reported = forms.CharField(max_length=20)
    date_update = forms.CharField(max_length=20)
    description = forms.CharField(max_length=20)

class Report(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['type', 'lat_position', 'lon_position', 'text', 'image']

def home(request):

    context = {
        'example_context_variable': 'Change me.',
        'vlat': 37.8,
        'vlon': -122.27,
        'view': 12
    }

    return render(request, 'pages/home.html', context)


def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)


def add_new(request):
    if 'lat' not in request.session.keys():
        time.sleep(1)
        return add_new(request)
    else:
        if request.method == 'POST':
            print('im getting here')
            form = Report(request.POST)
            if form.is_valid():
                report = form.save(commit=False)
                report.user = request.user
                report.save()
                return redirect('/')

        else:
            print("Lat: ", request.session['lat'],
                  "Lon: ", request.session['lon'])
            reports = [{'lat': request.session['lat'],
                        'lon': request.session['lon'],
                        'sometext': '',
                        }]
            form = Report(initial={'lat_position': request.session['lat'],
                                   'lon_position': request.session['lon']
                                   })
            context = {'form': form,
                       'reports': reports,
                       'vlat': request.session['lat'],
                       'vlon': request.session['lon'],
                       'view': '18',
                       }
            return render(request, 'pages/add_report.html', context)

def log_location(request):
    loc = json.loads(request.body)
    request.session['lat'] = loc['lat']
    request.session['lon'] = loc['lon']
    return HttpResponse(request)

def edit(request, id):
    context = {
    }

    return render(request, 'pages/about.html', context)

def list_view(request):
    context = {
    }

    return render(request, 'pages/about.html', context)

def delete(request, id):
    context = {
    }

    return render(request, 'pages/about.html', context)
