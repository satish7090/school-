from rest_framework import serializers
from .models import schoollist


class schoollistSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = schoollist
        fields = '__all__'
