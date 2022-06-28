from rest_framework import serializers
from django.contrib.auth.models import User


#account serializer
class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50,min_length=8,write_only=True) #not retrievable
    email = serializers.EmailField(max_length=100, min_length=8)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    #check data 
    def validate(self, data):
        email = data.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({
                'email': ('Email already Exists')}) #error message
        return super().validate(data)

    #create user
    def create(self, validated_data):
        return User.objects.create_user(**validated_data) #create user (also split the data accordingly)