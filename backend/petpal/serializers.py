from rest_framework import serializers
from .models import Petpal

class PetpalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petpal
        fields = ('id', 'title', 'description', 'completed')