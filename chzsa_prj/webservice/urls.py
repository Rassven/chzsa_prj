from django.urls import path

# пути в приложении webservice
from .views import *


urlpatterns = [
   path('welcome/', welcome, name="welcome"),
   path('rules/', RulesView.as_view(), name="rules"),
   # path('main/', MainPage.as_view(), name="main"),
   path('todo/', ToDo.as_view(), name="todo"),
   path('comments/', Comments.as_view(), name="comments"),
   path('xl_test/', xl_test, name="xl_test"),
   #
   # path('user/<int:pk>', UsersList.as_view(), name='users_list'),
   #
   path('machines', MachinesList.as_view(), name='machines_list'),
   path('machine/<int:pk>', MachineView.as_view(), name='machine'),
   path('machine/<int:pk>/edit/', MachineEdit.as_view(), name='machine_edit'),

   path('machinemodels/', MachineModels.as_view(), name='machinemodels'),
   path('machinemodel/<int:pk>', MachineModelView.as_view(), name='machinemodel'),

   path('enginemodels/', EngineModels.as_view(), name='enginemodels'),
   path('enginemodel/<int:pk>', EngineModelView.as_view(), name='enginemodel'),

   path('transmissionmodels/', TransmissionModels.as_view(), name='transmissionmodels'),
   path('transmissionmodel/<int:pk>', TransmissionModelView.as_view(), name='transmissionmodel'),

   path('drivebridgemodels/', DriveBridgeModels.as_view(), name='drivebridgemodels'),
   path('drivebridgemodel/<int:pk>', DriveBridgeModelView.as_view(), name='drivebridgemodel'),

   path('maintenances', MaintenanceList.as_view(), name='maintenances_list'),
   path('maintenance/<int:pk>', MaintenanceView.as_view(), name='maintenance'),
   # path('maintenance/<int:pk>/edit/', MaintenanceEdit.as_view(), name='maintenance_edit'),

   # path('claims', ClaimsList.as_view(), name='claims_list'),
   # path('claim/<int:pk>', ClaimView.as_view(), name='claim'),
   # path('claim/<int:pk>/edit/', ClaimEdit.as_view(), name='claim_edit'),

   path('report/', download_xlsx, name='create_report'),

]