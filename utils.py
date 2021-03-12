from telegram import KeyboardButton, ReplyKeyboardMarkup

def study_options_keybord():
    return ReplyKeyboardMarkup([['Программирование', 'Дизайн', 'Аналитика'], ['Затрудняюсь...']], one_time_keyboard=True, resize_keyboard=True)