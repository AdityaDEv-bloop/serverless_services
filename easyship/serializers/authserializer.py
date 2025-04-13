from rest_framework import serializers
from ..models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("email","username","firstname","lastname","phonenumber")



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("email","username","firstname","lastname","phonenumber","password")
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = Account(email = validated_data["email"],
                                    username = self.validated_data["username"], 
                                    firstname = validated_data["firstname"],
                                    lastname = validated_data["lastname"],
                                    phonenumber = validated_data["phonenumber"] ,)

        user.set_password( validated_data["password"])
        user.save()
        return user