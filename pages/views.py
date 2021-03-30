from django.shortcuts import render, HttpResponse
from utilities.mock_data import images_generator



# Create your views here.
def home_view(request):
    # todo create a model for this
    context = {
        "titles": '"feherrozi"',
        "subtitles": "Ahol a képzelet és a vászon találkozik",
        "content": "Háziaszony vagyok, és festő. Kreatív képeimmel szeretném azt megmutatni, ami nem létezik (vagy mégis?) Célom, hogy az emberek megálljanak képeim előtt és elgondolkozzanak. Érezzenek valamit, csodálkozzanak, szeressék, gyűlöljék, de mindenképp érzéseket váltson ki. Ne egyszerűen csak elmenjenek előtte, továbblépjenek. És ha valaki visszatér, hogy újra megnézze, akkor már boldog vagyok.",
        "photos": images_generator(5)

    }
    return render(request, "home.html", context)

def about_view(request):
    # todo create a model for this
    context = {
        "title": "Hogyan is készülnek a képeim?",
        "subtitle": "",
        "content": "Előszőr is tervezéssel! Sokat rajzolok, vázlatokat készítek a festés előtt. Egyrészt, szeretek koncepcióval készülni, és ha megrendelésre dolgozom, szeretek az elképzeléshez, modellhez legjobban illő ötletekkel előállni. A vászon elé emiatt felkészülten érkezek, és lehet is a koncepció kivitelezésével foglalkozni.",
        "photos": images_generator(1)

    }
    return render(request, "about.html", context)


def contact_view(request):
    # todo create a model for this
    context = {
        "title": "Kérjen tőlünk ajánlatot!",
        "subtitle": "",
        "content": "",
        "photos": images_generator(1)
    }
    return render(request, "contact.html", context)