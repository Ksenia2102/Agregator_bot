import logging

from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater)

from config import PROXY_URL, PROXY_USERNAME, PROXY_PASSWORD, API_KEY
from .main_dialog import generate_courses, start_bot, keyboard

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {
    'proxy_url': PROXY_URL,
    'urllib3_proxy_kwargs':
        {'username': PROXY_USERNAME,
         'password': PROXY_PASSWORD}
        }


def create_app():
    mybot = Updater(API_KEY, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher

    # Основная линия диалога с пользователем
    main_dialog = ConversationHandler(
        entry_points=[CommandHandler('start', start_bot)], #точка из которой стартует Converstation 
        states={
            #'skills': [MessageHandler(Filters.text, generate_skills)],
           # 'courses': [MessageHandler(Filters.text, generate_courses)],
            'test':[MessageHandler(Filters.text, keyboard)]
        },
        fallbacks=[]
    )

    dp.add_handler(main_dialog)

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
