"""
Views for home module
"""
import uuid
from base64 import b64encode
from http import HTTPStatus

import requests
from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView
from django.http import HttpResponseRedirect

from home.forms import UploadFileForm


class Tableau(FormView):
    form_class = UploadFileForm
    template_name = "index.html"

    def form_valid(self, form):
        username, password = list(settings.BASICAUTH_USERS.items())[0]
        response = requests.post(
            settings.GENERATOR_SERVICE_HOST,
            files={"file": form.cleaned_data["file"]},
            auth=(username, password),
        )
        return _forward_http_file(response)

tableau = Tableau.as_view()

def tableau_redirect(request):
    return HttpResponseRedirect(reverse('home:tableau'))

def publication_upload(request):
    # FIXME: Utiliser Formulaire Django

    generation_id = uuid.uuid4()
    upload_url = _generate_publication_url(generation_id, "upload_input")
    launch_generation_url = _generate_publication_url(generation_id, "generate")

    username, password = _get_basicauth_credentials()
    auth_token = b64encode(bytes(f"{username}:{password}", encoding="utf8")).decode(
        "utf8"
    )

    return render(
        request,
        "publication_upload.html",
        {
            "generation_id": generation_id,
            "upload_url": upload_url,
            "launch_generation_url": launch_generation_url,
            "auth_token": auth_token,
        },
    )


def publication_display(request, generation_id):
    publication_url = _generate_publication_url(generation_id, "")
    username, password = _get_basicauth_credentials()
    response = requests.get(
        publication_url,
        auth=(username, password),
    )

    if response.status_code == HTTPStatus.OK:
        return _forward_http_file(response)

    return HttpResponse("<meta http-equiv='refresh' content='10'>")


def _forward_http_file(response):
    http_response = FileResponse(response)
    headers_to_forward = ["Content-Type", "Content-Length", "Content-Disposition"]
    for header in headers_to_forward:
        http_response.headers[header] = response.headers[header]
    return http_response


def _get_basicauth_credentials():
    return list(settings.BASICAUTH_USERS.items())[0]


def _generate_publication_url(generation_id, suffix):
    return f"{settings.GENERATOR_SERVICE_HOST}/publication/{generation_id}/{suffix}"
