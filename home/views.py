from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home:main"))
    # test si authentifié, si oui, rediriger vers convention/index...
    return render(request, "index.html")

def main(request):
    return render(request, "main.html")
