from django.db import models


class Type(models.Model):
    nom_type = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_type


class Categorie(models.Model):
    nom_categ = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_categ


class Classement(models.Model):
    nom_class = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_class


class Location(models.Model):
    quartier_proche = models.CharField(max_length=255)

    def __str__(self):
        return self.quartier_proche


class ContactRs(models.Model):
    telephone = models.CharField(max_length=20)
    mail = models.CharField(max_length=100, null=True)
    skype = models.CharField(max_length=100, null=True)
    whatsapp = models.CharField(max_length=100, null=True)
    page_facebook = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.telephone


class Service(models.Model):
    nom = models.CharField(max_length=50)
    pdc = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    quartier = models.CharField(max_length=255, null=True)
    quartier_proche = models.ManyToManyField("Location")
    categorie = models.ForeignKey(
        Categorie, on_delete=models.SET_NULL, blank=True, null=True
    )
    classe = models.ForeignKey(
        Classement, on_delete=models.SET_NULL, blank=True, null=True
    )
    contactrs = models.OneToOneField(ContactRs, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

class Media(models.Model):
    nom_media = models.CharField(max_length=100)
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, blank=True, null=True
    )
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, blank=True, null=True)
    
    
    def __str__(self):
        return self.nom_media

class Seo(models.Model):
    mot = models.CharField(max_length=50)
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.mot


