from django.urls import path

# пути в приложении webservice
from .views import *


urlpatterns = [
   path('welcome/', start, name="welcome"),
   path('rules/', RulesView.as_view(), name="rules"),
   path('main/', MainPage.as_view(), name="main"),
   path('todo/', ToDo.as_view(), name="todo"),
   path('comments/', Comments.as_view(), name="comments"),
   #
   # path('user/<int:pk>', UsersList.as_view(), name='users_list'),
   #
   path('machines', MachinesList.as_view(), name='machines_list'),
   path('machine/<int:pk>', MachineView.as_view(), name='machine'),
   path('machine/<int:pk>/edit/', MachineEdit.as_view(), name='machine_edit'),

   # path('maintenances', MachinesList.as_view(), name='maintenances_list'),
   # path('maintenance/<int:pk>', MaintenanceView.as_view(), name='maintenance'),
   # path('maintenance/<int:pk>/edit/', MaintenanceEdit.as_view(), name='maintenance_edit'),

   # path('claims', ClaimsList.as_view(), name='claims_list'),
   # path('claim/<int:pk>', ClaimView.as_view(), name='claim'),
   # path('claim/<int:pk>/edit/', ClaimEdit.as_view(), name='claim_edit'),

]