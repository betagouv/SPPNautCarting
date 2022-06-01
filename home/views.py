"""
Views for home module
"""
import requests
from django.conf import settings
from django.http import FileResponse
from django.views.generic import FormView

from home.forms import UploadFileForm


class Index(FormView):
    form_class = UploadFileForm
    template_name = "index.html"

    def form_valid(self, form):
        response = requests.post(
            settings.GENERATOR_SERVICE_HOST, files={"file": form.cleaned_data["file"]}
        )

        http_response = FileResponse(response)
        headers_to_forward = ["Content-Type", "Content-Length", "Content-Disposition"]
        for header in headers_to_forward:
            http_response.headers[header] = response.headers[header]

        return http_response


index = Index.as_view()
