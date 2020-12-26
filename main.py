from telegram.ext import Updater

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    print(update.effective_chat.id)
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

from telegram.ext import CommandHandler

def echo(update, context):
    print(update.message.text, update.effective_chat.id)
    m = context.bot.send_copy(chat_id=update.effective_chat.id, from_chat_id="@kurdio20",  message_id=9)
    # m['forward_from_chat'] = None
    # m.forward(chat_id=update.effective_chat.id)
from telegram.ext import MessageHandler, Filters


# def unknown(update, context):
#     context.bot.forwardMessage(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == "__main__":
    token = ENV['bot_token']
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    echo_handler = CommandHandler("forward", echo)
    dispatcher.add_handler(echo_handler)
    # unknown_handler = MessageHandler(Filters.command, unknown)
    # dispatcher.add_handler(unknown_handler)

    updater.start_polling()
