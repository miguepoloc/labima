from django.shortcuts import render
from rest_framework import views, viewsets, mixins
from rest_framework.response import Response
from .serializers import (Categoria_componenteSerializer, Categoria_sensorSerializer, ComponenteSerializer,
                          EstacionSerializer, Componente_EstacionSerializer, SensorSerializer, Sensor_EstacionSerializer,
                          Tipo_Salida_De_CampoSerializer, InvestigadorSerializer, Salidas_De_CampoSerializer,
                          Sensor_Salidas_De_CampoSerializer, Componente_Salidas_De_CampoSerializer, Calendario_Salidas_De_CampoSerializer,
                          Tipo_EstacionSerializer, DataSerializer, Codigo_SensorSerializer)
from .models import (Categoria_componente, Categoria_sensor, Componente,
                     Estacion, Componente_Estacion, Sensor, Sensor_Estacion, Tipo_Salida_De_Campo, Investigador,
                     Salidas_De_Campo, Sensor_Salidas_De_Campo, Componente_Salidas_De_Campo, Calendario_Salidas_De_Campo,
                     Tipo_Estacion, Data, Codigo_Sensor)


class Codigo_SensorViewSet(viewsets.ModelViewSet):

    queryset = Codigo_Sensor.objects.all().order_by('id')
    serializer_class = Codigo_SensorSerializer


class DataViewSet(viewsets.ModelViewSet):

    queryset = Data.objects.all().order_by('-fecha')
    serializer_class = DataSerializer


class Tipo_EstacionViewSet(viewsets.ModelViewSet):

    queryset = Tipo_Estacion.objects.all().order_by('id')
    serializer_class = Tipo_EstacionSerializer


class Categoria_componenteViewSet(viewsets.ModelViewSet):

    queryset = Categoria_componente.objects.all().order_by('id')
    serializer_class = Categoria_componenteSerializer


class Categoria_sensorViewSet(viewsets.ModelViewSet):

    queryset = Categoria_sensor.objects.all().order_by('id')
    serializer_class = Categoria_sensorSerializer


class SensorViewSet(viewsets.ModelViewSet):

    queryset = Sensor.objects.all().order_by('id')
    serializer_class = SensorSerializer


class Sensor_EstacionViewSet(viewsets.ModelViewSet):

    queryset = Sensor_Estacion.objects.all().order_by('id')
    serializer_class = Sensor_EstacionSerializer


class ComponenteViewSet(viewsets.ModelViewSet):

    queryset = Componente.objects.all().order_by('id')
    serializer_class = ComponenteSerializer


class Componente_EstacionViewSet(viewsets.ModelViewSet):

    queryset = Componente_Estacion.objects.all().order_by('id')
    serializer_class = Componente_EstacionSerializer


class EstacionViewSet(viewsets.ModelViewSet):

    queryset = Estacion.objects.all().order_by('id')
    serializer_class = EstacionSerializer


class Tipo_Salida_De_CampoViewSet(viewsets.ModelViewSet):

    queryset = Tipo_Salida_De_Campo.objects.all().order_by('id')
    serializer_class = Tipo_Salida_De_CampoSerializer


class InvestigadorViewSet(viewsets.ModelViewSet):

    queryset = Investigador.objects.all().order_by('id')
    serializer_class = InvestigadorSerializer


class Salidas_De_CampoViewSet(viewsets.ModelViewSet):

    queryset = Salidas_De_Campo.objects.all().order_by('-fecha')
    serializer_class = Salidas_De_CampoSerializer


class Sensor_Salidas_De_CampoViewSet(viewsets.ModelViewSet):

    queryset = Sensor_Salidas_De_Campo.objects.all().order_by('id')
    serializer_class = Sensor_Salidas_De_CampoSerializer


class Componente_Salidas_De_CampoViewSet(viewsets.ModelViewSet):

    queryset = Componente_Salidas_De_Campo.objects.all().order_by('id')
    serializer_class = Componente_Salidas_De_CampoSerializer


class Calendario_Salidas_De_CampoViewSet(viewsets.ModelViewSet):

    queryset = Calendario_Salidas_De_Campo.objects.all().order_by('-fecha_inicio')
    serializer_class = Calendario_Salidas_De_CampoSerializer
