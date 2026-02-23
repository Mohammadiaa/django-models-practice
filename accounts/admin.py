from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone_number", "level"]
    list_filter = ["level"]
    search_fields = ["user__username", "phone_number"]

admin.site.register(Profile, ProfileAdmin)
