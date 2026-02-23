from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number =  PhoneNumberField(null=False, blank=False, unique=True)
    bio = models.TextField(blank=True)

    class Level(models.TextChoices) :
        JUNIOR = "Junior", "Junior"
        MID = "Mid-level", "Mid-level"
        SENIOR = "Senior", "Senior"

    level = models.CharField(max_length=10, choices=Level.choices)


    def __str__(self):
        return self.user.username
    
