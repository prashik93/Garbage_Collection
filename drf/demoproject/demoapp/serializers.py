from rest_framework import serializers
from .models import Flat,Manager,Analytics

class FlatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = '__all__'


class FlatManagerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class AnalyticsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Analytics
        fields = '__all__'