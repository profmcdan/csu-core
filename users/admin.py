from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'created_on', 'modified_on', 'first_name', 'last_name', 'email', 'is_staff',
    )


admin.site.register(User, UserAdmin)
