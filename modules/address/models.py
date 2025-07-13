from django.db import models
from django.utils.translation import gettext_lazy as _

from core.utils.models import AbstractBaseModel





class Country(AbstractBaseModel):
    """
    Responsável por armazenar os dados de países.
    """

    name: models.CharField = models.CharField(
        verbose_name=_('Country Name'),
        max_length=30,
    )
    abbreviation: models.CharField = models.CharField(
        verbose_name=_('Abbreviation'),
        max_length=3,
    )
    last_user: models.ForeignKey = models.ForeignKey(
        to='users.CustomUser',
        on_delete=models.RESTRICT,
        verbose_name=_('Last User'),
        related_name='country_customuser_lastuser',
    )

    class Meta:  # pylint: disable=missing-class-docstring
        ordering = ['-id']
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        indexes = [
            models.Index(fields=['name'], name='idx_name_country'),
        ]

    def __str__(self) -> str:
        return f'{self.name} - {self.abbreviation}'


class FederativeUnit(AbstractBaseModel):
    """
    Responsável por armazenar os dados de unidades federativas.
    """

    name: models.CharField = models.CharField(
        verbose_name=_('Federative Unit Name'),
        max_length=30,
    )
    abbreviation: models.CharField = models.CharField(
        verbose_name=_('Abbreviation'),
        max_length=2,
    )
    country: models.ForeignKey = models.ForeignKey(
        to='address.Country',
        on_delete=models.RESTRICT,
        verbose_name=_('Country'),
        related_name='federativeunit_country_country',
    )
    last_user: models.ForeignKey = models.ForeignKey(
        to='users.CustomUser',
        on_delete=models.RESTRICT,
        verbose_name=_('Last User'),
        related_name='federativeunit_customuser_lastuser',
    )

    class Meta:  # pylint: disable=missing-class-docstring
        ordering = ['-id']
        verbose_name = _('Federative Unit')
        verbose_name_plural = _('Federative Units')
        indexes = [
            models.Index(fields=['name'], name='idx_name_federative_unit'),
        ]

    def __str__(self) -> str:
        return f'{self.name} - {self.country.abbreviation}'  


class City(AbstractBaseModel):
    """
    Responsável por armazenar os dados de cidades.
    """

    name: models.CharField = models.CharField(
        verbose_name=_('City Name'),
        max_length=30,
    )
    federative_unit: models.ForeignKey = models.ForeignKey(
        to='address.FederativeUnit',
        on_delete=models.RESTRICT,
        verbose_name=_('Federative Unit'),
        related_name='city_federativeunit_federativeunit',
    )
    last_user: models.ForeignKey = models.ForeignKey(
        to='users.CustomUser',
        on_delete=models.RESTRICT,
        verbose_name=_('Last User'),
        related_name='city_customuser_lastuser',
    )

    class Meta:  # pylint: disable=missing-class-docstring
        ordering = ['-id']
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        indexes = [
            models.Index(fields=['name'], name='idx_name_city'),
        ]

    def __str__(self) -> str:
        return f'{self.name} - {self.federative_unit.abbreviation} - {self.federative_unit.country.abbreviation}'  

