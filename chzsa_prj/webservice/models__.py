from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import timedelta
# from django.urls import reverse


class Machine(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    # last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    machine_number = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name=_('Machine serial number'))
    machine_model = models.ForeignKey(to='ReferenceModel', on_delete=models.PROTECT, verbose_name=_('Model of the machine'))
    engine_model = models.ForeignKey(to='ReferenceModel', on_delete=models.PROTECT, verbose_name=_('Model of the engine'))
    engine_number = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name=_('Engine serial number'))
    transmission_model = models.ForeignKey(to='ReferenceModel', on_delete=models.PROTECT, verbose_name=_('Model of the transmission'))
    transmission_number = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name=_('Transmission serial number'))
    drive_bridge_model = models.ForeignKey(to='ReferenceModel', on_delete=models.PROTECT, verbose_name=_('Model of the drive bridge'))
    drive_bridge_number = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name=_('Drive bridge serial number'))
    controlled_bridge_model = models.ForeignKey(to='ReferenceModel', on_delete=models.PROTECT, verbose_name=_('Model of the controlled bridge'))
    controlled_bridge_number = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name=_('Controlled bridge serial number'))
    info_about_delivery_agreement = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('Information about the delivery agreement'))
    shipment_date = models.DateTimeField(null=True, blank=True, verbose_name=_('Date of shipment from the factory'))
    end_user = models.CharField(max_length=128, null=True, blank=True, verbose_name=_('Consignee (end user)'))
    user_address = models.CharField(max_length=128, null=True, blank=True, verbose_name=_('End user address'))
    package_contents = models.TextField(null=True, blank=True, verbose_name=_('Package contents'))
    client = models.ForeignKey(to='ReferenceModel', on_delete=models.PROTECT, verbose_name=_('Client'))
    service_company = models.ForeignKey(to='ReferenceModel', on_delete=models.PROTECT, verbose_name=_('Service company name'))

    # def machine_specification_loading(self, machine_number):
    #     answer = maintenance_info_loader(machine_number)
    #     if answer:  # Все поля валидны
    #     parametr(n) = maintenance_info_loader(machine_number, value_name(n))...
    #     self.machine_number = machine_number
    # ?   self.save()

    def __str__(self):
        return f'Machine:{self.machine_number}'

    # def get_url(self):
    #     return reverse('machine', args=[str(self.id)])


class MaintenanceInfo(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    # last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    maintenance_type = models.ForeignKey(to='ReferenceModel', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Type of maintenance'))
    maintenance_date = models.DateTimeField(null=False, blank=False, verbose_name=_('Date of maintenance'))
    worked_hours_time = models.IntegerField(default=0, null=False, blank=False,verbose_name=_('Working hours time'))
    order_number = models.TextField(null=False, blank=False, verbose_name=_('Order number'))
    order_date = models.DateTimeField(null=False, blank=False, verbose_name=_('Date of the work order'))
    maintenance_organization = models.ForeignKey(to='ReferenceModel', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('The organization that carried out the maintenance'))
    machine = models.ForeignKey(to='Machine', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Machine'))
    service_company = models.ForeignKey(to='ReferenceModel', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Service company name'))
    maintenance_description = models.TextField(null=False, blank=False, verbose_name=_('Maintenance description'))

    def __str__(self):
        return f'MaintenanceInfo:{self.maintenance_date}'

    # def get_url(self):
    #     return reverse('maintenance', args=[str(self.id)])


class ClaimInfo(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    # last_edit_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last edit'))
    # last_view_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last view'))
    failure_date = models.DateTimeField(null=False, blank=False, verbose_name=_('Date of failure'))
    worked_hours_time = models.IntegerField(default=0, null=False, blank=False, verbose_name=_('Working hours time'))
    failure_node = models.ForeignKey(to='ReferenceModel', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Node of failure'))
    failure_description = models.TextField(null=False, blank=False, verbose_name=_('Description of the failure'))
    recovery_method = models.ForeignKey(to='ReferenceModel', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Recovery method'))
    spare_parts = models.TextField(null=False, blank=False, verbose_name=_('Spare parts used'))
    recovery_date = models.DateTimeField(null=False, blank=False, verbose_name=_('Recovery date'))
    # TypeError: unsupported operand type(s) for -: 'DateTimeField' and 'DateTimeField'
    # equipment_downtime = recovery_date - failure_date  # DateTimeField operations?
    machine = models.ForeignKey(to='Machine', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Machine'))
    service_company = models.ForeignKey(to='ReferenceModel', null=False, blank=False, on_delete=models.PROTECT, verbose_name=_('Service company name'))

    def __str__(self):
        return f'ClaimInfo:{self.failure_date}'

    # def get_url(self):
    #     return reverse('claim', args=[str(self.id)])


class ReferenceModel(models.Model):
    directory_name = models.TextField(null=False, blank=False, verbose_name=_('The name of the directory'))
    name = models.TextField(null=False, blank=False, verbose_name=_('Name'))
    description = models.TextField(null=False, blank=False, verbose_name=_('Description'))
