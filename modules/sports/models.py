from django.db import models
from core.utils.choices import LEVEL_CHOICES
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

class FavoriteSport(AbstractBaseModel):
    user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        db_column='user_id',
    )
    sport = models.ForeignKey(
        'Sports',
        on_delete=models.CASCADE,
        db_column='sport_id',
    )
    level = models.CharField(
        max_length=12,
        choices=LEVEL_CHOICES,
        default='BEGINNER',
    )
    

    class Meta:
        db_table = 'favorite_sports'
        unique_together = ('user', 'sport')

    def __str__(self):
        return f'{self.user} - {self.sport} ({self.level})'