from django import forms
from django.forms import ValidationError


def test_vali(val):
    if not val.startswith("A"):
        raise ValidationError("Name should start with A.")


class TestForm(forms.Form):
    name = forms.CharField(help_text="Name should start with A.", label="Name 1", max_length=5,
                           validators=[test_vali])
    age = forms.IntegerField()
