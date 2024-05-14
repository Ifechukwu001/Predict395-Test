from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    BaseUserCreationForm,
)
from django import forms


class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    def _post_clean(self):
        super(BaseUserCreationForm, self)._post_clean()
