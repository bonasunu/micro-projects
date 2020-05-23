from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUser(UserCreationForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input'})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input'})
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input'})
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class':'input'})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'input'})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'input'})
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegisterUser, self).save(commit=False)
        
        if commit:
            user.save()

        return user