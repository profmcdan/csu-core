from django.db import models

# Create your models here.


class Profile(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    modified_on = models.DateTimeField(
        auto_now=True,
    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    department = models.CharField(max_length=255, null=True)
    faculty = models.CharField(max_length=255, null=True)
    graduation_year = models.CharField(max_length=20, null=True)
    position = models.CharField(max_length=255, null=True)
    profession = models.CharField(max_length=255, null=True)
    office_address = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    bio = models.TextField(null=True)
    birthdate = models.CharField(max_length=255, null=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    linkein = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)
