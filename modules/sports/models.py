from django.db import models
from core.utils.models import AbstractBaseModel

class Sports(AbstractBaseModel):
    name = models.CharField(
        max_length=100,
        verbose_name='Sport Name',
        help_text='Name of the sport',
    )
    last_user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.SET_NULL,
        related_name='last_sport',
        verbose_name='Last User',
        help_text='User who last modified this sport',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Sport'
        verbose_name_plural = 'Sports'

    def __str__(self) -> str:
        return self.name
