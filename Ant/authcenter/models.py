#!/usr/bin/evn python
# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class PermissionList(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)

    def __str__(self):
        return '%s(%s)' % (self.name, self.url)

class RoleList(models.Model):
    name = models.CharField(max_length=64)
    permission = models.ManyToManyField(PermissionList, blank=True)

    def __str__(self):
        return self.name

class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class UserInfo(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    # username = models.CharField(max_length=64)
    name = models.CharField(max_length=64, unique=True)
    token = models.CharField(u'token', max_length=128,default=None,blank=True,null=True)
    password = models.CharField(max_length=128)
    department = models.CharField(u'部门', max_length=32,default=None,blank=True,null=True)
    tel = models.CharField(u'座机', max_length=32,default=None,blank=True,null=True)
    mobile = models.CharField(u'手机', max_length=32,default=None,blank=True,null=True)

    is_superuser = models.BooleanField(default=False)
    nickname = models.CharField(max_length=64, null=True)
    role = models.ForeignKey(RoleList, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return  self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = u"用户信息"
    def __str__(self):
        return self.email

    objects = UserProfileManager()