from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]

    extra_kwargs = {"password": {"write_only": True}}

    # field_attr=

    # def validate(self, attrs):
    #     return super().validate(attrs)

    # def save(self, **kwargs):
    #     return super().save(**kwargs)

    # def create(self, validated_data):
    #     return super().create(validated_data)
