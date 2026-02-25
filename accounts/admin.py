from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile,Team,Project,Task,Assignment

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


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title","team")
    search_fields = ('title', 'team__name')
    list_filter = ('team',) 

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'project', 'parent_task')
    list_filter = ('status', 'project')
    search_fields = ('title',)

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'assigned_by', 'assigned_date')
    list_filter = ('assigned_date',)
    search_fields = ('task__title', 'user__username', 'assigned_by__username')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Assignment, AssignmentAdmin)