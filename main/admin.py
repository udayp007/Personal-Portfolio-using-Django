
from django.contrib import admin
from .models import Profile, Project, Skill, ContactMessage

admin.site.register(Profile)
admin.site.register(Project)

@admin.register(Skill)  # ✅ Keep this registration
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')


