from django.contrib.auth.forms import UserCreationForm

from .models import User

class SignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
