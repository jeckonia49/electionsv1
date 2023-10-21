from django.forms import ValidationError
from rest_framework import serializers
from accounts.models import AccountUser, Profile
from django.contrib.auth import authenticate


class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = ("email", 'username')




    
class AccountUserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = "__all__"
    def create(self, validated_data):
        user_obj = AccountUser.objects.create_user(email=validated_data['email'], password=validated_data['password'], username=validated_data['username'])
        return user_obj
    



class AccountUserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, validated_data):
        user = authenticate(email=validated_data['email'], password=validated_data['password'])
        if not user:
            raise ValidationError("user not found")
        return user
    

