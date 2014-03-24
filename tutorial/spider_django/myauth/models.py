# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

import models_setting as config

MAX_LENGTH = config.MAX_LENGTH_100


class UserManager(BaseUserManager):

    def create_user(self, name, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None):

        user = self.create_user(name, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    '''用户表'''

    name = models.CharField(max_length=MAX_LENGTH, unique=True)
    email = models.EmailField(max_length=MAX_LENGTH, unique=True)
    avatar = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    access_token = models.CharField(max_length=MAX_LENGTH, blank=True)
    refresh_token = models.CharField(max_length=MAX_LENGTH, blank=True)
    expires_in = models.BigIntegerField(max_length=MAX_LENGTH, default=0)

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ('email',)

    class Meta:
        ordering = ('-created_at',)

    def __unicode__(self):
        return self.name

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
