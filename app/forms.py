from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # Form is based on Question model
        fields = ['title', 'body']  # Fields to be included in the form
        labels = {'title': 'Write Your Question here!'}  # Custom label for the title field
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # Bootstrap styling for title input
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),  # Text area for body with styling
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['body'].required = False  # Make body optional


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer  # Form is based on Answer model
        fields = ['body']  # Only body field required to submit an answer
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Bootstrap styling for answer box
        }


class UserRegisterForm(UserCreationForm):  # Inherits built-in form for user registration
    class Meta:
        model = User  # User model for registration
        fields = ['username', 'password1', 'password2']  # Fields required for registration
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),  # Styling input fields
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
