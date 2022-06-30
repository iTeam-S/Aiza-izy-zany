from .models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer, ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=UserService.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserService
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
            "cin",
            "adresse",
            "num",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = UserService.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            cin=validated_data["cin"],
            adresse=validated_data["adresse"],
            num=validated_data["num"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class CategorieSerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = "__all__"


class ClassementSerializer(ModelSerializer):
    class Meta:
        model = Classement
        fields = "__all__"


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ("quartier_proche",)


class ContactRsSerializer(ModelSerializer):
    class Meta:
        model = ContactRs
        fields = ("telephone", "mail", "skype", "whatsapp", "page_facebook")

    def validate_mail(self, value):
        if ContactRs.objects.filter(mail=value).exists():
            raise ValidationError("Mail already exists")
        return value


class ServiceSerializer(ModelSerializer):

    contactrs = ContactRsSerializer()

    class Meta:
        model = Service
        fields = "__all__"


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"
