from django.contrib import admin
from .models import *


# def machine_specification_loading(specification_dir):
#     pass


# class MachineAdmin(admin.ModelAdmin):
#     list_display = ('__all__',)
#     # list_display = ('name', 'created_date', 'last_edit', 'serial_number', 'status', 'user__name')
#     # list_display = [field.name for field in Machine._meta.get_fields()]  # генерируем список имён всех полей
#     list_filter = ('__all__',)
#     search_fields = ('__all__',)
#     fields = ['name', 'serial_number', 'produced_date', 'detail_info']
#     # actions = [machine_specification_loading]  # добавляем действия в список


# admin.site.register(Machine, MachineAdmin)
