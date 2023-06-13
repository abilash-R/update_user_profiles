from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'bio', 'profile_picture']

    def validate_email(self, value):
        if not value.endswith('@example.com'):  # Custom email validation example
            raise serializers.ValidationError('Invalid email format. Only example.com emails are allowed.')
        return value