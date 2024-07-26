from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin  # , LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect

# my app:
from .models import *
from .filters import MachineFilter, MaintenancesFilter
from .forms import MachineForm
from .utils.xlsx_report_creator import create_excel_report


def download_xlsx(request):
    # сборщик опробовался на простом классе, а не на модели django и да, уже подсвечивает что не итерабельна.. И структура явно другая...
    return create_excel_report("project_report.xlsx")


def xl_test(request):
    display = []
    # print(Machine.mro())
    # prp_list = list(Machine.__dict__.keys())
    # print(prp_list)
    # if 'machine_model' in prp_list:
    #     print("FIND PROP", Machine.machine_model, Machine.machine_model.__dict__)
    # display.append({'Machine.machine_model': Machine.machine_model})
    # display.append({'Machine.machine_model.__dict__': Machine.machine_model.__dict__})
    display.append({'getattr(Machine, "machine_model")': getattr(Machine, "machine_model")})
    display.append({'hasattr(Machine, "machine_number")': hasattr(Machine, "machine_number")})
    display.append({'Machine.objects.all()': Machine.objects.all()})
    display.append({'list(Machine.objects.all())': list(Machine.objects.all())})
    # display.append({'list(Machine.objects.all())[0].__dict__': list(Machine.objects.all())[0].__dict__})
    # display.append({'list(Machine.objects.all())[0].__dict__.keys()': list(Machine.objects.all())[0].__dict__.keys()})
    display.append({'list(list(Machine.objects.all())[0].__dict__.keys())': list(list(Machine.objects.all())[0].__dict__.keys())})
    display.append({'getattr(list(Machine.objects.all())[0], "machine_model")': getattr(list(Machine.objects.all())[0], "machine_model")})
    one = list(Machine.objects.all())[0]
    # display.append({'one': one.__dict__})
    display.append({'one.machine_model': one.machine_model})
    display.append({'getattr(list(Machine.objects.all())[0], "machine_model")': type(getattr(list(Machine.objects.all())[0], "machine_model"))})
    co_model = getattr(list(Machine.objects.all())[0], "machine_model")
    display.append({'co_model.__dict__': co_model.__dict__})
    display.append({'co_model.__dict__.keys()': co_model.__dict__.keys()})

    return render(request, 'xl_test.html', context={"display": display})


class MachinesList(ListView):  # PermissionRequiredMixin
    # permission_required = ('webservice.view_machine',)
    model = Machine
    queryset = Machine.objects.all().filter(is_active=True,)  # .order_by('-creation_date')
    # ordering = '-creation_date'
    template_name = 'machines.html'
    context_object_name = 'machines'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MachineFilter(self.request.GET, queryset)
        return self.filterset.qs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     return context


class MachineView(DetailView):  # PermissionRequiredMixin
    # permission_required = ('webservice.view_machine',)
    model = Machine
    template_name = 'machine.html'
    context_object_name = 'machine'


class MachineEdit(UpdateView):  # PermissionRequiredMixin
    # permission_required = ('webservice.edit_machine', )
    form_class = MachineForm
    model = Machine
    template_name = 'machine_edit.html'
    success_url = reverse_lazy('machines_list')


class MachineModels(ListView):  # PermissionRequiredMixin
    # permission_required = ('webservice.view_machinemodelslist',)
    model = MachineModelsList
    queryset = MachineModelsList.objects.all().filter(is_active=True,)  # .order_by('-creation_date')
    # ordering = '-creation_date'
    template_name = 'machinemodels.html'
    context_object_name = 'machinemodels'


class MachineModelView(DetailView):  # PermissionRequiredMixin
    # permission_required = ('webservice.view_machinemodelslist',)
    model = MachineModelsList
    # queryset = MachineModelsList  #.objects.all().filter(is_active=True,)  # .order_by('-creation_date')
    # ordering = '-creation_date'
    template_name = 'machinemodel.html'
    context_object_name = 'machinemodel'


class EngineModels(ListView):  # PermissionRequiredMixin
    # permission_required = ('webservice.view_enginemodelslist',)
    model = EngineModelsList
    queryset = EngineModelsList.objects.all().filter(is_active=True,)  # .order_by('-creation_date')
    # ordering = '-creation_date'
    template_name = 'enginemodels.html'
    context_object_name = 'enginemodels'


class EngineModelView(DetailView):  # PermissionRequiredMixin
    # permission_required = ('webservice.view_machine',)
    model = EngineModelsList
    template_name = 'engine.html'
    context_object_name = 'engine'


class TransmissionModels(ListView):  # PermissionRequiredMixin
    # permission_required = ('webservice.view_enginemodelslist',)
    model = TransmissionModelsList
    queryset = TransmissionModelsList.objects.all().filter(is_active=True,)  # .order_by('-creation_date')
    # ordering = '-creation_date'
    template_name = 'transmissionmodels.html'
    context_object_name = 'transmissionmodels'


class TransmissionModelView(DetailView):  # PermissionRequiredMixin
    # permission_required = ('webservice.view_machine',)
    model = TransmissionModelsList
    template_name = 'transmission.html'
    context_object_name = 'transmission'


class DriveBridgeModels(ListView):  # PermissionRequiredMixin
    # permission_required = ('webservice.view_enginemodelslist',)
    model = DriveBridgeModelsList
    queryset = DriveBridgeModelsList.objects.all().filter(is_active=True,)  # .order_by('-creation_date')
    # ordering = '-creation_date'
    template_name = 'drivebridgemodels.html'
    context_object_name = 'drivebridgemodels'


class DriveBridgeModelView(DetailView):  # PermissionRequiredMixin
    # permission_required = ('webservice.view_machine',)
    model = DriveBridgeModelsList
    template_name = 'drivebridge.html'
    context_object_name = 'drivebridge'


class MaintenanceList(ListView):  # PermissionRequiredMixin
    # permission_required = ('webservice.view_enginemodelslist',)
    model = MaintenanceInfo
    # queryset = MaintenanceInfo.objects.all().filter(machine=1)  # .order_by('-creation_date')
    # ordering = '-creation_date'
    ordering = 'machine'
    template_name = 'maintenances.html'
    context_object_name = 'maintenances'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MaintenancesFilter(self.request.GET, queryset)
        return self.filterset.qs


class MaintenanceView(DetailView):  # PermissionRequiredMixin
    # permission_required = ('webservice.view_machine',)
    model = MaintenanceInfo
    template_name = 'maintenance.html'
    context_object_name = 'maintenance'


def welcome(request):
    return render(request, 'welcome.html')


class RulesView(TemplateView):
    template_name = 'rules.html'


class MainPage(TemplateView):
    template_name = 'main.html'


class ToDo(TemplateView):
    template_name = 'todo.html'


class Comments(TemplateView):
    template_name = 'comments.html'


