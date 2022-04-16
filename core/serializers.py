from pyexpat import model
from django.db.models import fields
from rest_framework import serializers
from activity.models import Activity
from tour.models import Tour
from staycation.models import Staycation

class ActivityListSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField('is_type')
    name=serializers.SerializerMethodField('is_name')

    def is_name(self,obj):
      return obj.activity_name

    def is_type(self,obj):
      return "activity"



    class Meta:
        model = Activity
        fields = ["id","name","image","latitude","longitude","type"]

        # lookup_field = 'slug'

class TourListSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField('is_type')
    name=serializers.SerializerMethodField('is_name')

    def is_name(self,obj):
      return obj.tour_name

    def is_type(self,obj):
      return "tours"

    class Meta:
        model=Tour
        fields = ["id","name","image","latitude","longitude","type"]
    
class StaycationListSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField('is_type')
    name=serializers.SerializerMethodField('is_name')

    def is_name(self,obj):
      return obj.staycation_name

    def is_type(self,obj):
      return "hotels"
      
    class Meta:
        model=Staycation
        fields = ["id","name","feature_image","latitude","longitude","type"]
