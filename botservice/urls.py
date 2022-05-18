from api.views import *
from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from django.conf.urls.static import static
from .settings import MEDIA_ROOT, MEDIA_URL
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

router = routers.SimpleRouter()


router.register("seo", SeoViewSet, basename="seo")
router.register("media", MediaViewSet, basename="media")
router.register("service", ServiceViewSet, basename="service")

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("api/", include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

