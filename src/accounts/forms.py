from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    BaseUserCreationForm,
)
from django import forms


class SignupForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"autofocus": True}),
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    def _post_clean(self):
        super(BaseUserCreationForm, self)._post_clean()
