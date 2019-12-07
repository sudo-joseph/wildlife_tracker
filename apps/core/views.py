from django.shortcuts import render
import json
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
