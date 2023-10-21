from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    AbstractBaseUser,
)
from .managers import AccountManager
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class AccountUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = AccountManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self, *args, **kwargs):
        return reverse("accounts:user_detail", args=[self.pk])


class Profile(models.Model):
    user = models.OneToOneField(
        AccountUser, on_delete=models.CASCADE, related_name="user_profile"
    )
    avatar = models.ImageField(upload_to="profile/avatar/", blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    full_name = models.CharField(max_length=300, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

    @property
    def username(self):
        if self.full_name is not None:
            return f"{self.full_name.split(' ')[0]}".title()
        else:
            return f"{self.user.email[:self.user.email.index('@')]}".title()

    def __str__(self):
        return f"{self.user.email}" or f"{self.full_name}"

    def save(self, *args, **kwargs):
        return super(Profile, self).save(*args, **kwargs)


@receiver(post_save, sender=AccountUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        Profile.objects.get(user=instance).save()
