from django.db import models
from django.core.validators import MinLengthValidator
from .validators import check_valid_username

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=15, validators=[check_valid_username, MinLengthValidator(2)])
    email = models.EmailField()
    age = models.PositiveIntegerField(blank=True, null=True)
