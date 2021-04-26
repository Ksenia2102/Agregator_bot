import logging

from telegram.ext import (CallbackQueryHandler, CommandHandler,
                          ConversationHandler, Filters, MessageHandler,
                          Updater)

import settings
from main_dialog import (choose_order, generate_courses, generate_skills,
                         get_troubles, start_bot)

logging.basicConfig(filename="bot.log", level=logging.INFO)

PROXY = {
    "proxy_url": settings.PROXY_URL,
    "urllib3_proxy_kwargs": {
        "username": settings.PROXY_USERNAME,
        "password": settings.PROXY_PASSWORD,
    },
}


def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher

    # Основная линия диалога с пользователем
    main_dialog = ConversationHandler(
        entry_points=[CommandHandler("start", start_bot)],
        states={
            "skills": [CallbackQueryHandler(generate_skills)],
            "order_choice": [CallbackQueryHandler(choose_order)],
            "courses": [CallbackQueryHandler(generate_courses)],
            "troubles": [CallbackQueryHandler(get_troubles)]
        },
        fallbacks=[],
    )

    dp.add_handler(main_dialog)

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
