from .serileazers import *
from rest_framework import filters
from rest_framework import generics
from .permissions import IsAdminAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterView(generics.CreateAPIView):
    queryset = UserService.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ServiceViewSet(ModelViewSet):

    # Securiser à get seulement
    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]
        else:
            self.permission_classes = [
                IsAuthenticated,
            ]

        return super(ServiceViewSet, self).get_permissions()

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["categorie", "type_de_service", "classe", "active"]
    search_fields = [
        "nom",
        "type_de_service__nom_type_service",
        "categorie__nom_categ",
        "classe__nom_class",
    ]
    serializer_class = ServiceSerializer
    queryset = Service.objects.all().order_by("classe")


class CategorieViewSet(ModelViewSet):
    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]
        else:
            self.permission_classes = [
                IsAdminAuthenticated,
            ]

        return super(CategorieViewSet, self).get_permissions()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["nom_categ"]
    serializer_class = CategorieSerializer
    queryset = Categorie.objects.all()


class MediaViewSet(ModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id"]
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    # permission_classes = (IsAuthenticated,)


class ClassementViewSet(ModelViewSet):
    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]
        else:
            self.permission_classes = [
                IsAdminAuthenticated,
            ]

        return super(ClassementViewSet, self).get_permissions()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["nom_class"]
    serializer_class = ClassementSerializer
    queryset = Classement.objects.all()


class TypeServiceViewSet(ModelViewSet):
    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]
        else:
            self.permission_classes = [
                IsAdminAuthenticated,
            ]

        return super(TypeServiceViewSet, self).get_permissions()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["nom_type_service"]
    serializer_class = TypeServiceSerializer
    queryset = TypeService.objects.all()
