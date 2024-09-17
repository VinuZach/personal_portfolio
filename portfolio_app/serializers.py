from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetails
        fields = '__all__'


class TechInProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechInProject
        fields = '__all__'
