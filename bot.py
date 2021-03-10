import logging
import settings
from telegram.ext import Updater,CommandHandler

logging.basicConfig(filename = 'bot.log',level = logging.INFO)


def start_user(update,context):
    print('Вызван /start')
    update.message.reply_text(f'Здравствуй пользователь!')

def main():
    mybot = Updater(settings.API_KEY,use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',start_user))

    logging.info('Бот стартовал')


    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()

