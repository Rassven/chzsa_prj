# Exception in thread django-main-thread:
# Traceback (most recent call last):
#   File "C:\Program Files\Python310\lib\threading.py", line 1016, in _bootstrap_inner
#     self.run()
#   File "C:\Program Files\Python310\lib\threading.py", line 953, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\LocalRepository\ChZSA\venv\lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
#     fn(*args, **kwargs)
#   File "C:\LocalRepository\ChZSA\venv\lib\site-packages\django\core\management\commands\runserver.py", line 133, in inner_run
#     self.check(display_num_errors=True)
#   File "C:\LocalRepository\ChZSA\venv\lib\site-packages\django\core\management\base.py", line 563, in check
#     raise SystemCheckError(msg)
# django.core.management.base.SystemCheckError: SystemCheckError: System check identified some issues:
#
# ERRORS:
# webservice.ClaimInfo.failure_node: (fields.E304) Reverse accessor 'ReferenceModel.claiminfo_set' for 'webservice.ClaimInfo.failure_node' clashes with reverse accessor for 'webservice.C
# laimInfo.recovery_method'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.ClaimInfo.failure_node' or 'webservice.ClaimInfo.recovery_method'.
# webservice.ClaimInfo.failure_node: (fields.E304) Reverse accessor 'ReferenceModel.claiminfo_set' for 'webservice.ClaimInfo.failure_node' clashes with reverse accessor for 'webservice.C
# laimInfo.service_company'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.ClaimInfo.failure_node' or 'webservice.ClaimInfo.service_company'.
# webservice.ClaimInfo.recovery_method: (fields.E304) Reverse accessor 'ReferenceModel.claiminfo_set' for 'webservice.ClaimInfo.recovery_method' clashes with reverse accessor for 'webser
# vice.ClaimInfo.failure_node'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.ClaimInfo.recovery_method' or 'webservice.ClaimInfo.failure_node'.
# webservice.ClaimInfo.recovery_method: (fields.E304) Reverse accessor 'ReferenceModel.claiminfo_set' for 'webservice.ClaimInfo.recovery_method' clashes with reverse accessor for 'webser
# vice.ClaimInfo.service_company'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.ClaimInfo.recovery_method' or 'webservice.ClaimInfo.service_company'.
# webservice.ClaimInfo.service_company: (fields.E304) Reverse accessor 'ReferenceModel.claiminfo_set' for 'webservice.ClaimInfo.service_company' clashes with reverse accessor for 'webser
# vice.ClaimInfo.failure_node'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.ClaimInfo.service_company' or 'webservice.ClaimInfo.failure_node'.
# webservice.ClaimInfo.service_company: (fields.E304) Reverse accessor 'ReferenceModel.claiminfo_set' for 'webservice.ClaimInfo.service_company' clashes with reverse accessor for 'webser
# vice.ClaimInfo.recovery_method'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.ClaimInfo.service_company' or 'webservice.ClaimInfo.recovery_method'.
# webservice.Machine.client: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.client' clashes with reverse accessor for 'webservice.Machine.controlled_
# bridge_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.client' or 'webservice.Machine.controlled_bridge_model'.
# webservice.Machine.client: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.client' clashes with reverse accessor for 'webservice.Machine.drive_bridg
# e_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.client' or 'webservice.Machine.drive_bridge_model'.
# webservice.Machine.client: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.client' clashes with reverse accessor for 'webservice.Machine.engine_mode
# l'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.client' or 'webservice.Machine.engine_model'.
# webservice.Machine.client: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.client' clashes with reverse accessor for 'webservice.Machine.machine_mod
# el'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.client' or 'webservice.Machine.machine_model'.
# webservice.Machine.client: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.client' clashes with reverse accessor for 'webservice.Machine.service_com
# pany'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.client' or 'webservice.Machine.service_company'.
# webservice.Machine.client: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.client' clashes with reverse accessor for 'webservice.Machine.transmissio
# n_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.client' or 'webservice.Machine.transmission_model'.
# webservice.Machine.controlled_bridge_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.controlled_bridge_model' clashes with reverse accessor f
# or 'webservice.Machine.client'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.controlled_bridge_model' or 'webservice.Machine.client'.
# webservice.Machine.controlled_bridge_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.controlled_bridge_model' clashes with reverse accessor f
# or 'webservice.Machine.drive_bridge_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.controlled_bridge_model' or 'webservice.Machine.drive_bridge_model'.
# webservice.Machine.controlled_bridge_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.controlled_bridge_model' clashes with reverse accessor f
# or 'webservice.Machine.engine_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.controlled_bridge_model' or 'webservice.Machine.engine_model'.
# webservice.Machine.controlled_bridge_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.controlled_bridge_model' clashes with reverse accessor f
# or 'webservice.Machine.machine_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.controlled_bridge_model' or 'webservice.Machine.machine_model'.
# webservice.Machine.controlled_bridge_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.controlled_bridge_model' clashes with reverse accessor f
# or 'webservice.Machine.service_company'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.controlled_bridge_model' or 'webservice.Machine.service_company'.
# webservice.Machine.controlled_bridge_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.controlled_bridge_model' clashes with reverse accessor f
# or 'webservice.Machine.transmission_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.controlled_bridge_model' or 'webservice.Machine.transmission_model'.
# webservice.Machine.drive_bridge_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.drive_bridge_model' clashes with reverse accessor for 'webser
# vice.Machine.client'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.drive_bridge_model' or 'webservice.Machine.client'.
# webservice.Machine.drive_bridge_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.drive_bridge_model' clashes with reverse accessor for 'webser
# vice.Machine.controlled_bridge_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.drive_bridge_model' or 'webservice.Machine.controlled_bridge_model'.
# webservice.Machine.drive_bridge_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.drive_bridge_model' clashes with reverse accessor for 'webser
# vice.Machine.engine_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.drive_bridge_model' or 'webservice.Machine.engine_model'.
# webservice.Machine.drive_bridge_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.drive_bridge_model' clashes with reverse accessor for 'webser
# vice.Machine.machine_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.drive_bridge_model' or 'webservice.Machine.machine_model'.
# webservice.Machine.drive_bridge_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.drive_bridge_model' clashes with reverse accessor for 'webser
# vice.Machine.service_company'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.drive_bridge_model' or 'webservice.Machine.service_company'.
# webservice.Machine.drive_bridge_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.drive_bridge_model' clashes with reverse accessor for 'webser
# vice.Machine.transmission_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.drive_bridge_model' or 'webservice.Machine.transmission_model'.
# webservice.Machine.engine_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.engine_model' clashes with reverse accessor for 'webservice.Machine
# .client'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.engine_model' or 'webservice.Machine.client'.
# webservice.Machine.engine_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.engine_model' clashes with reverse accessor for 'webservice.Machine
# .controlled_bridge_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.engine_model' or 'webservice.Machine.controlled_bridge_model'.
# webservice.Machine.engine_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.engine_model' clashes with reverse accessor for 'webservice.Machine
# .drive_bridge_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.engine_model' or 'webservice.Machine.drive_bridge_model'.
# webservice.Machine.engine_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.engine_model' clashes with reverse accessor for 'webservice.Machine
# .machine_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.engine_model' or 'webservice.Machine.machine_model'.
# webservice.Machine.engine_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.engine_model' clashes with reverse accessor for 'webservice.Machine
# .service_company'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.engine_model' or 'webservice.Machine.service_company'.
# webservice.Machine.engine_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.engine_model' clashes with reverse accessor for 'webservice.Machine
# .transmission_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.engine_model' or 'webservice.Machine.transmission_model'.
# webservice.Machine.machine_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.machine_model' clashes with reverse accessor for 'webservice.Machi
# ne.client'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.machine_model' or 'webservice.Machine.client'.
# webservice.Machine.machine_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.machine_model' clashes with reverse accessor for 'webservice.Machi
# ne.controlled_bridge_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.machine_model' or 'webservice.Machine.controlled_bridge_model'.
# webservice.Machine.machine_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.machine_model' clashes with reverse accessor for 'webservice.Machi
# ne.drive_bridge_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.machine_model' or 'webservice.Machine.drive_bridge_model'.
# webservice.Machine.machine_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.machine_model' clashes with reverse accessor for 'webservice.Machi
# ne.engine_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.machine_model' or 'webservice.Machine.engine_model'.
# webservice.Machine.machine_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.machine_model' clashes with reverse accessor for 'webservice.Machi
# ne.service_company'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.machine_model' or 'webservice.Machine.service_company'.
# webservice.Machine.machine_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.machine_model' clashes with reverse accessor for 'webservice.Machi
# ne.transmission_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.machine_model' or 'webservice.Machine.transmission_model'.
# webservice.Machine.service_company: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.service_company' clashes with reverse accessor for 'webservice.M
# achine.client'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.service_company' or 'webservice.Machine.client'.
# webservice.Machine.service_company: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.service_company' clashes with reverse accessor for 'webservice.M
# achine.controlled_bridge_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.service_company' or 'webservice.Machine.controlled_bridge_model'.
# webservice.Machine.service_company: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.service_company' clashes with reverse accessor for 'webservice.M
# achine.drive_bridge_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.service_company' or 'webservice.Machine.drive_bridge_model'.
# webservice.Machine.service_company: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.service_company' clashes with reverse accessor for 'webservice.M
# achine.engine_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.service_company' or 'webservice.Machine.engine_model'.
# webservice.Machine.service_company: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.service_company' clashes with reverse accessor for 'webservice.M
# achine.machine_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.service_company' or 'webservice.Machine.machine_model'.
# webservice.Machine.service_company: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.service_company' clashes with reverse accessor for 'webservice.M
# achine.transmission_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.service_company' or 'webservice.Machine.transmission_model'.
# webservice.Machine.transmission_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.transmission_model' clashes with reverse accessor for 'webser
# vice.Machine.client'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.transmission_model' or 'webservice.Machine.client'.
# webservice.Machine.transmission_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.transmission_model' clashes with reverse accessor for 'webser
# vice.Machine.controlled_bridge_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.transmission_model' or 'webservice.Machine.controlled_bridge_model'.
# webservice.Machine.transmission_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.transmission_model' clashes with reverse accessor for 'webser
# vice.Machine.drive_bridge_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.transmission_model' or 'webservice.Machine.drive_bridge_model'.
# webservice.Machine.transmission_model: (fields.E304) Reverse accessor 'ReferenceModel.machine_set' for 'webservice.Machine.transmission_model' clashes with reverse accessor for 'webser
# vice.Machine.engine_model'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.Machine.transmission_model' or 'webservice.Machine.engine_model'.
# webservice.MaintenanceInfo.service_company: (fields.E304) Reverse accessor 'ReferenceModel.maintenanceinfo_set' for 'webservice.MaintenanceInfo.service_company' clashes with reverse ac
# cessor for 'webservice.MaintenanceInfo.maintenance_organization'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.MaintenanceInfo.service_company' or 'webservice.MaintenanceInfo.maintenance_organization'.
# webservice.MaintenanceInfo.service_company: (fields.E304) Reverse accessor 'ReferenceModel.maintenanceinfo_set' for 'webservice.MaintenanceInfo.service_company' clashes with reverse ac
# cessor for 'webservice.MaintenanceInfo.maintenance_type'.
#         HINT: Add or change a related_name argument to the definition for 'webservice.MaintenanceInfo.service_company' or 'webservice.MaintenanceInfo.maintenance_type'.
#
# System check identified 54 issues (0 silenced).
