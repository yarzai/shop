from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ['id', 'email', 'image', 'date_of_birth']
    ordering = ['email']
    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        ("Personal info", {"fields": ('name', 'image')}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {
         "fields": ('date_of_birth', "last_login")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    list_display_links = ['id', 'email']


admin.site.register(Account, AccountAdmin)
