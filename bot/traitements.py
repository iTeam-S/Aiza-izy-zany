import models as data
from ampalibe import Payload
from ampalibe.ui import QuickReply


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
    for i in range(len(categorie)):
        if data_categorie[i].get("id") in categorie:
            categorie_nom.append(data_categorie[i].get("nom_categ"))
        else:
            pass

    print(categorie_id)
    print(categorie)
    print(categorie_nom)

    quick_rep = []
    for i in range(len(categorie_nom)):
        quick_rep.append(
            QuickReply(
                title=categorie_nom[i].upper(),
                payload=Payload("/categorie", nom_categ=categorie[i]),
            )
        )

    return quick_rep
