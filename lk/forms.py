from .models import User
from django import forms
from django.contrib.auth.forms import  UserCreationForm

class AddEmployerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'user_type', 'user_boss', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(AddEmployerForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['username'].widget.attrs['class'] = 'form-control'        
        self.fields['first_name'].label = 'Имя'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = 'e-mail'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['user_type'].label = 'Должность'
        self.fields['user_type'].widget.attrs['class'] = 'form-control'
        self.fields['user_boss'].label = 'Начальник'
        self.fields['user_boss'].widget.attrs['class'] = 'form-control'        
        self.fields['password1'].label = 'Пароль'
        self.fields['password1'].widget.attrs['class'] = 'register-input'
        self.fields['password2'].label = 'Подтверждение пароля'
        self.fields['password2'].widget.attrs['class'] = 'register-input'
        self.error_messages['duplicate_username']='Такой логин уже существует'
        
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])