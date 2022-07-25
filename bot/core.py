import const
import ampalibe
import traitements as trt
from conf import Configuration
from ampalibe.ui import QuickReply

bot = ampalibe.init(Configuration())
chat = bot.chat
query = bot.query

# create a get started option to get permission of user.
# bot.chat.get_started(payload="/get_started")


@ampalibe.command("/get_started")
def get_started(sender_id, **extends):
    chat.send_action(sender_id, "mark_seen")
    chat.send_message(sender_id, const.salutation_information)
    chat.send_media(sender_id, const.url_logo, "image")
    chat.send_quick_reply(
        sender_id, trt.quick_rep_principal, const.text_quick_principal
    )
    chat.persistent_menu(sender_id, const.persistent_menu, action="PUT")


@ampalibe.command("/")
def main(sender_id, cmd, **extends):
    chat.send_action(sender_id, "mark_seen")
    chat.send_quick_reply(
        sender_id, trt.quick_rep_principal, const.text_quick_principal
    )


@ampalibe.command("/rechercher")
def rechercher(sender_id, **extends):
    # Algo de recherche est ici
    chat.send_action(sender_id, "mark_seen")
    query.set_action(sender_id, "recherche")
    chat.send_message(sender_id, const.recherche)


@ampalibe.command("/voir_tout")
def voir_tout(sender_id, **extends):
    chat.send_action(sender_id, "mark_seen")
    chat.send_quick_reply(sender_id, trt.quick_rep_classement, const.text_quick_service)


@ampalibe.command("/formelle")
def formelle(sender_id, **extends):
    chat.send_action(sender_id, "mark_seen")
    quick_rep = trt.quick_type_service(type_de_service="formelle")

    if isinstance(quick_rep, list) and isinstance(quick_rep[0], QuickReply):
        chat.send_quick_reply(
            sender_id,
            quick_rep,
            const.text_quick_categorie,
            next="Voir plus",
        )
    else:
        chat.send_message(sender_id, quick_rep)


@ampalibe.command("/informelle")
def formelle(sender_id, **extends):
    chat.send_action(sender_id, "mark_seen")
    quick_rep = trt.quick_type_service(type_de_service="informelle")

    if isinstance(quick_rep, list) and isinstance(quick_rep[0], QuickReply):
        chat.send_quick_reply(
            sender_id,
            quick_rep,
            const.text_quick_categorie,
            next="Voir plus",
        )
    else:
        chat.send_message(sender_id, quick_rep)


@ampalibe.command("/tout")
def tout_les_produits(sender_id, **extends):
    chat.send_message(sender_id, "Voici donc tout les services disponibles")
    chat.send_template(sender_id, trt.tout_les_produits(), next="Voir plus")


@ampalibe.command("/categorie")
def resultat_de_categorie(sender_id, type_de_service, nom_categ, **extends):
    chat.send_action(sender_id, "mark_seen")
    if type_de_service and type_de_service == "formelle":
        chat.send_template(
            sender_id,
            trt.template_service(1, nom_categ),
            quick_rep=trt.retoure_au_categorie(type_de_service),
            next=True,
        )
    else:
        chat.send_template(
            sender_id,
            trt.template_service(2, nom_categ),
            quick_rep=trt.retoure_au_categorie(type_de_service),
            next=True,
        )


@ampalibe.command("/description")
def description(sender_id, service_id, **extends):
    chat.send_action(sender_id, "mark_seen")
    chat.send_message(sender_id, trt.description(service_id))
    chat.send_quick_reply(sender_id, trt.quick_retoure_type_de_service, const.retoure)


@ampalibe.command("/contact")
def contact(sender_id, service_id, **extends):
    chat.send_action(sender_id, "mark_seen")
    chat.send_message(sender_id, trt.contact(service_id))
    chat.send_quick_reply(sender_id, trt.quick_retoure_type_de_service, const.retoure)


@ampalibe.action("recherche")
def recherche(sender_id, cmd, **extends):
    chat.send_action(sender_id, "mark_seen")

    if trt.recherche(cmd):
        chat.send_message(sender_id, const.phrase_recherche)
        chat.send_template(sender_id, trt.recherche(cmd), next="Voir plus")
        query.set_action(sender_id, None)
        return True

    chat.send_message(sender_id, const.pas_de_donnees_recherche)
    chat.send_quick_reply(
        sender_id, trt.quick_rep_principal, const.text_quick_principal
    )
    query.set_action(sender_id, None)


@ampalibe.command("/retoure_type_service")
def retoure(sender_id, **extends):
    chat.send_action(sender_id, "mark_seen")
    chat.send_quick_reply(sender_id, trt.quick_rep_classement, const.text_quick_service)


@ampalibe.command("/information")
def information(sender_id, **extends):
    chat.send_action(sender_id, "mark_seen")
    chat.send_message(sender_id, const.salutation_information)
    chat.send_quick_reply(sender_id, trt.quick_retoure_type_de_service, const.retoure)
