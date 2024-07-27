from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Machine, MaintenanceInfo, ClaimInfo


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = '__all__'

    field_order = ['creation_date', 'machine_number']


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintenanceInfo
        # Maintenance.machine = forms.ModelChoiceField(label='Machine', queryset=Machine.objects.all())
        fields = '__all__'  # на время тестирования


class ClaimForm(forms.ModelForm):
    class Meta:
        model = ClaimInfo
        fields = '__all__'  # на время тестирования

