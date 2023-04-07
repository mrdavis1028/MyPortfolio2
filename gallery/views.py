from django.shortcuts import render

# Create your views here.
def caps(request):
    return render(request, 'gallery/gradCaps.html')


def wavers(request):
    return render(request, 'gallery/TopWavers.html')


def delikat(request):
    return render(request, 'gallery/Delikat.html')


def astro(request):
    return render(request, 'gallery/AstroShirts.html')


def site(request):
    return render(request, 'gallery/MakingSite.html')


def art(request):
    return render(request, 'gallery/ArtPort.html')