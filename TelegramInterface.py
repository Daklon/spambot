import logging

from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from Caller import Caller

class TelegramInterface:
    def __init__(self, token, admin_id):
        self.token = token
        self.admin_id = admin_id

        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        self.start_handler = CommandHandler('start', self.start)
        self.spam_handler = MessageHandler(Filters.regex('^[0-9]{9}$'), self.spam)
        self.incorrect_handler = MessageHandler(Filters.regex('.*'), self.incorrect)
    
        self.dispatcher.add_handler(self.start_handler)
        self.dispatcher.add_handler(self.spam_handler)
        self.dispatcher.add_handler(self.incorrect_handler)

        self.updater.start_polling()
        self.caller = Caller()

    def check_permissions(self, update):
        if update.message.from_user.id == self.admin_id:
            return True
        else:
            logging.error("non admin user trying to log in:" + update.message.text)
            return False

    def start(self, update: Update, context: CallbackContext):
        if self.check_permissions(update):
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="I'm a bot, please talk to me!")

    def incorrect(self, update: Update, context: CallbackContext):
        if self.check_permissions(update):
            context.bot.send_message(chat_id=update.effective_chat.id, text='Wrong number')

    def spam(self, update: Update, context: CallbackContext):
        if self.check_permissions(update):
            message = "Calling to "+ update.message.text + " Using Génesis"
            logging.info(message)
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            self.caller.call_genesis(update.message.text)

