

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class FormRegistrationUser(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=['cin','first_name','last_name','username',
                'email','password1','password2']
    def save(self, commit=True):
        user = super(FormRegistrationUser,self).save(commit)
        return user
        