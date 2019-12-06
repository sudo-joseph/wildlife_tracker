from django.shortcuts import render

# Two example views. Change or delete as necessary.
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
