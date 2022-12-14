from django import forms
from turnstile.fields import TurnstileField as CaptchaField
from django.core.exceptions import ValidationError
from .models import *


class FileForm(forms.Form):
    file = forms.FileField(
        label="file",
        allow_empty_file=False,
        widget=forms.FileInput(
            attrs={
                "class": "hidden",
            }
        ),
    )

    captcha = CaptchaField(theme="dark")

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = ""
        self.user = user

    def clean(self):
        captcha_error = self.errors.get("captcha")
        if captcha_error:
            raise ValidationError(captcha_error)
        self.url = save_file(self.user, self.get_file())
        return self.cleaned_data

    def get_file(self):
        return self.cleaned_data.get("file")

    def get_link(self):
        return self.url

    def get_error(self):
        try:
            return self.errors.get("__all__")[0]
        except TypeError:
            return "File / Captcha is required."
