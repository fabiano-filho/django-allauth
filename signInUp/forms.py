from allauth.account.forms import LoginForm
from django import forms

class LoginForm_(LoginForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm_, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(
            attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
            })
        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline'
            })