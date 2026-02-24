from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile,Team

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone_number", "level"]
    list_filter = ["level"]
    search_fields = ["user__username", "phone_number"]


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'foundation', 'leader')
    search_fields = ('name', 'leader__username')
    list_filter = ('foundation',)
    filter_horizontal = ('members',) 


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Team, TeamAdmin)