from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin  # , LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect

# my app:
from .models import *
from .filters import MachineFilter
from .forms import MachineForm
# from ..utils import spc_hash_check, xlsx_report_creator


class MachinesList(PermissionRequiredMixin, ListView):
    permission_required = ('webservice.view_machine',)
    model = Machine
    queryset = Machine.objects.all().filter(is_active=True,)  # .order_by('-creation_date')
    ordering = '-creation_date'
    template_name = 'machines.html'

    context_object_name = 'machines'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = MachineFilter(self.request.GET, queryset)
    #     return self.filterset.qs


class MachineView(PermissionRequiredMixin, DetailView):
    permission_required = ('webservice.view_machine',)
    model = Machine
    template_name = 'machine.html'
    context_object_name = 'machine'


class MachineEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('webservice.edit_machine', )
    form_class = MachineForm
    model = Machine
    template_name = 'machine_edit.html'
    success_url = reverse_lazy('machines_list')


def start(request):
    print('Start page message: >>> Запущен сервер приложения. <<<')
    return render(request, 'welcome.html')


class RulesView(TemplateView):
    template_name = 'rules.html'


class MainPage(TemplateView):
    template_name = 'main.html'


class ToDo(TemplateView):
    template_name = 'todo.html'


class Comments(TemplateView):
    template_name = 'comments.html'
