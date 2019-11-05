# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

    modified_on = models.DateTimeField(
        auto_now=True,
        null=True,
    )

    deactivated = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Deactivated',
        help_text='Designates whether this user should be treated as deactivated',
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Last Name',
    )

    email = models.EmailField(
        unique=True,
        max_length=50,
        verbose_name='Email',
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name='Is Staff',
        help_text='Designates whether the user can log into Django admin site',
    )

    password_reset_token = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Password Reset Token',
    )

    invitation_token = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Invitation Token'
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        get_latest_by = 'date_joined'

    def __str__(self):
        return self.email
