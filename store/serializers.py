from rest_framework import serializers
from store.models import Box


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ['id','length','width','height','area','volume','last_updated']
        
class StaffBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ['id','length','width','height','area','volume','created_by','created_on','last_updated']
