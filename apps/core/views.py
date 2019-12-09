from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from .models import Report
import json
import time

class Report(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['type', 'lat_position', 'lon_position', 'text', 'image']

def home(request):
    context = {'example_context_variable': 'Change me.',
               'vlat': 37.8,
               'vlon': -122.27,
               'view': 12,
               'drag': 'false',
               }

    return render(request, 'pages/home.html', context)


def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)


def add_new(request):
    if  request.user.is_anonymous:
        context = {}
        return render(request, 'pages/login_required.html', context)

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
                       'drag': 'true'
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
