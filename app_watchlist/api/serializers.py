from rest_framework import serializers
from app_watchlist.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "name", "description", "active", "len_name"]
        # fields = "__all__"
        # fields = ["id", "name"]
        # exclude = ["id"]

    def get_len_name(self, object):
        length = len(object.name)
        return length

    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("the name is too short")
        else:
            return value

    def validate(self, data):
        if data["name"] == data["description"]:
            raise serializers.ValidationError("cant be the same name and description")
        else:
            return data


# def check_len(value):
#     if len(value) < 4:
#         raise serializers.ValidationError(" description is too short")


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[check_len])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

#     def validate_name(self, value):
#         if len(value) < 4:
#             raise serializers.ValidationError("the name is too short")
#         else:
#             return value

#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("cant be the same name and description")
#         else:
#             return data
