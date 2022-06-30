import random
import models as data
from ampalibe import Payload
from conf import Configuration
from ampalibe.ui import QuickReply, Element, Button


quick_rep_principal = [
    QuickReply(
        title="RECHERCHER",
        payload="/rechercher",
    ),
    QuickReply(
        title="VOIR TOUT",
        payload="/voir_tout",
    ),
]

quick_rep_classement = [
    QuickReply(
        title="FORMELLE",
        payload="/formelle",
    ),
    QuickReply(
        title="INFORMELLE",
        payload="/informelle",
    ),
]


def quick_type_service(type_de_service):

    data_service = data.get_data_type_de_service(type_de_service)
    data_categorie = data.get_categorie()

    categorie_id = []
    for i in range(len(data_categorie)):
        categorie_id.append(data_categorie[i].get("id"))

    categorie = []
    for i in range(len(data_service)):
        if data_service[i].get("categorie") in categorie_id:
            if data_service[i].get("categorie") not in categorie:
                categorie.append(data_service[i].get("categorie"))
            else:
                pass
        else:
            pass

    categorie_nom = []
    for i in range(len(data_categorie)):
        if data_categorie[i].get("id") in sorted(categorie):
            categorie_nom.append(data_categorie[i].get("nom_categ"))
        else:
            pass

    print(categorie_id)
    print(sorted(categorie))
    print(categorie_nom)

    quick_rep = []
    for i in range(len(categorie_nom)):
        quick_rep.append(
            QuickReply(
                title=categorie_nom[i].upper(),
                payload=Payload(
                    "/categorie",
                    type_de_service=type_de_service,
                    nom_categ=categorie[i],
                ),
            )
        )
    return quick_rep


def template(data_service):
    list_items = []
    for i in range(len(data_service)):
        list_items.append(
            Element(
                title=data_service[i].get("nom").upper(),
                subtitle=f"DOMICILE : {data_service[i].get('quartier')}",
                image_url=f"{Configuration.APP_URL}/{'/'.join(data_service[i].get('pdc').split('/')[-2:])}",
                buttons=[
                    Button(
                        type="postback",
                        title="DESCRIPTION",
                        payload=Payload(
                            "/description", service_id=data_service[i].get("id")
                        ),
                    ),
                    Button(
                        type="postback",
                        title="CONTACTS",
                        payload=Payload(
                            "/contact", service_id=data_service[i].get("id")
                        ),
                    ),
                ],
            )
        )

    return list_items


def template_service(type_de_service, nom_categ):
    data_service = data.get_service(type_de_service, nom_categ)
    return template(data_service)


def recherche(mot_cle):
    _data = data.recherche(mot_cle)

    classe = random.choice(range(1, 3))
    _data_super_classe = data.super_class(classe)

    if _data:
        return template(_data)
    return template(random.sample(_data_super_classe, 3))


def description(service_id):
    return data.get_info_service(service_id).get("description")


def contact(service_id):
    _data = data.get_info_service(service_id)
    return f"\t\tVOICI NOS CONTACTS\n\nNumero : {_data.get('contactrs').get('telephone')}\n\
{'Email : ' + _data.get('contactrs').get('mail') if _data.get('contactrs').get('mail') else ''}\n\
{'Skype : ' + _data.get('contactrs').get('skype') if _data.get('contactrs').get('skype') else ''}\n\
{'Whatsapp : ' + _data.get('contactrs').get('whatsapp') if _data.get('contactrs').get('whatsapp') else ''}\n\
{'Page facebook : ' + _data.get('contactrs').get('page_facebook') if _data.get('contactrs').get('page_facebook') else ''}\n\n\
Adresse : {_data.get('adresse')}"
