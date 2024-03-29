from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    contact_picture = models.URLField(null=True)
    is_favourite = models.BooleanField(default=False)