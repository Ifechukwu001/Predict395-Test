from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import signup_view, login_view, logout_view
from .forms import SignupForm, AuthenticationForm


class AccountViewTestCase(SimpleTestCase):
    def test_signup_url(self):
        url = reverse("accounts:signup")
        self.assertEqual(resolve(url).func.__name__, signup_view.__name__)

    def test_login_url(self):
        url = reverse("accounts:login")
        self.assertEqual(resolve(url).func.__name__, login_view.__name__)

    def test_logout_url(self):
        url = reverse("accounts:logout")
        self.assertEqual(resolve(url).func.__name__, logout_view.__name__)

    def test_signup_template(self):
        response = self.client.get(reverse("accounts:signup"))
        self.assertTemplateUsed(response, "accounts/signup.html")

    def test_login_template(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertTemplateUsed(response, "accounts/login.html")


class AccountFormTestCase(TestCase):
    def test_signup_form(self):
        form = SignupForm(
            data={
                "username": "testuser",
                "password1": "testpassword",
                "password2": "testpassword",
            }
        )
        self.assertTrue(form.is_valid())

    def test_signup_form_no_data(self):
        form = SignupForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_login_form(self):
        form = SignupForm(
            data={
                "username": "testuser",
                "password1": "testpassword",
                "password2": "testpassword",
            }
        )
        form.save()
        form = AuthenticationForm(
            data={"username": "testuser", "password": "testpassword"}
        )
        self.assertTrue(form.is_valid())

    def test_login_form_no_data(self):
        form = AuthenticationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
