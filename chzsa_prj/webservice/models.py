from django.db import models
from django.contrib.auth.models import Group, User, Permission
from django.utils.translation import gettext_lazy as _
from datetime import timedelta
# from django.urls import reverse


class Machine(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    machine_number = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name=_('Machine serial number'))
    machine_model = models.ForeignKey(to='MachineModelsList', on_delete=models.PROTECT, verbose_name=_('Model of the machine'))
    engine_model = models.ForeignKey(to='EngineModelsList', on_delete=models.PROTECT, verbose_name=_('Model of the engine'))
    engine_number = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name=_('Engine serial number'))
    transmission_model = models.ForeignKey(to='TransmissionModelsList', on_delete=models.PROTECT, verbose_name=_('Model of the transmission'))
    transmission_number = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name=_('Transmission serial number'))
    drive_bridge_model = models.ForeignKey(to='DriveBridgeModelsList', on_delete=models.PROTECT, verbose_name=_('Model of the drive bridge'))
    drive_bridge_number = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name=_('Drive bridge serial number'))
    controlled_bridge_model = models.ForeignKey(to='ControlledBridgeModelsList', on_delete=models.PROTECT, verbose_name=_('Model of the controlled bridge'))
    controlled_bridge_number = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name=_('Controlled bridge serial number'))
    info_about_delivery_agreement = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('Information about the delivery agreement'))
    shipment_date = models.DateTimeField(null=True, blank=True, verbose_name=_('Date of shipment from the factory'))
    end_user = models.ForeignKey(to='EndUsersList', on_delete=models.PROTECT, verbose_name=_('Consignee (end user)'))
    end_user_address = models.CharField(max_length=128, null=True, blank=True, verbose_name=_('End user address'))
    package_contents = models.TextField(null=True, blank=True, verbose_name=_('Package contents'))
    client = models.ForeignKey(to='ClientsList', on_delete=models.PROTECT, verbose_name=_('Client'))
    service_company = models.ForeignKey(to='ServiceCompaniesList', on_delete=models.PROTECT, verbose_name=_('Service company name'))
    is_active = models.BooleanField(default=True, verbose_name=_('Machine status'))

    def __str__(self):
        return f'Machine:{self.machine_number}'

    # def get_url(self):
    #     return reverse('machine', args=[str(self.id)])


# Lists for type Machine:
class MachineModelsList(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    name = models.TextField(null=False, blank=False, verbose_name=_('Machine model name'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Machine model description'))
    work_history = models.JSONField(encoder=None, decoder=None, null=True, blank=True, verbose_name=_('Machine work history'))
    is_active = models.BooleanField(default=True, verbose_name=_('Machine model status'))


class EngineModelsList(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    name = models.TextField(null=False, blank=False, verbose_name=_('Engine model name'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Engine model description'))
    work_history = models.JSONField(encoder=None, decoder=None, null=True, blank=True, verbose_name=_('Engine work history'))
    is_active = models.BooleanField(default=True, verbose_name=_('Engine status'))


class TransmissionModelsList(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    name = models.TextField(null=False, blank=False, verbose_name=_('Transmission model name'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Transmission model description'))
    work_history = models.JSONField(encoder=None, decoder=None, null=True, blank=True, verbose_name=_('Transmission work history'))
    is_active = models.BooleanField(default=True, verbose_name=_('Transmission status'))


class DriveBridgeModelsList(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    name = models.TextField(null=False, blank=False, verbose_name=_('Drive bridge model name'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Drive bridge model description'))
    work_history = models.JSONField(encoder=None, decoder=None, null=True, blank=True, verbose_name=_('Drive bridge work history'))
    is_active = models.BooleanField(default=True, verbose_name=_('Drive bridge status'))


class ControlledBridgeModelsList(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    name = models.TextField(null=False, blank=False, verbose_name=_('Controlled bridge model name'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Controlled bridge model description'))
    work_history = models.JSONField(encoder=None, decoder=None, null=True, blank=True, verbose_name=_('Controlled bridge work history'))
    is_active = models.BooleanField(default=True, verbose_name=_('Controlled bridge status'))


class TheUser(User):
    # Основные (\venv\Lib\site-packages\django\contrib\auth\models.py)
    # password, last_login (Дата и время последней активности в веб-приложении), username(unique),
    # email, is_staff (может заходить в панель администратора), is_active (доступ пользователя
    # на сайт в целом), date_joined (дата и время регистрации пользователя)
    CHOICE_LIST = [('enduser', 'Конечный пользователь'), ('service', 'Обслуживающая организация'),
                   ('manager', 'Представитель производителя'), ('maintenance', 'Организация проводящая ТО'),
                   ('client', 'Клиент (?)'), ]
    group_name = models.CharField(max_length=128, choices=CHOICE_LIST, null=False, blank=False, verbose_name=_("Group name"))
    # group_permissions = models.ManyToManyField(Permission, null=False, blank=False, verbose_name=_("Group permissions"))
    # personal_code = pc_gen(name=username, group=group_name, date=date_joined, type="card")
    access_code = models.CharField(max_length=24, default='0000-0000-0000-0000', unique=True, verbose_name=_('Access code'), )
    # last_viewed_url = models.URLField(null=True, blank=True, verbose_name=_('Last viewed page'), )
    # Уведомления на ...
    # m_mailing = models.BooleanField(default=False, verbose_name=_('Mailing'))  # отправка на e-mail
    # t_mailing = models.BooleanField(default=False, verbose_name=_('Phone notifications'))  # отправка на телефон
    #  def email_user(self, subject, message, from_email=None, **kwargs):
    #         """Send an email to this user."""
    #         send_mail(subject, message, from_email, [self.email], **kwargs)
    REQUIRED_FIELDS = ["email", "username", "group_name", "access_code"]

    def __str__(self):
        return f'<{self.username}>'  # ({self.email})>'


class EndUsersList(TheUser):
    # creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    # last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    name = models.TextField(null=False, blank=False, verbose_name=_('End user name'))
    description = models.TextField(null=False, blank=False, verbose_name=_('End user description'))
    # is_active = models.BooleanField(default=True, verbose_name=_('End user status'))


class ClientsList(TheUser):
    # creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    # last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    name = models.TextField(null=False, blank=False, verbose_name=_('Client name'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Client description'))
    # is_active = models.BooleanField(default=True, verbose_name=_('Client status'))


class ServiceCompaniesList(TheUser):  # по заданию одна
    # creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    # last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    name = models.TextField(null=False, blank=False, verbose_name=_('Service company name'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Service company description'))
    # is_active = models.BooleanField(default=True, verbose_name=_('Service company status'))


class MaintenanceOrganizationsList(TheUser):
    # creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    # last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    name = models.TextField(null=False, blank=False, verbose_name=_('Maintenance organization name'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Maintenance organization description'))
    # is_active = models.BooleanField(default=True, verbose_name=_('Maintenance organization status'))


class MaintenanceInfo(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    maintenance_type = models.ForeignKey(to='MaintenanceTypesList', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Type of maintenance'))
    maintenance_date = models.DateTimeField(null=False, blank=False, verbose_name=_('Date of maintenance'))
    worked_hours_time = models.IntegerField(default=0, null=False, blank=False,verbose_name=_('Working hours time'))
    order_number = models.TextField(null=False, blank=False, verbose_name=_('Order number'))
    order_date = models.DateTimeField(null=False, blank=False, verbose_name=_('Date of the work order'))
    maintenance_organization = models.ForeignKey(to='MaintenanceOrganizationsList', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('The organization that carried out the maintenance'))
    machine = models.ForeignKey(to='Machine', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Machine'))
    service_company = models.ForeignKey(to='ServiceCompaniesList', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Service company name'))
    maintenance_description = models.TextField(null=False, blank=False, verbose_name=_('Maintenance description'))

    def __str__(self):
        return f'MaintenanceInfo:{self.maintenance_date}'

    # def get_url(self):
    #     return reverse('maintenance', args=[str(self.id)])


# Lists for type MaintenanceInfo:
class MaintenanceTypesList(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    name = models.TextField(null=False, blank=False, verbose_name=_('Maintenance type name'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Maintenance type description'))


class ClaimInfo(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    failure_date = models.DateTimeField(null=False, blank=False, verbose_name=_('Date of failure'))
    worked_hours_time = models.IntegerField(default=0, null=False, blank=False, verbose_name=_('Working hours time'))
    failure_node = models.ForeignKey(to='NodesList', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Node of failure'))
    failure_description = models.TextField(null=False, blank=False, verbose_name=_('Description of the failure'))
    recovery_method = models.ForeignKey(to='RecoveryMethodsList', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Recovery method'))
    spare_parts = models.TextField(null=False, blank=False, verbose_name=_('Spare parts used'))
    recovery_date = models.DateTimeField(null=False, blank=False, verbose_name=_('Recovery date'))
    # TypeError: unsupported operand type(s) for -: 'DateTimeField' and 'DateTimeField'
    # equipment_downtime = recovery_date - failure_date  # DateTimeField operations?
    machine = models.ForeignKey(to='Machine', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Machine'))
    service_company = models.ForeignKey(to='ServiceCompaniesList', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Service company name'))

    def __str__(self):
        return f'ClaimInfo:{self.failure_date}'

    # def get_url(self):
    #     return reverse('claim', args=[str(self.id)])


# Lists for type ClaimInfo:
class NodesList(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    name = models.TextField(null=False, blank=False, verbose_name=_('Node name'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Node description'))
    work_history = models.JSONField(encoder=None, decoder=None, null=True, blank=True, verbose_name=_('Node work history'))
    is_active = models.BooleanField(default=True, verbose_name=_('Node status'))
    # См. комплектацию... Данные модели Machine.


class RecoveryMethodsList(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    name = models.TextField(null=False, blank=False, verbose_name=_('Recovery method name'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Recovery method description'))
