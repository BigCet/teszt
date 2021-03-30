from django.shortcuts import render
from utilities.mock_data import images_generator

# Create your views here.
def gallery_view(request):
    context = {
        "categories": ["Wedding", "Nature", "Sport"],
        "photos": images_generator(50)
    }
    return render(request, "gallery.html", context)

def photo_details(request, slug):
    context={
        "photo": f"https://source.unsplash.com/1600x900/?nature{slug},water{slug}",
        "title": "Ez itt a kép",
        "subtitle": "2020 aug. 1.",
        "content": "Kép leírása...",
    }

    return render(request, "photo_details.html", context)