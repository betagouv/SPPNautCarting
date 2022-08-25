import requests

from functools import partial
from django.conf import settings

get=partial(requests.get, auth=(settings.GENERATOR_USERNAME, settings.GENERATOR_PASSWORD))

post=partial(requests.post, auth=(settings.GENERATOR_USERNAME, settings.GENERATOR_PASSWORD))

# def get(*args, **kwargs):
#     response = requests.get(
#         *args,
#         **kwargs,
#         auth=(settings.GENERATOR_USERNAME, settings.GENERATOR_PASSWORD),
#     )
#     return response

# def post(*args, **kwargs):
#     response = requests.post(
#         *args,
#         **kwargs,
#         auth=(settings.GENERATOR_USERNAME, settings.GENERATOR_PASSWORD),
#     )
#     return response
