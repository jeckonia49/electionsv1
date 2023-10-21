from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import AccountUser, Profile


@admin.register(AccountUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = AccountUser
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    actions = ("_make_staff", "_unmake_staff")

    @admin.action(description="Make Staff")
    def _make_staff(self, request, queryset):
        return queryset.update(is_staff=True)

    @admin.action(description="Remove Staff")
    def _unmake_staff(self, request, queryset):
        return queryset.update(is_staff=False)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone", "full_name", "username", "is_public"]
    actions = ("_make_public",)

    @admin.action(description="Make Profile Public")
    def _make_public(self, request, queryset):
        return queryset.update(is_public=True)
