from code_manager.models import Code
from rest_framework import serializers


class CodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Code
        fields = '__all__'
        extra_kwargs = {'code': {'write_only': True}}
