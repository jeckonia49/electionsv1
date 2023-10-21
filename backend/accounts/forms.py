from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import AccountUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = AccountUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = AccountUser
        fields = ("email",)


class UserLoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email address"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control fakepassword",
                "placeholder": "Enter your password...",
            }
        )
    )


class UserForgetPasswordForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter the email address for the account",
            }
        )
    )


class UserRegisterForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email address"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control fakepassword",
                "placeholder": "Enter your password...",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "confirm password",
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password1 = cleaned_data.get("password1")
        if len(password) < 8:
            raise forms.ValidationError("Password cannot be less than 8 character")
        if password != password1:
            raise ValueError("Password Did not match")
        return cleaned_data
