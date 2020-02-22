from app.models import User, Record
from rest_framework import serializers


class RecordSerializer(serializers.ModelSerializer):
    owner = serializers.CharField()
    quit_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Record
        fields = ['owner', 'quit_date', 'is_active']
