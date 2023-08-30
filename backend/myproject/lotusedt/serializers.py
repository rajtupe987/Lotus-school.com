from rest_framework import serializers
from .models import Instructor,Expertise

class InstructorSerializer(serializers.ModelSerializer):
    expertise = serializers.PrimaryKeyRelatedField(queryset=Expertise.objects.all(), many=True)

    class Meta:
        model = Instructor
        fields = ['id', 'first_name', 'last_name', 'expertise', 'email', 'password', 'created_at']


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = ['id', 'name']