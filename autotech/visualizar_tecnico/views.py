from django.shortcuts import render
from rest_framework import viewsets, filters
from models import TecnicoModel

class BusquedaTecnicosView(viewsets.ReadOnlyModelViewSet):
    queryset = TecnicoModel.objects.all()
    serializer = TecnicoSerializer

    #filtrado
    filtro = [filters.SearchFilter]
    search_fields = ['nombre', 'apellido', 'anio']
