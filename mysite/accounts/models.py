from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Accounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/')
    address=models.CharField(max_length=200 )
    line1=models.CharField(max_length=300)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50,)
    pincode=models.IntegerField(null=True)
    def __str__(self):
        return self(self.user)