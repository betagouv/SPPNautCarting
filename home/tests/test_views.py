"""
Test default view of sppnaut application
"""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class UserViewTests(TestCase):
    """
    class to test the views before and after login including the failed login
    """

    @classmethod
    def setUpTestData(cls):
        # pylint: disable=R0914
        User.objects.create_user("coralie", "coralie@sppnaut.com", "12345")

    def test_no_login(self):
        """
        If not login, the request is not redirected and buton to login are displayed
        """
        self.assertEqual("/", reverse("users:index"))
        response = self.client.get(reverse("users:index"))

        #        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Vous n'êtes pas loggé")
        self.assertContains(response, "S'identifier")
        self.assertNotContains(response, "Se déconnecter")

        response = self.client.post(
            reverse("login"),
            {"username": "coralie", "password": "faux mot de passe"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        self.assertContains(
            response,
            "Votre identifiant / email et votre mot de passe de correspondent pas.",
        )
        response = self.client.post(
            reverse("login"), {"username": "coralie", "password": "12345"}
        )
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("home:index"))
        self.assertRedirects(response, reverse("home:main"))

        response = self.client.get(reverse("home:main"))
        self.assertContains(response, "Se déconnecter")
        self.assertContains(response, "Vous êtes loggé")
        self.assertNotContains(response, "S'identifier")
