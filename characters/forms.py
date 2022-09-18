from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "--не выбрано--"


    class Meta:
        model = Character
        fields = [
            'title', 'about', 'photo', 'slug', 'is_published', 'abil1',
            'skil1', 'photo_skill_1', 'abil2', 'skil2', 'photo_skill_2', 'abil3', 'skil3', 'photo_skill_3',
            'abil4', 'skil4', 'photo_skill_4', 'abil5', 'skil5', 'photo_skill_5',
             'abil6', 'skil6', 'photo_skill_6', 'abil7', 'skil7', 'photo_skill_7',
            'abil8', 'skil8', 'photo_skill_8', 'abil9', 'skil9', 'photo_skill_9',
            'abil10', 'skil10', 'photo_skill_10', 'abil11', 'skil11', 'photo_skill_11', 'cat',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
        }

        for i in fields:
            if i[:4] == 'skil' or i == 'about':
                widgets[i] = forms.Textarea(attrs={'cols': 39, 'rows': 5})

    def clean_title(self):
        """Пользовательский валидатор поля"""
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError("Длина превышает 200 символов")

        return title

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Имя",
        max_length=255,
        widget=forms.TextInput(
            attrs={'placeholder': 'Введите ваше имя'}
        )
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(
            attrs={'placeholder': 'Введите Email'}
        )
    )
    content = forms.CharField(
        label="Введите текст",
        widget=forms.Textarea(attrs={'cols': 39, 'rows': 5, 'placeholder': 'Сообщение'}))

    captcha = CaptchaField(label="Капча")