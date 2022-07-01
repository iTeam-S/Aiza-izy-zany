from .models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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
            "first_name",
            "last_name",
            "cin",
            "adresse",
            "num",
            "email",
            "password",
            "password2",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "email": {"unique": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = UserService.objects.create(
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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        # Add extra responses here
        data["id"] = self.user.id
        data["email"] = self.user.email
        data["nom"] = self.user.first_name
        data["prenom"] = self.user.last_name

        return data


class CategorieSerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = "__all__"


class ClassementSerializer(ModelSerializer):
    class Meta:
        model = Classement
        fields = "__all__"


class TypeServiceSerializer(ModelSerializer):
    class Meta:
        model = TypeService
        fields = "__all__"


class ContactRsSerializer(ModelSerializer):
    class Meta:
        model = ContactRs
        fields = ("telephone", "mail", "skype", "whatsapp", "page_facebook")

    # def validate_mail(self, value):
    #     if ContactRs.objects.filter(mail=value).exists():
    #         raise ValidationError("Mail already exists")
    #     return value


class ServiceSerializer(ModelSerializer):

    contactrs = ContactRsSerializer()

    class Meta:
        model = Service
        fields = "__all__"

    def create(self, validated_data):
        contactrs_data = validated_data.pop("contactrs")
        contactrs_save = ContactRs.objects.create(**contactrs_data)
        contactrs_save.save()
        service = Service.objects.create(contactrs=contactrs_save, **validated_data)
        service.save()
        return service


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"
