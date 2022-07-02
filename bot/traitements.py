import random
import models as data
from ampalibe import Payload
from conf import Configuration
from ampalibe.ui import QuickReply, Element, Button


quick_rep_principal = [
    QuickReply(
        title="RECHERCHER",
        image_url="https://i.ytimg.com/vi/_NltVXqwGQw/maxresdefault.jpg",
        payload="/rechercher",
    ),
    QuickReply(
        title="VOIR TOUT",
        image_url="https://thumbs.dreamstime.com/z/style-plat-d-ic%C3%B4ne-de-yeux-logo-isolement-sur-le-fond-illustrations-vecteur-133373134.jpg",
        payload="/voir_tout",
    ),
]

quick_rep_classement = [
    QuickReply(
        title="FORMELLE",
        image_url="https://img.freepik.com/vecteurs-libre/logo-vectoriel-symbole-smoking-hommes-mafieux-noirs_557439-2630.jpg?w=2000",
        payload="/formelle",
    ),
    QuickReply(
        title="INFORMELLE",
        image_url="https://c8.alamy.com/compfr/2cy13rd/message-d-accueil-informel-poignee-de-main-abstract-vector-ensemble-de-modeles-de-signature-d-embleme-ou-de-logo-icone-de-lettrage-de-la-fraternite-ou-de-l-equipe-sympathique-main-de-cinq-palmes-2cy13rd.jpg",
        payload="/informelle",
    ),
]

quick_retoure_type_de_service = [
    QuickReply(
        title="TYPE DE SERVICE",
        image_url="https://thumbs.dreamstime.com/z/repair-service-logo-design-repair-service-logo-design-166728199.jpg",
        payload="/retoure_type_service",
    ),
    QuickReply(
        title="MENUS PRINCIPAUX",
        image_url="https://png.pngtree.com/png-clipart/20190614/original/pngtree-menu-vector-icon-png-image_3791388.jpg",
        payload="/",
    ),
]


def quick_type_service(type_de_service):

    data_service = data.get_data_type_de_service(type_de_service)
    if not data_service:
        return f"Pas de service {type_de_service.upper()} disponible pour le moment"

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

    quick_rep = []
    for i in range(len(categorie_nom)):
        quick_rep.append(
            QuickReply(
                title="🟣 " + categorie_nom[i].upper(),
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
                title=f"🟪 {data_service[i].get('nom').upper()} 🟪",
                subtitle=f"🏠 DOMICILE : {data_service[i].get('quartier')} 🏠",
                image_url=f"{Configuration.APP_URL}/{'/'.join(data_service[i].get('pdc').split('/')[-2:])}",
                buttons=[
                    Button(
                        type="postback",
                        title="💠DESCRIPTION💠",
                        payload=Payload(
                            "/description", service_id=data_service[i].get("id")
                        ),
                    ),
                    Button(
                        type="postback",
                        title="☎️CONTACTS☎️",
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
    return f"\t\tVOICI NOS CONTACTS\n\n☎️Numero : {_data.get('telephone')}\n\
{'📩Email : ' + _data.get('mail') if _data.get('mail') else ''}\n\
{'📱Skype : ' + _data.get('skype') if _data.get('skype') else ''}\n\
{'📲Whatsapp : ' + _data.get('whatsapp') if _data.get('whatsapp') else ''}\n\
{'📃Page facebook : ' + _data.get('page_facebook') if _data.get('page_facebook') else ''}\n\n\
🏘️Adresse : {_data.get('adresse')}"


def retoure_au_categorie(type_de_service):
    return [
        QuickReply(
            title="RETOUR",
            image_url="https://www.brockeur.com/img/cms/previous-black.png",
            payload=f"/{type_de_service}",
        )
    ]
