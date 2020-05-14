from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUser(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class':"input"})
        )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'input'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'input'})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'input'})
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
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegisterUser, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

    #  TODO edit form style and handle error input on user registration (ex: wrong password input)