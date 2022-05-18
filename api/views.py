from .serileazers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = UserService.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ServiceViewSet(ModelViewSet):

    #Securiser à get seulement
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated,]

        return super(ServiceViewSet, self).get_permissions()

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
    permission_classes = [IsAuthenticated,]


class SeoViewSet(ModelViewSet):
    serializer_class = SeoSerializer
    queryset = Seo.objects.all()
    permission_classes = [IsAuthenticated,]
