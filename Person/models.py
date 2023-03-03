from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.
# def length_cin(value):
#     if len(value)!=8:
#         raise ValidationError("Your CIN must have 8 characters!")
#     return value
def is_email_esprit(mail):
    if str(mail).endswith("@esprit.tn")== False:
        raise ValidationError(
            "Your email {m} must ends with @€sprit.tn",
            params={'m':mail})
    return mail
        
class Person(AbstractUser):
    cin=models.IntegerField(primary_key=True,validators=[])
        #MaxLengthValidator(8),MinLengthValidator(8)])
    email=models.EmailField(unique=True,validators=[is_email_esprit])
