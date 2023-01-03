from rest_framework import serializers
from cliente.models import Municipio, Departamento, Direccion, TipoCliente, Cliente

class DepartamentoSerializer(serializers.ModelSerializer):
    #user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model= Departamento
        fields= "__all__"
        
class DepSerializer(serializers.ModelSerializer):
    #user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model= Departamento
        fields= ('id', 'nombre', 'create')
        
class DepartamentoMiniSerializer(serializers.ModelSerializer):
    #user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model= Departamento
        fields= ('id', 'nombre', 'create')

class MunicipioSerializer(serializers.ModelSerializer):
    #departamento=DepartamentoSerializer() #Mostrar toda la data del serializador  a través de foreignkey 
    departamento=serializers.StringRelatedField()#Muestra el __str__ que se define en el modelo 
    class Meta:
        model= Municipio
        fields= "__all__"
   
class MunicipioWithDepartamentoSerializer(serializers.ModelSerializer):
    departamento=DepartamentoSerializer(write_only=True)
    class Meta:
        model=Municipio
        fields= "__all__"
        
class DireccionSerializer(serializers.ModelSerializer):
    #departamento=serializers.StringRelatedField()
    #municipio=serializers.StringRelatedField()
    class Meta:
        model=Direccion
        fields= "__all__"
        


class ClienteSerializer(serializers.ModelSerializer):
    #tipoclientelist=TipoCLienteSerializer(many=True, read_only=True)
    #direccion=serializers.StringRelatedField()
    
    direccioncliente=serializers.StringRelatedField(many=True, read_only=True)
    #tipo_cliente=serializers.StringRelatedField()
    class Meta:
        model=Cliente
        #exclude=['direccion']
        fields= "__all__"
        
    # def update(self, validated_data):
    #     tipo_cliente_data=validated_data.pop('tipoclientelist')
    #     cliente=Cliente.objects.update(**validated_data)
    #     for i in range(tipo_cliente_data):
    #         TipoCliente.objects.update(cliente=cliente, **i)
    #     return cliente
class TipoCLienteSerializer(serializers.ModelSerializer):
    #stipoclientelist=ClienteSerializer(many=True, read_only=True)
    clientelist=serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model:TipoCliente
        fields= "__all__"    

        

        

     
 