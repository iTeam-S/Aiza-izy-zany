from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from api.views import *

router = routers.SimpleRouter()

router.register("seo", SeoViewSet, basename="seo")
router.register("type", TypeMediaViewSet, basename="type")
router.register("media", MediaViewSet, basename="media")
router.register("service", ServiceViewSet, basename="service")
router.register("location", LocationViewSet, basename="location")
router.register("contactrs", ContactRsViewSet, basename="contactrs")
router.register("categorie", CategorieViewSet, basename="categorie")
router.register("classement", ClassementViewSet, basename="classement")

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
