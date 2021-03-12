from utils import study_options_keybord


welcome_text = '''Привет! Выбери направление, которое ты хотел бы изучить.
Если тебе трудно определиться, нажми кнопку "Затрудняюсь..." и мы поподробней расскажем о каждом из направлений.'''

def start_bot(update,context):
    update.message.reply_text(welcome_text, reply_markup=study_options_keybord())
