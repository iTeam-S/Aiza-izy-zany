import const
import ampalibe
import traitements as trt
from conf import Configuration

bot = ampalibe.init(Configuration())
chat = bot.chat

# # create a get started option to get permission of user.
# bot.chat.get_started(payload="/get_started")


@ampalibe.command("/get_started")
def get_started(sender_id, **extends):
    chat.send_message(sender_id, const.salutation_information)
    chat.send_media(sender_id, const.url_logo, "image")
    chat.send_quick_reply(
        sender_id, trt.quick_rep_principal, const.text_quick_principal
    )


@ampalibe.command("/")
def main(sender_id, cmd, **extends):
    chat.send_quick_reply(
        sender_id, trt.quick_rep_principal, const.text_quick_principal
    )


@ampalibe.command("/rechercher")
def rechercher(sender_id, **extends):
    # Algo de recherche est ici
    chat.send_message(sender_id, "bientot la recherche")


@ampalibe.command("/voir_tout")
def voir_tout(sender_id, **extends):
    chat.send_quick_reply(sender_id, trt.quick_rep_classement, const.text_quick_service)


@ampalibe.command("/formelle")
def formelle(sender_id, **extends):
    chat.send_quick_reply(
        sender_id,
        trt.quick_type_service(type_de_service="formelle"),
        const.text_quick_categorie,
        next="Voir plus",
    )

@ampalibe.command("/informelle")
def formelle(sender_id, **extends):
    chat.send_quick_reply(
        sender_id,
        trt.quick_type_service(type_de_service="informelle"),
        const.text_quick_categorie,
        next="Voir plus",
    )
