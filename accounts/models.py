from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    
@receiver(post_save, sender=User)
def create_user_profile (sender, instance, created, **kwargs):
    if created:      
        Profile.objects.get_or_create(user = instance)

class Team(models.Model):
    name = models.CharField(max_length=100)
    foundation = models.DateField()
    leader = models.ForeignKey(User,null=True, blank=True,related_name="led_teams", on_delete=models.SET_NULL)
    members = models.ManyToManyField(User, related_name="teams")

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    team = models.ForeignKey(Team, related_name="projects", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    