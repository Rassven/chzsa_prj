from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Machine, MaintenanceInfo, ClaimInfo


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = '__all__'


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintenanceInfo
        # Maintenance.machine = forms.ModelChoiceField(label='Machine', queryset=Machine.objects.all())
        fields = '__all__'  # на время тестирования

