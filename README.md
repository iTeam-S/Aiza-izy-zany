# BOT SERVICE

## Documentation de toutes les APIs

## REGISTER POUR les propriétaires du service
```
POST <host>/api/register/
content-type: application/json

{
    "first_name": "<nom | string | required>",
    "last_name": "<prenom | string | required>",
    "cin": "<numero cin | string | required>",
    "adresse": "<adresse exacte | string | required>",
    "num": "<numero du telephone | string | required>",
    "email": "<email | email | required>",
    "password": "<password | string | required>",
    "password2": "<confirm password | string | required>",
}
```

## LOGIN 
```
POST <host>/api/login/
content-type: application/json

{
    "email": "<son email>",
    "password": "<son password>"
}

```
## GET

> GET tout les services FORMELS et ACTIVES <br>
> NB: Dans la BDD, l'id de type du service FORMEL est obligatoirement 1

```
GET <host>/api/service/?type_de_service=1&active=true
```

> GET tout les services INFORMELS et ACTIVES  <br>
> NB: Dans la BDD, l'id de type du service INFORMEL est obligatoirement 2

```
GET <host>/api/service/?type_de_service=2&active=true
```
> GET tout les services d'un categorie dans un type de service [informel ou formelle] et actives

```
GET <host>/api/service/?categorie={id_categorie}&type_de_service={id_type_de_service}&active=true
```

>GET toutes les informations concernant un seul service

```
GET <host>/api/service/{service_id}
```
> GET tout les services recherché à partir d'un mot clé

```
GET <host>/api/service/?search={mot_cle}&active=true
```
> GET tout les services filtrés par sa classe [chaque service est classé de l'un de ces trois classes qui sont GOLD, MEDIUM et LESS. Alors dans la BDD ces derniers ont l'id respectivement 1,2 et 3

```
GET <host>/api/service/?classe={id_classe}&active=true
```
> GET tous les categories existants dans la BDD

```
GET <host>/api/categorie
```
> GET tous les classement existants de service dans la BDD

```
GET <host>/api/classement
```
> GET tous les types de services existants dans la BDD

```
GET <host>/api/typedeservice
```
## POST

> AJOUTER un service

```
POST <host>/api/service/
content-type: application/json
Authorization: Bearer <Token>

{
    "nom": "<nom_du_service | string | required>",
    "pdc": <fichier_image | file | required>,
    "description": "<description_du_service | string | required>",
    "adresse": "<adresse | string | required>",
    "quartier": "<quartier | string | required>",
    "telephone": "<numero_de_telephone | string | required>",
    "mail": "<adresse_mail | string | not required>",
    "skype": "<numero_skype | string | not required>",
    "whatsapp": "<numero_watsapp | string | not required>",
    "page_facebook": "<lien_page_facebook | url | not required>",
    "active": <Bool | default=false>,
    "categorie": <id_categorie | integer | required>,
    "classe": <id_classe | integer | required>,
    "type_de_service": <id_type_de_service | integer | required>,
    "proprietaire": <id_proprietaire | integer | required>,
}
```

> AJOUTER un categorie pour les services <br>
> NB : Cet action a besoin d'authentification de la super admin c-à-d seule la super admin la peut faire 

```
POST <host>/api/categorie/
content-type: application/json
Authorization: Bearer <Token>

{
    "nom_categ": "<nom_du_categorie>"
}
```

> AJOUTER un MEDIA pour un service

```
POST <host>/api/media/
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
PATCH <host>/api/service/{id_service}
content-type: application/json
Authorization: Bearer <Token>

{
    les champs à modifier
}
```

> MODIFIER un categorie <br> 
> NB : Cet action a besoin d'authentification de la super admin c-à-d seule la super admin la peut faire 

```
PATCH <host>/api/categorie/{id_categorie}
content-type: application/json
Authorization: Bearer <Token>

{
    les champs à modifier
}
```

> MODIFIER d'un MEDIA pour un service

```
PATCH <host>/api/media/{id_media}
content-type: application/json
Authorization: Bearer <Token>

{
    les champs à modifier
}
```
## DELETE

> SUPPRIMER un service

```
DELETE <host>/api/service/{id_service}
content-type: application/json
Authorization: Bearer <Token>
```

> SUPPRIMER un categorie <br> 
> NB : Cet action a besoin d'authentification de la super admin c-à-d seule la super admin la peut faire 

```
DELETE <host>/api/categorie/{id_categorie}
content-type: application/json
Authorization: Bearer <Token>
```

> SUPPRIMER d'un MEDIA pour un service

```
DELETE <host>/api/media/{id_media}
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
