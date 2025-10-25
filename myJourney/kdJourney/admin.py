from django.contrib import admin
from .models import Profile, LearningEntry

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'skills', 'email')   # shows in admin list view
    fields = ('name', 'bio', 'skills', 'email', 'image')  # shows in the edit form

admin.site.register(Profile, ProfileAdmin)
admin.site.register(LearningEntry)
