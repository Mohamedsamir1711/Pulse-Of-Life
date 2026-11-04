# myapp/serializers.py
from rest_framework import serializers
from .management.commands.models import Result

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'