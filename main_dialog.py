from telegram.ext import ConversationHandler

from settings import STUDY_OPTIONS, SKILLS
from texts import welcome_text
from utils import study_options_keybord, skills_keyboard


def start_bot(update, context):
    update.message.reply_text(
        welcome_text, reply_markup=study_options_keybord()
        )
    return 'skills'


def generate_skills(update, context):
    study_option = update.message.text
    if study_option in STUDY_OPTIONS:
        update.message.reply_text(
            'Выберите навык, который хотите изучить.',
            reply_markup=skills_keyboard(study_option))
        return 'courses'


def generate_courses(update, context):
    course_name = update.message.text
    print(SKILLS.values())
    for skills in SKILLS.values():
        if course_name in skills:
            update.message.reply_text(
                f'ЗДЕСЬ БУДЕТ СПИСОК КУРСОВ ПО {course_name}'
                )
            return ConversationHandler.END
