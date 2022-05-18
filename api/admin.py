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


class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "quartier_proche")


class ContactRsAdmin(admin.ModelAdmin):
    list_display = ("id", "telephone", "mail", "skype", "whatsapp", "page_facebook")


class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nom",
        "pdc",
        "description",
        "adresse",
        "quartier",
        "quartier_proche",
        "categorie",
        "classe",
        "type_de_service",
        "contactrs",
    )

    def quartier_proche(self, obj):
        print(obj)
        return "\n".join([a.quartier_proche for a in obj.quartier_proche.all()])


class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "media", "service")


class SeoAdmin(admin.ModelAdmin):
    list_display = ("id", "mot", "service")


admin.site.register(Seo, SeoAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(ContactRs, ContactRsAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Classement, ClassementAdmin)
admin.site.register(TypeService, TypeServiceAdmin)
admin.site.register(UserService, UserServiceAdmin)
