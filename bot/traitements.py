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

    liste_data = data.get_data_type_de_service(type_de_service)
    categorie = []
    quick_rep = []

    for i in range(0, len(liste_data)):
        element = liste_data[i].get("categorie")["nom_categ"]
        if element not in categorie:
            categorie.append(element)
        else:
            pass

    for i in range(len(categorie)):
        quick_rep.append(
            QuickReply(
                title=categorie[i].upper(),
                payload=Payload("/categorie", nom_categ=categorie[i]),
            )
        )

    return quick_rep

