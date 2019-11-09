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
    department = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    graduation_year = models.CharField(max_length=20)
    position = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    office_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)
