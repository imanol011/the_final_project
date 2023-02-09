from django.contrib import admin
from users.models import UserProfile

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ('phone', 'birth_date')