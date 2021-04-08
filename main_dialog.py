from telegram.ext import ConversationHandler

from texts import welcome_text, skill_text
from utils import skills_keyboard, study_options_keyboard, get_study_options
from data_base.models import Skill


def start_bot(update, context):
    update.message.reply_text(
        welcome_text, reply_markup=study_options_keyboard()
        )
    return 'skills'


def generate_skills(update, context):
    query = update.callback_query
    query.answer()
    study_option = update.callback_query.data
    if study_option in get_study_options():
        query.edit_message_text(text=skill_text, reply_markup=skills_keyboard(study_option))
        return 'courses'


# WIP будущая функция развилки по цене и рейтингу
# def choose_order(update, context):
#     user_choice = context.user_data
#     # вызов функции генерации
#     return ConversationHandler.END
     

# def generate_courses_list(update, context):
#     skill = context.user_data
#     if skill in Skill.query.all():
#         update.message.reply_text(
#             f'ЗДЕСЬ БУДЕТ СПИСОК КУРСОВ ПО {skill}'
#             )
#         return ConversationHandler.END