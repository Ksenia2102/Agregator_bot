from texts import welcome_text
from utils import study_options_keybord


def start_bot(update,context):
    update.message.reply_text(welcome_text, reply_markup=study_options_keybord())
