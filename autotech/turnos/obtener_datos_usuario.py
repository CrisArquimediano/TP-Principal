from administracion.models import Taller

def obtener_email_usuario():
    return 'luciacsoria5@gmail.com'
    
def obtener_direccion_taller(taller_id) -> str:
    taller = Taller.objects.get(id_taller= taller_id)
    return f'{taller.direccion}, {taller.localidad}, {taller.provincia}.'