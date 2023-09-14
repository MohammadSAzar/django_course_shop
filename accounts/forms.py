from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomCreationUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomChangeUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)



