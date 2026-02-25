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

class Task(models.Model):
    title = models.CharField(max_length=100)
    
    class Status(models.TextChoices):
        DONE = "Done", "Done"
        IN_PROGRESS = "In progress", "In progress"
        TO_DO = "To do", "To do"
    status = models.CharField(max_length=20, default=Status.TO_DO, choices=Status.choices)

    project = models.ForeignKey(Project, related_name="tasks",null=True, on_delete=models.SET_NULL) 
    parent_task = models.ForeignKey("self",null=True, blank=True,related_name="subtasks", on_delete=models.SET_NULL ) 

    assigned_users = models.ManyToManyField(User,
        through='Assignment',
        through_fields=('task', 'user'),
        related_name="tasks_assigned")

    def __str__(self):
        return self.title
    
class Assignment(models.Model):
    task = models.ForeignKey(Task, null=False , on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, related_name="assignments_received", on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(User, null=True ,related_name="assignments_given", on_delete=models.SET_NULL)
    assigned_date = models.DateTimeField() 


class TimeLog(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="time_logs") 
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date_logged  = models.DateTimeField(auto_now_add=True)
    hours = models.FloatField()
   
    def __str__(self):
        if self.user:
            return f"{self.user.username} - {self.task.title} - {self.hours}h"
        return f"Deleted user - {self.task.title} - {self.hours}h"