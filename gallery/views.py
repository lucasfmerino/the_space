from django.shortcuts import render, get_object_or_404

from gallery.models import Photography

# Create your views here.



def index(request):

    # photo_data = {
    # 1: {"name": "Nebulosa de Carina",
    #     "legend": "webbtelescope.org / NASA / James Webb"},
    # 2: {"name": "Galáxia NGC 1079",
    #     "legend": "nasa.org / NASA / Hubble"},
    # }

    photographs = Photography.objects.all()
    return render(request, 'gallery/index.html', {"index_cards": photographs})


def image(request, photography_id):
    photography = get_object_or_404(Photography, pk=photography_id)
    return render(request, 'gallery/image.html', {"photography": photography})
