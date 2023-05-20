import requests
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from administracion.models import Turno_taller
from .detalle_turnos_views import DetalleTurnosViewSet
from .validaciones_views import ValidadorSupervisor


class EstadoTurnosViewSet(ViewSet):
    ESTADO_PENDIENTE = 'pendiente'
    ESTADO_EN_PROCESO = 'en_proceso'
    ESTADO_TERMINADO = 'terminado'
    ESTADO_CANCELADO = 'cancelado'
    validador_sup = ValidadorSupervisor()
    detalle = DetalleTurnosViewSet()

    @action(detail=False, methods=['get'])
    def turnos_pendientes(self, request):
        papeles_en_regla = request.GET.get('papeles_en_regla')
        sucursal_supervisor = request.GET.get('branch')
        if not self.validador_sup.sucursal(sucursal_supervisor):
            return HttpResponse('error: numero de sucursal no valido', status=400)
        if papeles_en_regla is None or (papeles_en_regla.lower() != 'true' and papeles_en_regla.lower() != 'false'):
            return HttpResponse('error: se requiere información sobre si los papeles están en regla o no', status=400)       
        id_sucursal = self.obtener_id_sucursal(sucursal_supervisor)
        pendientes = []
        if papeles_en_regla.lower() == 'true':
            pendientes += self.obtener_turnos_por_estado(self.ESTADO_PENDIENTE, id_sucursal, tipo='service')
            pendientes += self.obtener_turnos_por_estado(self.ESTADO_PENDIENTE, id_sucursal, tipo='extraordinario')
            pendientes += self.obtener_turnos_por_estado(self.ESTADO_PENDIENTE, id_sucursal, tipo='reparacion')
            pendientes += self.obtener_turnos_por_estado(self.ESTADO_PENDIENTE, id_sucursal, papeles_en_regla=True, tipo='evaluacion')
        elif papeles_en_regla.lower() == 'false':
            pendientes = self.obtener_turnos_por_estado(self.ESTADO_PENDIENTE, id_sucursal, papeles_en_regla=False, tipo='evaluacion')
        turnos_data = self.detalle.obtener_data_turnos_pendientes(pendientes)
        return Response(turnos_data)

    @action(detail=False, methods=['get'])
    def turnos_en_proceso(self, request):
        sucursal_supervisor = request.GET.get('branch')
        if not self.validador_sup.sucursal(sucursal_supervisor):
            return HttpResponse({'error': 'Numero de sucursal no valido'}, status=400)     
        id_sucursal = self.obtener_id_sucursal(sucursal_supervisor)
        en_procesos = self.obtener_turnos_por_estado(self.ESTADO_EN_PROCESO, id_sucursal)
        try:
            turnos_data = self.detalle.obtener_data_turnos_en_proceso_terminado(en_procesos, self.ESTADO_EN_PROCESO)
            return Response(turnos_data)
        except requests.HTTPError as e:
            return HttpResponse(str(e), status=e.response.status_code)
        except Exception as e:
                return HttpResponse('error: violacion en el sistema existe un turno asignado a un usuario que no es un tecnico', status=404)

    @action(detail=False, methods=['get'])
    def turnos_terminados(self, request):
        sucursal_supervisor = request.GET.get('branch')
        if not self.validador_sup.sucursal(sucursal_supervisor):
            return HttpResponse('error: numero de sucursal no valido', status=400)     
        id_sucursal = self.obtener_id_sucursal(sucursal_supervisor)
        terminados = self.obtener_turnos_por_estado(self.ESTADO_TERMINADO, id_sucursal)
        try:
            turnos_data = self.detalle.obtener_data_turnos_en_proceso_terminado(terminados, self.ESTADO_TERMINADO)  
            return Response(turnos_data)
        except requests.HTTPError as e:
            return HttpResponse(str(e), status=e.response.status_code)
        except Exception as e:
                return HttpResponse('error: violacion en el sistema existe un turno asignado a un usuario que no es un tecnico', status=404)   
    
    @action(detail=True, methods=['patch'])
    def actualizar_estado_turno_en_proceso(self, request, id_turno):  
        try:
            turno = Turno_taller.objects.get(id_turno=id_turno, estado=self.ESTADO_EN_PROCESO)
        except Turno_taller.DoesNotExist:
            return HttpResponse('error: el turno no existe o no esta en proceso', status=400)      
        turno.estado = self.ESTADO_TERMINADO
        turno.save()
        return HttpResponse('El turno ha cambiado de estado a terminado exitosamente.')
  
    
    @action(detail=True, methods=['patch'])
    def cancelar_turno_pendiente(self, request, id_turno):
        try:
            turno = Turno_taller.objects.get(id_turno=id_turno, estado=self.ESTADO_PENDIENTE)
        except Turno_taller.DoesNotExist:
            return HttpResponse('error: el turno no existe o no esta en estado pendiente', status=400) 
        turno.estado = self.ESTADO_CANCELADO
        turno.save()
        return HttpResponse('El turno ha sido cancelado correctamente.')
        
    def obtener_id_sucursal(self, sucursal_supervisor):
        return int(sucursal_supervisor[-3:])

    def obtener_turnos_por_estado(self, estado, id_sucursal, papeles_en_regla=None, tipo=None):
        query = Turno_taller.objects.filter(estado=estado, taller_id=id_sucursal)
        if papeles_en_regla is not None:
            query = query.filter(papeles_en_regla=papeles_en_regla)
        if tipo is not None:
                query = query.filter(tipo=tipo)
        return query