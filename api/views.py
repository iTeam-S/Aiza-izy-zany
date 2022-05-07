from .serileazers import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class TypeMediaViewSet(ModelViewSet):
    serializer_class = TypeMediaSerializer
    queryset = TypeMedia.objects.all()


class CategorieViewSet(ModelViewSet):
    serializer_class = CategorieSerializer
    queryset = Categorie.objects.all()


class ClassementViewSet(ModelViewSet):
    serializer_class = ClassementSerializer
    queryset = Classement.objects.all()


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class ContactRsViewSet(ModelViewSet):
    serializer_class = ContactRsSerializer
    queryset = ContactRs.objects.all()


class ServiceViewSet(ReadOnlyModelViewSet):

    serializer_class = ServiceSerializer

    def get_queryset(self):

        formelle = self.request.GET.get("formelle")
        informelle = self.request.GET.get("informelle")

        if formelle and formelle == "ok":
            queryset = Service.objects.filter(type_de_service=1)

        elif informelle and informelle == "ok":
            queryset = Service.objects.filter(type_de_service=2)
        
        else:
            queryset = Service.objects.all()

        return queryset


class MediaViewSet(ModelViewSet):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()


class SeoViewSet(ModelViewSet):
    serializer_class = SeoSerializer
    queryset = Seo.objects.all()
