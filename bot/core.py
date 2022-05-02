import ampalibe
from conf import Configuration

bot = ampalibe.init(Configuration())
chat = bot.chat

# create a get started option to get permission of user.
# bot.chat.get_started()

@ampalibe.command('/')
def main(sender_id, cmd, **extends):
    chat.send_message(sender_id, "Hello BOT-SERVICE")
    
