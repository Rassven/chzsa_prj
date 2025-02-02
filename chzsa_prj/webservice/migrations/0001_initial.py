# Generated by Django 5.0.6 on 2024-07-20 15:54

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('name', models.TextField(verbose_name='Client name')),
                ('description', models.TextField(verbose_name='Client description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Client status')),
            ],
        ),
        migrations.CreateModel(
            name='ControlledBridgeModelsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('name', models.TextField(verbose_name='Controlled bridge model name')),
                ('description', models.TextField(verbose_name='Controlled bridge model description')),
                ('work_history', models.JSONField(blank=True, null=True, verbose_name='Controlled bridge work history')),
                ('is_active', models.BooleanField(default=True, verbose_name='Controlled bridge status')),
            ],
        ),
        migrations.CreateModel(
            name='DriveBridgeModelsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('name', models.TextField(verbose_name='Drive bridge model name')),
                ('description', models.TextField(verbose_name='Drive bridge model description')),
                ('work_history', models.JSONField(blank=True, null=True, verbose_name='Drive bridge work history')),
                ('is_active', models.BooleanField(default=True, verbose_name='Drive bridge status')),
            ],
        ),
        migrations.CreateModel(
            name='EndUsersList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('name', models.TextField(verbose_name='End user name')),
                ('description', models.TextField(verbose_name='End user description')),
                ('is_active', models.BooleanField(default=True, verbose_name='End user status')),
            ],
        ),
        migrations.CreateModel(
            name='EngineModelsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('name', models.TextField(verbose_name='Engine model name')),
                ('description', models.TextField(verbose_name='Engine model description')),
                ('work_history', models.JSONField(blank=True, null=True, verbose_name='Engine work history')),
                ('is_active', models.BooleanField(default=True, verbose_name='Engine status')),
            ],
        ),
        migrations.CreateModel(
            name='MachineModelsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('name', models.TextField(verbose_name='Machine model name')),
                ('description', models.TextField(verbose_name='Machine model description')),
                ('work_history', models.JSONField(blank=True, null=True, verbose_name='Machine work history')),
                ('is_active', models.BooleanField(default=True, verbose_name='Machine model status')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceOrganizationsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('name', models.TextField(verbose_name='Maintenance organization name')),
                ('description', models.TextField(verbose_name='Maintenance organization description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Maintenance organization status')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceTypesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('name', models.TextField(verbose_name='Maintenance type name')),
                ('description', models.TextField(verbose_name='Maintenance type description')),
            ],
        ),
        migrations.CreateModel(
            name='NodesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('name', models.TextField(verbose_name='Node name')),
                ('description', models.TextField(verbose_name='Node description')),
                ('work_history', models.JSONField(blank=True, null=True, verbose_name='Node work history')),
                ('is_active', models.BooleanField(default=True, verbose_name='Node status')),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryMethodsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('name', models.TextField(verbose_name='Recovery method name')),
                ('description', models.TextField(verbose_name='Recovery method description')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCompaniesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('name', models.TextField(verbose_name='Service company name')),
                ('description', models.TextField(verbose_name='Service company description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Service company status')),
            ],
        ),
        migrations.CreateModel(
            name='TheUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('group_name', models.CharField(choices=[('enduser', 'Конечный пользователь'), ('service', 'Обслуживающая организация'), ('manager', 'Представитель производителя'), ('maintenance', 'Организация проводящая ТО'), ('client', 'Клиент (?)')], max_length=128, verbose_name='Group name')),
                ('access_code', models.CharField(default='0000-0000-0000-0000', max_length=24, unique=True, verbose_name='Access code')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionModelsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('name', models.TextField(verbose_name='Transmission model name')),
                ('description', models.TextField(verbose_name='Transmission model description')),
                ('work_history', models.JSONField(blank=True, null=True, verbose_name='Transmission work history')),
                ('is_active', models.BooleanField(default=True, verbose_name='Transmission status')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('machine_number', models.CharField(max_length=16, unique=True, verbose_name='Machine serial number')),
                ('engine_number', models.CharField(max_length=16, unique=True, verbose_name='Engine serial number')),
                ('transmission_number', models.CharField(max_length=16, unique=True, verbose_name='Transmission serial number')),
                ('drive_bridge_number', models.CharField(max_length=16, unique=True, verbose_name='Drive bridge serial number')),
                ('controlled_bridge_number', models.CharField(max_length=16, unique=True, verbose_name='Controlled bridge serial number')),
                ('info_about_delivery_agreement', models.CharField(blank=True, max_length=64, null=True, verbose_name='Information about the delivery agreement')),
                ('shipment_date', models.DateTimeField(blank=True, null=True, verbose_name='Date of shipment from the factory')),
                ('end_user_address', models.CharField(blank=True, max_length=128, null=True, verbose_name='End user address')),
                ('package_contents', models.TextField(blank=True, null=True, verbose_name='Package contents')),
                ('work_history', models.JSONField(blank=True, null=True, verbose_name='Machine work history')),
                ('is_active', models.BooleanField(default=True, verbose_name='Machine status')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.clientslist', verbose_name='Client')),
                ('controlled_bridge_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.controlledbridgemodelslist', verbose_name='Model of the controlled bridge')),
                ('drive_bridge_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.drivebridgemodelslist', verbose_name='Model of the drive bridge')),
                ('end_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.enduserslist', verbose_name='Consignee (end user)')),
                ('engine_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.enginemodelslist', verbose_name='Model of the engine')),
                ('machine_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.machinemodelslist', verbose_name='Model of the machine')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.servicecompanieslist', verbose_name='Service company name')),
                ('transmission_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.transmissionmodelslist', verbose_name='Model of the transmission')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('maintenance_date', models.DateTimeField(verbose_name='Date of maintenance')),
                ('worked_hours_time', models.IntegerField(default=0, verbose_name='Working hours time')),
                ('order_number', models.TextField(verbose_name='Order number')),
                ('order_date', models.DateTimeField(verbose_name='Date of the work order')),
                ('maintenance_description', models.TextField(verbose_name='Maintenance description')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.machine', verbose_name='Machine')),
                ('maintenance_organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.maintenanceorganizationslist', verbose_name='The organization that carried out the maintenance')),
                ('maintenance_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.maintenancetypeslist', verbose_name='Type of maintenance')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.servicecompanieslist', verbose_name='Service company name')),
            ],
        ),
        migrations.CreateModel(
            name='ClaimInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last edit')),
                ('failure_date', models.DateTimeField(verbose_name='Date of failure')),
                ('worked_hours_time', models.IntegerField(default=0, verbose_name='Working hours time')),
                ('failure_description', models.TextField(verbose_name='Description of the failure')),
                ('spare_parts', models.TextField(verbose_name='Spare parts used')),
                ('recovery_date', models.DateTimeField(verbose_name='Recovery date')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.machine', verbose_name='Machine')),
                ('failure_node', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.nodeslist', verbose_name='Node of failure')),
                ('recovery_method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.recoverymethodslist', verbose_name='Recovery method')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webservice.servicecompanieslist', verbose_name='Service company name')),
            ],
        ),
    ]
