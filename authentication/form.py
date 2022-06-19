from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')


        # try:
        #     self.user = User.objects.get(username=username)
        # except User.DoesNotExist:
        #     raise forms.ValidationError(f'The user with username {username} does not exist')
