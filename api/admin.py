from django.contrib import admin
from .models import *


class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "nom_type")


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
        "contactrs",
    )

    def quartier_proche(self, obj):
        return "\n".join([a.quartier_proche for a in obj.quartier_proche.all()])

    # @admin.display(description='quartier proche')
    # def quartier_proche(self, obj):
    #     deg = Location.objects.filter(personal=obj).first()
    #     if deg:
    #         return deg.name_degree
    #     return None

class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "nom_media", "service", "type")


class SeoAdmin(admin.ModelAdmin):
    list_display = ("id", "mot", "service")


admin.site.register(Type, TypeAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Classement, ClassementAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(ContactRs, ContactRsAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Seo, SeoAdmin)


