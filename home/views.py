"""
Views for home module
"""
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    """
    Check the authentication and redirect or render html following the authentication status of
    the user.
    """
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home:main"))
    # test si authentifié, si oui, rediriger vers convention/index...
    return render(request, "index.html")


@login_required
def main(request):
    """
    Render the main page when user is logged
    """
    return render(request, "main.html")
