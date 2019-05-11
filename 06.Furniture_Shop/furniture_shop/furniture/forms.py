from django import forms
from django.core.validators import MinValueValidator

from .models import Furniture, Maretial


form_control = {'class': 'form-control'}


def text_input_widget():
    return forms.TextInput(attrs=form_control)


class CreateFurnitureForm(forms.ModelForm):
    make = forms.CharField(required=True, widget=text_input_widget())
    model = forms.CharField(required=True, widget=text_input_widget())
    description = forms.CharField(required=True, widget=forms.Textarea(
        attrs=form_control
    ))
    price = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(10)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'number'
            }
        )
    )
    image_url = forms.URLField(required=True, widget=text_input_widget())
    material = forms.ModelChoiceField(
        required=False,
        queryset=Maretial.objects.all(),
        widget=forms.Select(attrs=form_control)
    )

    class Meta:
        model = Furniture
        fields = ('id', 'make', 'model', 'description', 'price', 'image_url',
                  'material')
