from rest_framework import serializers
from  .models import Facilities

class FacilitiesSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ['background_image','title','description']