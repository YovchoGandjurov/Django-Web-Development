from django import forms
from .models import Animal
from django.core.validators import RegexValidator, URLValidator, \
                                   MinValueValidator


class AnimalForm(forms.ModelForm):
    name_error = "Animal's name must starts with capital letter followed by letters \
                  from a-z"
    age_error = "Animal's age must be positive number."
    breed_error = "Animal's breed must starts with capital letter."

    choices = list(Animal.KIND_CHOICES)

    name = forms.CharField(
        required=True,
        validators=[RegexValidator(r'^[A-Z][a-z]+$', message=name_error)],
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    age = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(0, message=age_error)],
        widget=forms.NumberInput(attrs={'class': 'form-control'}))

    breed = forms.CharField(
        required=True,
        validators=[RegexValidator(r'^[A-Z].*', message=breed_error)],
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control'}))

    image_url = forms.URLField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    kind = forms.ChoiceField(
        choices=choices,
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Animal
        fields = 'name age breed description image_url kind'.split()
