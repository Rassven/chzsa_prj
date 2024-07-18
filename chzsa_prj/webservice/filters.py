from django_filters import FilterSet, DateTimeFilter, FilterSet, ModelChoiceFilter
from django.forms import DateTimeInput
from .models import *  # Machine, MaintenanceInfo, ClaimInfo  # *
from django.utils.translation import gettext_lazy as _


class MachineFilter(FilterSet):
    creation_date = DateTimeFilter(field_name=_('creation_date'), lookup_expr='gte',
                                   widget=DateTimeInput(format='%Y-%m-%d', attrs={'type': 'datetime-local'}, ), )

    class Meta:
        model = Machine
        fields = {'machine_number': ['exact'], 'machine_model': ['exact'], }


class MaintenancesFilter(FilterSet):
    type = ModelChoiceFilter(queryset=MaintenanceTypesList.objects.all(), label='name', empty_label='любая', )
    create_time = DateTimeFilter(field_name='edit_time', lookup_expr='gte',
                                 widget=DateTimeInput(format='%Y-%m-%d', attrs={'type': 'datetime-local'}, ), )

    class Meta:
        model = MaintenanceInfo
        fields = {'maintenance_type': ['exact'], 'maintenance_date': ['gte'], }  # 'creation_time': ['gte'], }
        #  exact - полное соответствие
        #  iexact - Точное совпадение без учета регистра.
        #  contains - Тест на содержание с учетом регистра.
        #  icontains - Тест содержание без учета регистра.
        #  in - В заданном итерируемом; часто это список, кортеж или набор запросов. Это не распространенный вариант
        #       использования, но допустимы строки (будучи итерируемыми).
        #  gte - Больше или равно.
        #  lte - Меньше или равно.
        #  startswith - С учетом регистра начинается с.
        #  istartswith - Начинается с без учета регистра.
        #  endswith - С учетом регистра заканчивается на .
        #  iendswith - Без учета регистра заканчивается на .
        #  range - Проверка дальности (включительно).
        #  date - Для полей даты и времени преобразует значение в дату. Позволяет связывать дополнительные поиски полей.
        #           Принимает значение даты
