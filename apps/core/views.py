from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from .models import Report
import json
import time


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['type', 'lat_position', 'lon_position', 'text', 'image']
        widgets = {'text': forms.Textarea()}


def home(request):
    reports = Report.objects.all().order_by('-created')

    loc_oakland = {'lat_position': 37.8, 'lon_position': -122.27, }
    map_zoom_level = 10

    context = {'example_context_variable': 'Change me.',
               'vlat': loc_oakland['lat_position'],
               'vlon': loc_oakland['lon_position'],
               'view': map_zoom_level,
               'drag': 'false',
               'reports': reports,
               }

    return render(request, 'pages/home.html', context)


def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)


def add_new(request):
    if request.user.is_anonymous:
        context = {}
        return render(request, 'pages/login_required.html', context)

    if 'lat' not in request.session.keys():
        loc_oakland = {'lat_position': 37.8, 'lon_position': -122.27, }
        request.session['lat'] = loc_oakland['lat_position']
        request.session['lon'] = loc_oakland['lon_position']

    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('/')

    else:
        reports = [{'lat_position': request.session['lat'],
                    'lon_position': request.session['lon'],
                    'text': '',
                    }]
        form = ReportForm(initial={'lat_position': request.session['lat'],
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
    request.session['lat'] = round(loc['lat'],7)
    request.session['lon'] = round(loc['lon'],7)
    return HttpResponse(request)


@login_required
def edit(request, id):
    report = Report.objects.get(id=id)

    if request.method == "POST":
        if report.user == request.user:
            form = ReportForm(request.POST, request.FILES, instance=report)
            if form.is_valid():
                form.save()
                return redirect('/account/users/' + request.user.username)
            else:
                messages.error(request, 'Form Validation Error at the server')
                return redirect('/')
        else:
            messages.error(request, 'Could not confirm if this record was filed by the current user.')
            return redirect('/')

    form = ReportForm(instance=report)
    context = {
        'form': form,
    }

    return render(request, 'pages/add_report.html', context)


def list_view(request):
    context = {
    }

    return render(request, 'pages/about.html', context)


@login_required
def delete(request, id):
    context = {
    }

    return render(request, 'pages/about.html', context)
