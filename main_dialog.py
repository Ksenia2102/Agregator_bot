from telegram.ext import ConversationHandler

from data_base.models import Skill
from texts import skill_text, welcome_text
from utils import (get_study_options, order_choice_keyboard, skills_keyboard,
                   study_options_keyboard, generate_courses_list)


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
        return 'order_choice'


# выбираем как ранжировать курсы
def choose_order(update, context):
    query = update.callback_query
    query.answer()
    context.user_data['skill'] = update.callback_query.data
    query.edit_message_text(
        'Как бы хотели ранжировать курсы?', reply_markup=order_choice_keyboard()
    )
    return 'courses'


# вывод курсов на экран 
def generate_courses(update, context):
    query = update.callback_query
    query.answer()
    order_choice = update.callback_query.data  # rating or cost
    skill_choice = context.user_data['skill'] 
    courses_list = generate_courses_list(order_choice, skill_choice)
    query.edit_message_text(courses_list)
    return ConversationHandler.END
