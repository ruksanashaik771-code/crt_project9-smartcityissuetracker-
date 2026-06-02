from django import forms
from .models import Issue
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue

        fields = [
            'title',
            'category',
            'description',
            'location',
            'image'
        ]

        widgets = {
            'description': forms.Textarea(
                attrs={'rows': 4}
            )
        }