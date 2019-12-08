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
    context = {
    }

    return render(request, 'pages/about.html', context)

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

