import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import Message, User


class JCBMessenger(object):
    listener_ids = ['-256959090']

    def __init__(self):
        self.updater = Updater(token='587631567:AAEGhOU3lHiwSimyx8qdMYwQ-wG0vhEnGqU')
        self.bot = telegram.Bot(token='587631567:AAEGhOU3lHiwSimyx8qdMYwQ-wG0vhEnGqU')
        self.setup_handler()
        self.updater.start_polling()

    @property
    def dispatcher(self):
        return self.updater.dispatcher

    def setup_handler(self):
        start_handler = CommandHandler('start', self.start_handler)
        self.dispatcher.add_handler(start_handler)

        add_handler = CommandHandler('add', self.add)
        self.dispatcher.add_handler(add_handler)

    def send_text(self, text):
        if not text or len(text) == 0:
            return

        for chat_id in self.listener_ids:
            self.bot.send_message(chat_id=chat_id, text=text)

    @staticmethod
    def start_handler(bot, update):
        msg = update.message  # type: Message

        if msg:
            bot.send_message(chat_id=update.message.chat_id, text="Hi {}, 你好! 我是機器人".format(msg.from_user.username))

    def add(self, bot, update):
        user = update.message.from_user  # type: User
        new_chat_id = update.message.chat_id

        if not any(new_chat_id in self.listener_ids):
            self.listener_ids.append(new_chat_id)
            bot.send_message(chat_id=new_chat_id, text="感謝您的加入 {}, 有任何最新變化，都會告訴你喲".format(user.username))
        else:
            bot.send_message(chat_id=new_chat_id, text="{} 您已經加入了".format(user.username))

    pass
