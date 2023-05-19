from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register(r'talleres_admin', TallerViewSet, 'talleres_admin')
router.register(r'turnos_admin', TurnoTallerViewSet , 'turnos_admin')
router.register(r'checklist_reparacion_admin', ChecklistReparacionViewSet , 'checklist_reparacion_admin')
router.register(r'registro_reparacion_admin', RegistroReparacionViewSet , 'registro_reparacion_admin')


urlpatterns = [
    path('cobro_hora/todos',CobroXHoraTodosViewSet.as_view(actions={'get': 'list', 'post': 'create'}), name = 'cobro_x_hora_todos'),
    path('cobro_hora/Tecnicos/',CobroXHoraTecnicosViewSet.as_view(actions={'get': 'list'}), name = 'cobro_x_hora_tecnicos'),
    path('cobro_hora/Tecnicos/<str:categoria/',CobroXHoraTecnicosCategoriaViewSet.as_view(actions={'get': 'list'}), name = 'cobro_x_hora_tecnicos_categoria'),
    path('cobro_hora/Supervisores/',CobroXHoraSupervisorViewSet.as_view(actions={'get': 'list'}), name = 'cobro_x_hora_supervisor')
]


urlpatterns = router.urls + urlpatterns
