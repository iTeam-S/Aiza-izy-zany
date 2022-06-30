# BOT SERVICE

## Documentation de toutes les APIs
## GET

> GET tout les services FORMELS et ACTIVES <br>
> NB: Dans la BDD, l'id de type du service FORMEL est obligatoirement 1

```
GET http://127.0.0.1:8000/api/service/?type_de_service=1&active=true
```

> GET tout les services INFORMELS et ACTIVES  <br>
> NB: Dans la BDD, l'id de type du service INFORMEL est obligatoirement 2

```
GET http://127.0.0.1:8000/api/service/?type_de_service=2&active=true
```
> GET tout les services d'un categorie dans un type de service [informel ou formelle] et actives

```
GET http://127.0.0.1:8000/api/service/?categorie={id_categorie}&type_de_service={id_type_de_service}&active=true
```

>GET toutes les informations concernant un seul service

```
GET http://127.0.0.1:8000/api/service/{service_id}
```
> GET tout les services recherché à partir d'un mot clé

```
GET http://127.0.0.1:8000/api/service/?search={mot_cle}&active=true
```
> GET tout les services filtrés par sa classe [chaque service est classé de l'un de ces trois classes qui sont GOLD, MEDIUM et LESS. Alors dans la BDD ces derniers ont l'id respectivement 1,2 et 3

```
GET http://127.0.0.1:8000/api/service/?classe={id_classe}&active=true
```
> GET tous les categories existants dans la BDD

```
GET http://127.0.0.1:8000/api/categorie
```

## POST

> AJOUTER un service

```
POST http://127.0.0.1:8000/api/service/
content-type: application/json
Authorization: Bearer <Token>

{
    "contactrs": {
        "telephone": "<numero_de_telephone>",
        "mail": "<adresse_mail>",
        "skype": "<numero_skype>",
        "whatsapp": "<numero_watsapp>",
        "page_facebook": "<lien_page_facebook>"
    },
    "nom": "<nom_du_service>",
    "pdc": <fichier_image>,
    "description": "<description_du_service>",
    "adresse": "<adresse>",
    "quartier": "<quartier>",
    "active": false,
    "categorie": <id_categorie>,
    "classe": <id_classe>,
    "type_de_service": <id_type_de_service>,
    "proprietaire": <id_proprietaire>,
    "quartier_proche": [ids_quartier_proches]
}
```

> AJOUTER un categorie pour les services <br>
> NB : Cet action a besoin d'authentification de la super admin c-à-d seule la super admin la peut faire 

```
POST http://127.0.0.1:8000/api/categorie/
content-type: application/json
Authorization: Bearer <Token>

{
    "nom_categ": "<nom_du_categorie>"
}
```

> AJOUTER un MEDIA pour un service

```
POST http://127.0.0.1:8000/api/media/
content-type: application/json
Authorization: Bearer <Token>

{
    "media": <fichier>,
    "service": <id_service>
}
```

## PATCH

> MODIFER un service

```
PATCH http://127.0.0.1:8000/api/service/{id_service}
content-type: application/json
Authorization: Bearer <Token>

{
    les champs à modifier
}
```

> MODIFIER un categorie <br> 
> NB : Cet action a besoin d'authentification de la super admin c-à-d seule la super admin la peut faire 

```
PATCH http://127.0.0.1:8000/api/categorie/{id_categorie}
content-type: application/json
Authorization: Bearer <Token>

{
    les champs à modifier
}
```

> MODIFIER d'un MEDIA pour un service

```
PATCH http://127.0.0.1:8000/api/media/{id_media}
content-type: application/json
Authorization: Bearer <Token>

{
    les champs à modifier
}
```
## DELETE

> SUPPRIMER un service

```
DELETE http://127.0.0.1:8000/api/service/{id_service}
content-type: application/json
Authorization: Bearer <Token>
```

> SUPPRIMER un categorie <br> 
> NB : Cet action a besoin d'authentification de la super admin c-à-d seule la super admin la peut faire 

```
DELETE http://127.0.0.1:8000/api/categorie/{id_categorie}
content-type: application/json
Authorization: Bearer <Token>
```

> SUPPRIMER d'un MEDIA pour un service

```
PATCH http://127.0.0.1:8000/api/media/{id_media}
content-type: application/json
Authorization: Bearer <Token>

```
<br>

## CONTRIBUTEURS DE CE PROJET
![Image des contributeurs GitHub](https://contrib.rocks/image?repo=iTeam-S/Aiza-izy-zany)


<br>

## TECHNOLOGIES ET LANGAGES
<p><img height="100" src="https://github.com/iTeam-S/Ampalibe/raw/main/docs/source/_static/ampalibe_logo.png"/>
<img height="100" src="https://www.django-rest-framework.org/img/logo.png"/>
<img height="100" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png"/></p>
