from rest_framework.response import Response
from cliente.models import Municipio, Departamento, Direccion, TipoCliente, Cliente
from cliente.api.serializers import (MunicipioSerializer, ClienteSerializer, MunicipioWithDepartamentoSerializer, 
                                     DepartamentoSerializer, DepartamentoMiniSerializer, DepSerializer)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from cliente.api.permissions import IsAdminOrReadOnly, IsDepartamentoUserOrReadonly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import viewsets, filters
from cliente.api.pagination import DepartamentoPagination, DepartamentoLOPagination

#from rest_framework_filters import Filterset, NumberFilter
class ClienteLS(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes=[IsAuthenticated]

    # def list(self, request, *args, **kwargs):
    #     departamento = Cliente.objects.all()
    #     serializer = ClienteSerializer(departamento, many=True)
    #     return Response(serializer.data)
    
    # def create(self, request):
    #     serializer=ClienteSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

# class ClienteLS(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Cliente.objects.all()
#     serializer_class=ClienteSerializer
    
   
    

# class DepartamentoLS(viewsets.ModelViewSet):
#     queryset=Departamento.objects.all()
#     serializer_class = DepSerializer    # def list(self, request):
#     #     queryset=Departamento.objects.all()
#     #     serializer=DepSerializer(queryset, many=True)
#     #     return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         queryset=Departamento.objects.get(pk=pk)
#         serializer=DepSerializer(queryset)     
#         return Response(serializer.data) 
    
    # def create(self, request):
    #     serializer=DepSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
#     def update(self, request, pk):
#         try:
#             departamento=Departamento.objects.get(pk=pk)
#         except Departamento.DoesNotExist:
#             return Response({'error': 'Departamento does not exist'}, status=status.HTTP_404_NOT_FOUND)
#         serializer=DepSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class DepartamentoVS(viewsets.ModelViewSet):
    queryset=Departamento.objects.all()
    serializer_class = DepSerializer
    # def list(self, request):
    #     queryset=Departamento.objects.all()
    #     serializer=DepSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # def retrieve(self, request, pk=None):
    #     queryset=Departamento.objects.get(pk=pk)
    #     serializer=DepSerializer(queryset)     
    #     return Response(serializer.data) 
    
    # def create(self, request):
    #     serializer=DepSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    # def update(self, request, pk):
    #     try:
    #         departamento=Departamento.objects.get(pk=pk)
    #     except Departamento.DoesNotExist:
    #         return Response({'error': 'Departamento does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #     serializer=DepSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

class UsuarioDepartamento(generics.ListAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    
    # def get_queryset(self):
    #     username=self.kwargs['username']
    #     return Departamento.objects.filter(user__username=username)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre']
    #pagination_class=DepartamentoLOPagination
    pagination_class=DepartamentoPagination
   
    
    # def get_queryset(self):
    #     username=self.request.query_params.get('username', None)
    #     return Departamento.objects.filter(user__username=username)

class DepartamentoAC(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset=Departamento.objects.all()
    serializer_class=DepSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    

class DepartamentoRetrieve(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset=Departamento.objects.all()
    serializer_class=DepSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class DepartamentoListAV(APIView):
    # queryset=Departamento.objects.all()
    # serializer_class=DepartamentoSerializer
    
    # def list(self, request, *args, **kwargs):
    #     departamento=Departamento.objects.all()
    #     serializer=DepartamentoMiniSerializer(departamento, many=True)
    #     return Response(serializer.data)
        
    
    
    
   # permission_classes = [IsAdminOrReadOnly]
    
    #permission_classes = [IsAuthenticated]
    def get(self, request): #Desplegar resultados
        departamento=Departamento.objects.all()
        serializer=DepartamentoSerializer(departamento, many=True)
        return Response(serializer.data)

    def post(self, request): #Un nuevi registro  
        serializer=DepartamentoSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
    
    throttle_classes=[UserRateThrottle, AnonRateThrottle]
        
class DepartamentoDetalleAV(APIView):
    #permission_classes = [IsAdminOrReadOnly]
    
    def put(self, request, pk): #Modificar registro  
        try:
            departamento=Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=DepartamentoSerializer(departamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, pk):
        try:
            departamento=Departamento.objects.get(pk=pk) 
        except Departamento.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=DepartamentoSerializer(departamento)
        return Response(serializer.data)
    
    # def get(self, request): #Desplegar resultados
    #     departamento=Departamento.objects.all()
    #     serializer=DepartamentoSerializer(departamento, many=True)
    #     return Response(serializer.data)

    def post(self, request): #Un nuevi registro  
        serializer=DepartamentoSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
   
        
    def delete(self, request, pk): #Borrar registro
        try:
            departamento=Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        departamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClienteListAV(APIView):
    def get(self, request): #Desplegar resultados
        cliente=Cliente.objects.all()
        serializer=ClienteSerializer(cliente, many=True)
        return Response(serializer.data)

    def post(self, request): #Un nuevi registro  
        serializer=ClienteSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
class ClienteDetail(APIView):
    def get(self, request, pk):
        try:
            cliente=Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=ClienteSerializer(cliente)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        try:
            cliente=Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:    
            cliente=Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        



class MuncipioWithDepartamentoAV(APIView):
    def get(self, request): #Desplegar resultados
        municipio=Municipio.objects.all()
        serializer=MunicipioWithDepartamentoSerializer(municipio, many=True)
        return Response(serializer.data)
    
    def post(self, request): #Un nuevi registro  
        serializer=MunicipioWithDepartamentoSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MuncipioListAV(APIView):
    def get(self, request): #Desplegar resultados
        municipio=Municipio.objects.all()
        serializer=MunicipioSerializer(municipio, many=True)
        return Response(serializer.data)
    
    def post(self, request): #Un nuevi registro  
        serializer=MunicipioSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
class MunicipioDetalleAV(APIView):
    
    def get(self, request, pk):
        try:
            municipio=Municipio.objects.get(pk=pk) 
        except Municipio.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=MunicipioSerializer(municipio)
        return Response(serializer.data)
    
    def put(self, request, pk): #Modificar registro  
        try:
            municipio=Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=MunicipioSerializer(municipio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk): #Borrar registro
        try:
            municipio=Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        municipio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
        
class ClienteList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset= Cliente.objects.all()
    serializer_class=ClienteSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class MunicipioDepartamentoLS(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset= Municipio.objects.all()
    serializer_class=MunicipioWithDepartamentoSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)