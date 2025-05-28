"""
A model is the single, definitive source of information about
your data. It contains the essential fields and behaviors of the
data you're storing. Generally, each model maps to a single database
table.
"""

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


from core.utils.validators import validate_email
from modules.users.user_manager import CustomUserManager




class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Responsável por armazenar os dados de usuários,
    sendo uma customização da classe User implementada pelo Django.
    """
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    username: models.CharField = models.CharField(
        verbose_name=_('Username'),
        max_length=60,
        unique=True,
    )
    email = models.EmailField(
    verbose_name=_('Email address'),
    unique=True,
    validators=[validate_email],
    null=True,
    blank=True,
    )
    is_admin: models.BooleanField = models.BooleanField(
        verbose_name=_('Admin Status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into the admin site.'
        ),
    )
    date_joined: models.DateTimeField = models.DateTimeField(
        verbose_name=_('Join Date'),
        auto_now_add=True,
    )
    is_notified: models.BooleanField = models.BooleanField(
        verbose_name=_('Is Notified'),
        default=False,
    )
    is_active: models.BooleanField = models.BooleanField(
        verbose_name=_('Active'),
        default=True,
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  
        verbose_name=_('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions', 
        blank=True,
        verbose_name=_('user permissions'),
    )


    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    class Meta:  # pylint: disable=missing-class-docstring
        ordering = ['-id']
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self) -> str:
        return f'{self.username}'  

    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin



