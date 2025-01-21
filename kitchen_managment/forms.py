from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from .models import Dish, Cook
from django.core.validators import MaxValueValidator, MinValueValidator


class CookCreationForm(UserCreationForm):
    years_of_experience = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience",
                                                 "email")


class CookExperienceUpdateForm(forms.ModelForm):
    years_of_experience = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = ("years_of_experience",)


class CookUsernameSearchForm(forms.Form):
    username = forms.CharField(max_length=150,
                               required=False,
                               label="",
                               widget=forms.TextInput(
                                   attrs={"placeholder": "Search by username"}
                               )
                               )


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishNameSearchForm(forms.Form):
    name = forms.CharField(max_length=255,
                           required=False,
                           label="",
                           widget=forms.TextInput(
                               attrs={"placeholder": "Search by name"}
                               )
                           )


class DishTypeNameSearchForm(forms.Form):
    name = forms.CharField(max_length=255,
                           required=False,
                           label="",
                           widget=forms.TextInput(
                               attrs={"placeholder": "Search by name"}
                            )
                           )
