from rest_framework import serializers
from .models import webScrModel,sendArrayModal

class webScrSerializer(serializers.ModelSerializer):
    class Meta():
        model = webScrModel
        fields = '__all__'

class sendArrayModalSerializer(serializers.ModelSerializer):
    class Meta():
        model = sendArrayModal
        fields = '__all__'