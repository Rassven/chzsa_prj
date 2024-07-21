from django.contrib import admin
from .models import *
# from ..utils import spc_hash_check, xlsx_report_creator

# class MachineAdmin(admin.ModelAdmin):
#     list_display = ('__all__',)
#     # list_display = ('name', 'created_date', 'last_edit', 'serial_number', 'status', 'user__name')
#     # list_display = [field.name for field in Machine._meta.get_fields()]  # генерируем список имён всех полей
#     list_filter = ('__all__',)
#     search_fields = ('__all__',)
#     fields = ['name', 'serial_number', 'produced_date', 'detail_info']
#     # actions = [machine_specification_loading]  # добавляем действия в список

# class MachineAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class MachineModelsListAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class EngineModelsListAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class TransmissionModelsListAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class DriveBridgeModelsListAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class ControlledBridgeModelsListAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class TheUserAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class EndUsersListAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class ClientsListAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class ServiceCompaniesListAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class MaintenanceOrganizationsListAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class MaintenanceInfoAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class MaintenanceTypesListAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class ClaimInfoAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class NodesListAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# class RecoveryMethodsListAdmin(admin.ModelAdmin):
#     list_display = ('__all__', )
#     list_filter = ('__all__', )
#     search_fields = ('__all__', )
#     fields = ['__all__', ]
#
#
# admin.site.register(Machine, MachineAdmin)
# admin.site.register(MachineModelsList, MachineModelsListAdmin)
# admin.site.register(EngineModelsList, EngineModelsListAdmin)
# admin.site.register(TransmissionModelsList, TransmissionModelsListAdmin)
# admin.site.register(DriveBridgeModelsList, DriveBridgeModelsListAdmin)
# admin.site.register(ControlledBridgeModelsList, ControlledBridgeModelsListAdmin)
# admin.site.register(TheUser, TheUserAdmin)
# admin.site.register(EndUsersList, EndUsersListAdmin)
# admin.site.register(ClientsList, ClientsListAdmin)
# admin.site.register(ServiceCompaniesList, ServiceCompaniesListAdmin)
# admin.site.register(MaintenanceOrganizationsList, MaintenanceOrganizationsListAdmin)
# admin.site.register(MaintenanceInfo, MaintenanceInfoAdmin)
# admin.site.register(MaintenanceTypesList, MaintenanceTypesListAdmin)
# admin.site.register(ClaimInfo, ClaimInfoAdmin)
# admin.site.register(NodesList, NodesListAdmin)
# admin.site.register(RecoveryMethodsList, RecoveryMethodsListAdmin)

admin.site.register(Machine)
admin.site.register(MachineModelsList)
admin.site.register(EngineModelsList)
admin.site.register(TransmissionModelsList)
admin.site.register(DriveBridgeModelsList)
admin.site.register(ControlledBridgeModelsList)
admin.site.register(TheUser)
admin.site.register(EndUsersList)
admin.site.register(ClientsList)
admin.site.register(ServiceCompaniesList)
admin.site.register(MaintenanceOrganizationsList)
admin.site.register(MaintenanceInfo)
admin.site.register(MaintenanceTypesList)
admin.site.register(ClaimInfo)
admin.site.register(NodesList)
admin.site.register(RecoveryMethodsList)
