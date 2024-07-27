from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter, OrderingFilter
from django.forms import DateTimeInput
from .models import *  # Machine, MaintenanceInfo, ClaimInfo  # *
from django.utils.translation import gettext_lazy as _

CHOICES = [["machine_number", "По номеру машины"], ["creation_date", "По дате создания"], ]


class MachineFilter(FilterSet):
    CHOICES = [["machine_number", "По номеру машины"],
               ["creation_date", "По дате создания"],
               ['machine_model', 'По модели машины'],
               ['engine_model', 'По модели двигателя'],
               ['transmission_model', 'По модели трансмиссии'],
               ['drive_bridge_model', 'По модели ведущего моста'],
               ['controlled_bridge_model', 'По модели управляемого моста'],
               ['shipment_date', 'По дате продажи'],
               ['end_user', 'По получателю'],
               ['service_company', 'По сервисной организации'],
               ]
    creation_date = DateTimeFilter(field_name=_('creation_date'), lookup_expr='gte',
                                   widget=DateTimeInput(format='%Y-%m-%d', attrs={'type': 'datetime-local'}, ), )
    ordering = OrderingFilter(choices=CHOICES, required=True, empty_label=None, )

    class Meta:
        model = Machine
        # fields = {'machine_number': ['exact'], 'machine_model': ['exact'], }
        # fields = '__all__'
        fields = {'machine_number': ['exact'], 'machine_model': ['exact'], }


class MaintenancesFilter(FilterSet):
    CHOICES = [["machine", "По номеру машины"],
               ["creation_date", "По дате создания"],
               ['worked_hours_time', 'По наработанным часам'],
               ['order_number', 'По номеру заказ-наряда'],
               ]
    # CHOICES = list(MaintenanceInfo.objects.all().__dict__.keys())
    # type = ModelChoiceFilter(queryset=MaintenanceTypesList.objects.all(), label='name', empty_label='любая', )
    creation_date = DateTimeFilter(field_name=_('creation_date'), lookup_expr='gte',
                                   widget=DateTimeInput(format='%Y-%m-%d', attrs={'type': 'datetime-local'}, ), )
    ordering = OrderingFilter(choices=CHOICES, required=True, empty_label=None, )

    class Meta:
        model = MaintenanceInfo
        fields = {'maintenance_type': ['exact'], 'machine': ['exact'], }  # 'creation_time': ['gte'], }
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
