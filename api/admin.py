from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class UserServiceAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "cin",
        "adresse",
        "num",
        "password",
    )


class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "nom_type")


class TypeServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "nom_type_service")


class CategorieAdmin(admin.ModelAdmin):
    list_display = ("id", "nom_categ")


class ClassementAdmin(admin.ModelAdmin):
    list_display = ("id", "nom_class")


class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nom",
        "pdc",
        "description",
        "adresse",
        "quartier",
        "categorie",
        "classe",
        "type_de_service",
        "telephone",
        "mail",
        "skype",
        "whatsapp",
        "page_facebook",
        "date_created",
        "active",
    )

    def quartier_proche(self, obj):
        print(obj)
        return "\n".join([a.quartier_proche for a in obj.quartier_proche.all()])


class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "media", "service")


admin.site.register(Media, MediaAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Classement, ClassementAdmin)
admin.site.register(TypeService, TypeServiceAdmin)
admin.site.register(UserService, UserServiceAdmin)
