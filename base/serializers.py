from rest_framework import serializers
from .models import Base


class BaseSerializer(serializers.Serializer):
    
    class Meta:
        model = Base
        fields = ["date", "time", "message"]
 
    def validate(self, attrs):
        return attrs
    
    def create(self, attrs):
        base_obj = Base.objects.create(**attrs)
        return base_obj
