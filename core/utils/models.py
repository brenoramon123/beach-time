from django.db import models
from django.utils.translation import gettext_lazy as _

from core.utils import resolve
from core.utils.choices import (
    COMPOSITION_CHOICES,
    CONTRACT_TYPES_CHOICES,
    DAYS_WEEK_CHOICES,
    PHOTO_STATUS_CHOICES,
    PHOTOGRAPHIC_REGISTER_STATUS_CHOICES,
    TYPE_FRANCHISE_CHOICES,
    UNIT_CHOICES,
    UNIT_CONSIDER_CALC_CHOICES,
)


class AbstractBaseModel(models.Model):
    """
    Responsável por definir os campos padrões de todos os models
    do projeto.
    """

    registration: models.DateTimeField = models.DateTimeField(
        verbose_name=_('Registration Date'),
        auto_now_add=True,
    )
    last_modification: models.DateTimeField = models.DateTimeField(
        verbose_name=_('Modification Date'),
        auto_now=True,
    )
    is_active: models.BooleanField = models.BooleanField(
        verbose_name=_('Active'),
        default=True,
    )

    class Meta:
        abstract = True


class AbstractService(AbstractBaseModel):
    """
    Responsável por definir os campos padrões de todos os models
    de serviços do projeto.
    """

    name: models.CharField = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
    )

    class Meta:  # pylint: disable=missing-class-docstring
        abstract = True


class AbstractCompany(AbstractBaseModel):
    """
    Responsável por definir os campos padrões de todos os models
    de empresas do projeto.
    """

    cnpj: models.CharField = models.CharField(
        verbose_name=_('CNPJ'),
        max_length=14,
    )
    state_registration: models.CharField = models.CharField(
        verbose_name=_('State Registration'),
        max_length=14,
    )
    city_registration: models.CharField = models.CharField(
        verbose_name=_('City Registration'),
        max_length=11,
        null=True,
        blank=True,
    )
    trade_name: models.CharField = models.CharField(
        verbose_name=_('Trade Name'),
        max_length=100,
    )
    legal_name: models.CharField = models.CharField(
        verbose_name=_('Legal Name'),
        max_length=100,
    )
    fiscal_cnae: models.CharField = models.CharField(
        verbose_name=_('Fiscal CNAE'),
        max_length=7,
    )
    main_activity: models.CharField = models.CharField(
        verbose_name=_('Main Activity'),
        max_length=50,
    )
    establishment_date: models.DateField = models.DateField(
        verbose_name=_('Establishment Date'),
    )
    landline_phone: models.CharField = models.CharField(
        verbose_name=_('Landline Phone'),
        max_length=14,
    )
    cellphone: models.CharField = models.CharField(
        verbose_name=_('Cellphone'),
        max_length=14,
        null=True,
        blank=True,
    )
    email: models.EmailField = models.EmailField(
        verbose_name=_('Email'),
        null=True,
        blank=True,
    )
    name_of_responsible: models.CharField = models.CharField(
        verbose_name=_('Name of Responsible'),
        max_length=100,
    )
    cpf_of_responsible: models.CharField = models.CharField(
        verbose_name=_('CPF of Responsible'),
        max_length=11,
    )

    class Meta:  # pylint: disable=missing-class-docstring
        abstract = True


class AbstractModel(AbstractBaseModel):
    """
    Responsável por definir os campos padrões de todos os modelos
    referentes as marcas dos produtos.
    """

    name: models.CharField = models.CharField(
        verbose_name=_('Name'),
        max_length=25,
    )

    class Meta:  # pylint: disable=missing-class-docstring
        abstract = True


class AbstractBrand(AbstractBaseModel):
    """
    Responsável por definir os campos padrões de todos os modelos
    de marcas dos produtos.
    """

    name: models.CharField = models.CharField(
        verbose_name=_('Name'),
        max_length=25,
    )

    class Meta:  # pylint: disable=missing-class-docstring
        abstract = True


class DaysWeek(AbstractBaseModel):
    """
    Responsável por definir os campos padrões de todos os modelos
    de dias da semana.
    """

    name: models.CharField = models.CharField(
        verbose_name=_('Name'),
        choices=DAYS_WEEK_CHOICES,
        max_length=15,
    )

    class Meta:  # pylint: disable=missing-class-docstring
        ordering = ['-id']
        verbose_name = _('Day of the Week')
        verbose_name_plural = _('Days of the Week')

    def __str__(self) -> str:
        return str(self.name)


class AbstractPeriodDay(AbstractBaseModel):
    """
    Responsável por definir os campos padrões de todos os modelos
    de períodos do dia.
    """

    start_time: models.TimeField = models.TimeField(
        verbose_name=_('Start Time'),
    )
    end_time: models.TimeField = models.TimeField(
        verbose_name=_('End Time'),
    )

    class Meta:  # pylint: disable=missing-class-docstring
        abstract = True


class AbstractWasteReleases(AbstractBaseModel):
    """
    Model base responsável por armazenar os lançamentos de resíduos.
    """

    date: models.DateField = models.DateField(
        verbose_name=_('Date'),
        auto_now_add=True,
    )
    total_value: models.DecimalField = models.DecimalField(
        default=0,
        verbose_name=_('Total value'),
        max_digits=16,
        decimal_places=2,
    )
    addition: models.DecimalField = models.DecimalField(
        verbose_name=_('Addition'),
        help_text=_('Addition'),
        max_digits=15,
        decimal_places=2,
        default=0.00,
    )
    deduction: models.DecimalField = models.DecimalField(
        verbose_name=_('Deduction'),
        help_text=_('Deduction'),
        max_digits=15,
        decimal_places=2,
        default=0.00,
    )
    justification_increase_discount: models.TextField = models.TextField(
        verbose_name=_('Justification Increase Discount'),
        help_text=_('Justification Increase Discount'),
        default='',
    )
    observations: models.TextField = models.TextField(
        verbose_name=_('Observations'),
        blank=True,
        null=True,
    )

    class Meta:  # pylint: disable=missing-class-docstring
        abstract = True


class AbstractServiceRelease(AbstractBaseModel):
    """
    Model base responsável por armazenar os dados dos serviços ofertados nos
    contratos em resíduos urbanos.
    """

    quantity: models.DecimalField = models.DecimalField(
        verbose_name=_('Quantity'),
        max_digits=15,
        decimal_places=3,
    )
    unit_type: models.CharField = models.CharField(
        verbose_name=_('Unit Type'),
        choices=UNIT_CHOICES,
        max_length=3,
    )
    total_release_item: models.DecimalField = models.DecimalField(
        verbose_name=_('Total Release Item'),
        max_digits=15,
        decimal_places=2,
    )
    composition: models.CharField = models.CharField(
        verbose_name=_('Composition'),
        max_length=2,
        choices=COMPOSITION_CHOICES,
    )

    class Meta:  # pylint: disable=missing-class-docstring
        abstract = True


class AbstractContract(AbstractBaseModel):
    """
    Model responsável por armazenar os dados dos contratos.
    """

    contract_type: models.CharField = models.CharField(
        verbose_name=_('Contract Type'),
        max_length=3,
        choices=CONTRACT_TYPES_CHOICES,
    )
    num_contract: models.CharField = models.CharField(
        verbose_name=_('Contract Number'),
        max_length=15,
    )
    internal_num_contract: models.CharField = models.CharField(
        verbose_name=_('Internal Contract Number'),
        max_length=50,
        default=""
    )
    billing_day = models.IntegerField(
        verbose_name=_('Billing Day'),
        default=0,
    )
    due_day = models.IntegerField(
        verbose_name=_('Due Day'),
        default=0,
    )
    initial_date: models.DateField = models.DateField(
        verbose_name=_('Initial Date'),
    )
    final_date: models.DateField = models.DateField(
        verbose_name=_('Final Date'),
    )
    contract_inspector: models.CharField = models.CharField(
        verbose_name=_('Contract Inspector'),
        max_length=60,
    )
    cpf_contract_inspector: models.CharField = models.CharField(
        verbose_name=_('Contract Inspector CPF'),
        max_length=11,
    )
    observations: models.TextField = models.TextField(
        verbose_name=_('Observations'),
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class AbstractServiceContract(AbstractBaseModel):
    """
    Model responsável por armazenar os dados dos contratos de serviço.
    """

    type_franchise: models.CharField = models.CharField(
        verbose_name=_('Type Franchise'),
        max_length=3,
        choices=TYPE_FRANCHISE_CHOICES,
    )
    minimum_franchise_quantity: models.DecimalField = models.DecimalField(
        verbose_name=_('Minimum Franchise Quantity'),
        max_digits=15,
        decimal_places=3,
        default=0,
    )
    monthly_deductible: models.BooleanField = models.BooleanField(
        verbose_name=_('Monthly Deductible'),
        default=False,
    )
    monthly_deductible_quantity: models.DecimalField = models.DecimalField(
        verbose_name=_('Monthly Deductible Quantity'),
        max_digits=15,
        decimal_places=3,
        null=True,
        blank=True,
        default=0,
    )
    composition: models.CharField = models.CharField(
        verbose_name=_('Composition'),
        max_length=2,
        choices=COMPOSITION_CHOICES,
    )
    unit_consider_calc: models.CharField = models.CharField(
        verbose_name=_('Unit Consider Calculation'),
        max_length=2,
        choices=UNIT_CONSIDER_CALC_CHOICES,
    )
    unit_type: models.CharField = models.CharField(
        verbose_name=_('Unit'),
        choices=UNIT_CHOICES,
        max_length=3,
    )
    value_unit_contract: models.DecimalField = models.DecimalField(
        verbose_name=_('Value'),
        max_digits=15,
        decimal_places=6,
    )
    excess_value: models.DecimalField = models.DecimalField(
        verbose_name=_('Excess Value'),
        max_digits=15,
        decimal_places=2,
        default=0,
        null=True,
        blank=True,
    )
    contracted_quantity: models.DecimalField = models.DecimalField(
        verbose_name=_('Contracted Quantity'),
        max_digits=15,
        decimal_places=3,
    )
    quantity_used: models.DecimalField = models.DecimalField(
        verbose_name=_('Quantity Used'),
        max_digits=15,
        decimal_places=3,
        default=0,
    )
    balance_quantity: models.DecimalField = models.DecimalField(
        verbose_name=_('Balance Quantity'),
        max_digits=15,
        decimal_places=3,
        default=0,
    )
    num_components_team: models.IntegerField = models.IntegerField(
        verbose_name=_('Number of Components per Team'),
        default=0,
    )
    quantity_charge_unit: models.DecimalField = models.DecimalField(
        verbose_name=_('Quantity Charge Unit'),
        max_digits=15,
        decimal_places=2,
        default=0,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class AbstractPictureWaste(AbstractBaseModel):
    """
    Model responsável por armazenar as imagens de resíduos.
    """

    picture_path: models.ImageField = models.ImageField(
        verbose_name=_('Picture'),
        upload_to=resolve.file_saving_location,
        max_length=255,
    )
    place: models.TextField = models.TextField(
        verbose_name=_('Place'),
    )
    latitude: models.FloatField = models.FloatField(
        verbose_name=_('Latitude'),
        blank=True,
        null=True,
    )
    longitude: models.FloatField = models.FloatField(
        verbose_name=_('Longitude'),
        blank=True,
        null=True,
    )
    geolocation_description: models.TextField = models.TextField(
        verbose_name=_('Geolocation Description'),
        blank=True,
        null=True,
    )
    time_occurred: models.TimeField = models.TimeField(
        verbose_name=_('Time Occurred'),
    )
    time: models.TimeField = models.TimeField(
        verbose_name=_('Time'),
        auto_now_add=True,
    )
    status: models.CharField = models.CharField(
        verbose_name=_('Status'),
        max_length=3,
        choices=PHOTO_STATUS_CHOICES,
        default='APR',
    )
    justify_rejection: models.TextField = models.TextField(
        verbose_name=_('Justification Rejection'),
        blank=True,
    )

    class Meta:  # pylint: disable=missing-class-docstring
        abstract = True


class AbstractPhotographicRegister(AbstractBaseModel):
    """
    Model responsável por armazenar os registros fotográficos de lançamentos de resíduos.
    """

    description: models.TextField = models.TextField(
        verbose_name=_('Description'),
    )
    status: models.CharField = models.CharField(
        verbose_name=_('Status'),
        choices=PHOTOGRAPHIC_REGISTER_STATUS_CHOICES,
        max_length=3,
        default='PEN',
    )

    class Meta:  # pylint: disable=missing-class-docstring
        abstract = True


class AbstractDailyVehicleInspection(AbstractBaseModel):
    date: models.DateField = models.DateField(
        verbose_name=_('Date'),
        help_text=_('Date of Registration'),
        auto_now_add=True,
    )
    status: models.BooleanField = models.BooleanField(
        verbose_name=_('Status'),
        help_text=_('Status'),
        default=True,
    )
    observation: models.TextField = models.TextField(
        verbose_name=_('Observation'),
        help_text=_('Observation About the Inspection'),
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class AbstractDailyVehicleInspectionResponse(AbstractBaseModel):
    response: models.BooleanField = models.BooleanField(
        verbose_name=_('Response'),
        help_text=_('Response'),
    )

    class Meta:
        abstract = True


class UnitMeasurement(AbstractBaseModel):
    name: models.CharField = models.CharField(
        verbose_name=_('Name'),
        max_length=80,
    )
    acronym: models.CharField = models.CharField(
        verbose_name=_('Acronym'),
        max_length=3,
    )
    last_user: models.ForeignKey = models.ForeignKey(
        to='users.CustomUser',
        on_delete=models.RESTRICT,
        verbose_name=_('Last User'),
        related_name='unitmeasurement_customuser_lastuser',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = _('Unit of Measurement')
        verbose_name_plural = _('Units of Measurement')

    def __str__(self):
        return self.name
