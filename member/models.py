from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    class MemberRole(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        EMPLOYEE = 'employee', 'Employee'

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=MemberRole.choices, default=MemberRole.EMPLOYEE)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []