"""
Views for home module
"""
import datetime
import uuid
from base64 import b64encode
from collections import defaultdict
from http import HTTPStatus

from django.conf import settings
from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import FormView

from . import generator
from .forms import (
    PublicationReferentielPreparationForm,
    PublicationReferentielProductionForm,
    UploadFileForm,
)


class Tableau(FormView):
    form_class = UploadFileForm
    template_name = "tableau_upload.html"

    def form_valid(self, form):
        response = generator.post(
            settings.GENERATOR_SERVICE_HOST, files={"file": form.cleaned_data["file"]}
        )
        return _forward_http_file(response)


tableau = Tableau.as_view()


def tableau_redirect(request):
    return HttpResponseRedirect(reverse("home:tableau"))


def publication_upload(request):
    # FIXME: Utiliser Formulaire Django

    generation_id = uuid.uuid4()
    upload_url = _generate_publication_url(generation_id, "upload_input")
    launch_generation_url = _generate_publication_url(generation_id, "generate")

    auth_token = b64encode(
        bytes(
            f"{settings.GENERATOR_USERNAME}:{settings.GENERATOR_PASSWORD}",
            encoding="utf8",
        )
    ).decode("utf8")

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


class PublicationReferentiel(FormView):
    form_class = PublicationReferentielPreparationForm
    template_name = "publication_referentiel.html"

    def form_valid(self, form):
        response = generator.post(
            f"{settings.GENERATOR_SERVICE_HOST}/publication/from_preparation/generate",
            {"ouvrage": form.cleaned_data["ouvrage"]},
        )
        json_response = response.json()
        generation_id = json_response["generation_id"]

        return redirect("home:publication_display", generation_id=generation_id)


publication_referentiel = PublicationReferentiel.as_view()


def publication_display(request, generation_id):
    publication_url = _generate_publication_url(generation_id, "")
    response = generator.get(publication_url)

    if response.status_code == HTTPStatus.OK:
        return _forward_http_file(response)

    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return render(
            request,
            "publication_generation_failed.html",
            {"generation_id": generation_id},
        )

    logs = ""
    if response.status_code == HTTPStatus.NOT_FOUND:
        logs = str(response.content, "utf-8")

    return render(
        request,
        "generating_page.html",
        {"logs": logs},
    )


class PublicationProd(FormView):
    form_class = PublicationReferentielProductionForm
    template_name = "publication_prod.html"

    def form_valid(self, form):
        response = generator.post(
            f"{settings.GENERATOR_SERVICE_HOST}/publication/from_production/generate",
            {"ouvrage": form.cleaned_data["ouvrage"]},
        )
        json_response = response.json()
        generation_id = json_response["generation_id"]

        return redirect("home:publication_display", generation_id=generation_id)

    def get_context_data(self, **kwargs):
        ouvrages_from_generator = generator.get(
            f"{settings.GENERATOR_SERVICE_HOST}/publication/from_production/list"
        ).json()
        ouvrage_list = defaultdict(dict)
        for ouvrage, files in ouvrages_from_generator.items():
            document_date = datetime.datetime.fromisoformat(
                # Le problème du Z est corrigé dans Python 3.11 : https://docs.python.org/3.11/whatsnew/3.11.html#datetime
                files["document.pdf"]["date"].replace("Z", "+00:00")
            ).date()
            ouvrage_list[document_date][ouvrage] = files
            ouvrage_list[document_date] = dict(
                sorted(ouvrage_list[document_date].items())
            )
        kwargs["ouvrages"] = dict(sorted(ouvrage_list.items(), reverse=True))
        return super().get_context_data(**kwargs)


publication_prod = PublicationProd.as_view()


def _forward_http_file(response):
    http_response = FileResponse(response)
    headers_to_forward = ["Content-Type", "Content-Length", "Content-Disposition"]
    for header in headers_to_forward:
        http_response.headers[header] = response.headers[header]
    return http_response


def _generate_publication_url(generation_id, suffix):
    return f"{settings.GENERATOR_SERVICE_HOST}/publication/{generation_id}/{suffix}"
