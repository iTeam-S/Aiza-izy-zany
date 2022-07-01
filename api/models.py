from re import T
import time
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserService(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=False)
    email = models.EmailField(unique=True, null=True)
    cin = models.CharField("cin", max_length=12, blank=True, null=True)
    adresse = models.CharField("adresse", max_length=100, blank=True, null=True)
    num = models.CharField("numero de telephone", max_length=100, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.first_name + " " + self.last_name


class TypeService(models.Model):
    nom_type_service = models.CharField("nom de type de service", max_length=10)

    def __str__(self):
        return self.nom_type_service


class Categorie(models.Model):
    nom_categ = models.CharField("nom du catégorie", max_length=255)

    def __str__(self):
        return self.nom_categ


class Classement(models.Model):
    nom_class = models.CharField("nom du classement", max_length=255)

    def __str__(self):
        return self.nom_class


class ContactRs(models.Model):
    telephone = models.CharField("téléphone", max_length=20)
    mail = models.CharField("email", max_length=100, null=True, blank=True)
    skype = models.CharField("skype", max_length=100, null=True, blank=True)
    whatsapp = models.CharField("whatsapp", max_length=100, null=True, blank=True)
    page_facebook = models.CharField(
        "page facebook", max_length=255, null=True, blank=True
    )

    def __str__(self):
        return self.telephone


class Service(models.Model):
    nom = models.CharField("nom du service", max_length=50)

    def image_filename(instance, filename):
        extension = filename.split(".")[-1]
        specifique = str(time.time())
        new_filename = f"pdc_{instance.nom}_{specifique}.{extension}"
        return new_filename

    pdc = models.ImageField(
        "photo de couverture", upload_to=image_filename, blank=True, null=True
    )
    description = models.CharField("description", max_length=255)
    adresse = models.CharField("adresse", max_length=255)
    quartier = models.CharField("quartier", max_length=255, null=True)
    categorie = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, blank=True, null=True
    )
    classe = models.ForeignKey(
        Classement, on_delete=models.CASCADE, blank=True, null=True
    )
    type_de_service = models.ForeignKey(
        TypeService, on_delete=models.CASCADE, blank=True, null=True
    )
    contactrs = models.OneToOneField(ContactRs, on_delete=models.CASCADE, null=True)

    proprietaire = models.ForeignKey(
        UserService, on_delete=models.CASCADE, blank=True, null=True
    )
    date_created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.nom


class Media(models.Model):
    def file_filename(instance, filename):
        extension = filename.split(".")[-1]
        specifique = str(time.time())
        new_filename = f"file_{instance.service}_{specifique}.{extension}"
        return new_filename

    media = models.FileField("fichier", upload_to=file_filename, null=True, blank=True)
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return str(self.media)
