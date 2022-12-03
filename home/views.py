"""
Views for home module
"""
import uuid
from base64 import b64encode
from collections import defaultdict
from http import HTTPStatus
from operator import attrgetter

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET
from django.views.generic import FormView
from natsort import natsorted

from . import generator
from .forms import (
    PublicationReferentielPreparationForm,
    PublicationReferentielProductionForm,
    UploadFileForm,
)
from .ouvrages import Ouvrage


class Tableau(LoginRequiredMixin, FormView):
    form_class = UploadFileForm
    template_name = "tableau_upload.html"

    def form_valid(self, form):
        response = generator.post(
            settings.GENERATOR_SERVICE_HOST, files={"file": form.cleaned_data["file"]}
        )
        return _forward_http_file(response)


tableau = Tableau.as_view()


@login_required
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


class PublicationReferentiel(LoginRequiredMixin, FormView):
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


@login_required
def publication_display(request, generation_id):
    publication_url = _generate_publication_url(generation_id, "")
    response = generator.get(publication_url)

    if response.status_code == HTTPStatus.OK:
        return _forward_http_file(response)

    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return render(
            request,
            "publication_generation_failed.html",
            {"generation_id": generation_id, "logs": response.text},
        )

    return render(
        request,
        "generating_page.html",
        {"displayable_step": response.text},
    )


@login_required
@require_GET
def ouvrages_by_name(request):
    ouvrages_from_generator = generator.get(
        f"{settings.GENERATOR_SERVICE_HOST}/publication/from_production/list"
    ).json()

    ouvrages = [
        ouvrage_item
        for ouvrage, files in ouvrages_from_generator.items()
        if (ouvrage_item := Ouvrage.from_json(ouvrage, files))
    ]
    return render(
        request,
        "ouvrages_by_name.html",
        {
            "ouvrages": sorted(ouvrages, key=attrgetter("name")),
        },
    )


class OuvragesByDate(LoginRequiredMixin, FormView):
    template_name = "ouvrages_by_date.html"
    form_class = PublicationReferentielProductionForm

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

        ouvrage_objects = [
            ouvrage_item
            for ouvrage, files in ouvrages_from_generator.items()
            if (ouvrage_item := Ouvrage.from_json(ouvrage, files))
        ]

        ouvrages = defaultdict(list)
        for ouvrage in ouvrage_objects:
            ouvrages[ouvrage.date].append(ouvrage)
            ouvrages[ouvrage.date] = natsorted(
                ouvrages[ouvrage.date], key=attrgetter("name")
            )
        ouvrages_by_date = dict(sorted(ouvrages.items(), reverse=True))
        kwargs["ouvrages_by_date"] = {
            f"Ouvrages générés le {key.strftime('%d/%m/%Y')}": value
            for key, value in ouvrages_by_date.items()
        }
        return super().get_context_data(**kwargs)


ouvrages_by_date = OuvragesByDate.as_view()


def _forward_http_file(response):
    http_response = FileResponse(response)
    headers_to_forward = ["Content-Type", "Content-Length", "Content-Disposition"]
    for header in headers_to_forward:
        http_response.headers[header] = response.headers[header]
    return http_response


def _generate_publication_url(generation_id, suffix):
    return f"{settings.GENERATOR_SERVICE_HOST}/publication/{generation_id}/{suffix}"
