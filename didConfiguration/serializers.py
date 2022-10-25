from rest_framework_json_api import serializers
from didConfiguration.models import DidConfiguration

class DidConfigurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DidConfiguration
        fields = ('context',)
        
