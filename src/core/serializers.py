from rest_framework import serializers
from .models import Contact, Group, User

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields:str = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = Contact
        fields:tuple = ('user','phone_number','email','address','notes','groups')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields:tuple = ('username', 'password', 'email')
        extra_kwargs:dict = {'password': {'write_only': True}}

    def create(self, validated_data: dict) -> User:
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
