# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser
from .models import FoodIntake

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'activity_level', 'height', 'weight', 'username', 'password', 'required_intake']
        extra_kwargs = {
            'password': {'write_only': True},
            
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
            activity_level=validated_data['activity_level'],
            height=validated_data['height'],
            weight=validated_data['weight'],
            required_intake = validated_data['required_intake'],
        )
        user.set_password(validated_data['password'])
        
        user.save()
        return user
class FoodIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodIntake
        fields = ['date', 'meal_time', 'calories', 'carbs', 'protein', 'fat']
        read_only_fields = ['user']