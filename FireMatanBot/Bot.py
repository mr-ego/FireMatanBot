from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Database import Database
import telegram
import logging
import datetime


class Bot:

    def __init__(self):
        self.updater = Updater(token='598802718:AAFFg2u5VRPbc5HyOmzZxEUIkWXMABXLbvU')
        self.bot = telegram.Bot(token='598802718:AAFFg2u5VRPbc5HyOmzZxEUIkWXMABXLbvU')
        self.dispatcher = self.updater.dispatcher
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

        start_handler = CommandHandler('start', self.start)
        set_handler = CommandHandler('set', self.set_feierwehr, pass_args=True)
        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(set_handler)

        self.updater.start_polling()

    def start(self, bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Bitte benutze /set <Feuerwehr>")

    def set_feierwehr(self, bot, update, args):
        chat_id = update.message.chat_id
        feierwehr = ""
        for x in range(len(args)):
            feierwehr += args[x]
            if not (len(args) == 0 or x == len(args)-1):
                feierwehr += " "
        db = Database()
        try:
            db.insert(chat_id, feierwehr)
        except:
            db.update(chat_id, feierwehr)
        bot.send_message(chat_id=update.message.chat_id, text="Erfolgreich gesetzt")

    def send_notification(self, data):
        message = "Einsatz Feuerwehr %s %s. %s mit Alarmstufe %s. Einsatzzeit: %s; Sendezeit: %s" % (data['feuerwehr'], data['nummer'], data['art'], data['alarmstufe'], data['zeit'], datetime.datetime.now().time())
        db = Database()
        users = db.get_id(data['feuerwehr'])
        for user in users:
            self.bot.send_message(chat_id=user[0], text=message)
            print("Message sent:", user)

    def update(self, data):
        self.send_notification(data)





