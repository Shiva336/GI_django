from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ["name", "email", "age"]
        
    def validate_name(self, name):
        if not name.strip():
            raise serializers.ValidationError("Name should not be empty")
        return name
    
    def validate_age(self, age):
        if age < 0 or age > 120: 
            raise serializers.ValidationError("Age must be a number between 0 and 120")
        return age