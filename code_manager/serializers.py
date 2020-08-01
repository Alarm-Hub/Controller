from code_manager.models import Code
from rest_framework import serializers


class CodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Code
        fields = ['id', 'last_used']  # code should never returned
