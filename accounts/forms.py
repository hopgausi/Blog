from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile


class UserRegistrationForm(UserCreationForm, ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username','password1', 'password2']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username']