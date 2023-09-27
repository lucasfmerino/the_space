from django.shortcuts import render

# Create your views here.



def index(request):
    photo_data = {
    1: {"name": "Nebulosa de Carina",
        "legend": "webbtelescope.org / NASA / James Webb"},
    2: {"name": "Galáxia NGC 1079",
        "legend": "nasa.org / NASA / Hubble"},
    }
    return render(request, 'gallery/index.html', {"index_cards": photo_data})


def image(request):
    return render(request, 'gallery/image.html')
