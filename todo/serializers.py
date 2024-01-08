from rest_framework import serializers
from .models import ToDos


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDos
        fields = ['date', 'dev_name', 'pro_name', 'pro_description']
