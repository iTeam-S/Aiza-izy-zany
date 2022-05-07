from .models import *
from rest_framework.serializers import ModelSerializer


class TypeMediaSerializer(ModelSerializer):
    class Meta:
        model = TypeMedia
        fields = "__all__"


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
        fields = "__all__"


class ContactRsSerializer(ModelSerializer):
    class Meta:
        model = ContactRs
        fields = "__all__"


class ServiceSerializer(ModelSerializer):

    categorie = CategorieSerializer()
    classe = ClassementSerializer()
    contactrs = ContactRsSerializer()

    class Meta:
        model = Service
        fields = "__all__"


class MediaSerializer(ModelSerializer):

    type = TypeMediaSerializer()

    class Meta:
        model = Media
        fields = "__all__"


class SeoSerializer(ModelSerializer):

    service = ServiceSerializer()

    class Meta:
        model = Seo
        fields = "__all__"
