from rest_framework.serializers import ModelSerializer
from .models import *

class TaskSerializer(ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_complete']