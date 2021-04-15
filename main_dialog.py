from telegram.ext import ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from sqlalchemy import asc
from data_base.models import Skill, Course
from data_base.db import db_session
from texts import skill_text, welcome_text, trouble, trouble_desc
from utils import (
    get_study_options,
    order_choice_keyboard,
    skills_keyboard,
    study_options_keyboard,
    generate_courses_list,
)


def start_bot(update, context):
    update.message.reply_text(welcome_text, reply_markup=study_options_keyboard())
    return "skills"


def generate_skills(update, context):
    query = update.callback_query
    query.answer()
    study_option = update.callback_query.data

    trouble_keyboard = list(
        map(
            lambda item: [InlineKeyboardButton(text=item[1][0], callback_data=item[0])],
            trouble.items(),
        )
    )
    trouble_keyboard.append([InlineKeyboardButton("В начало", callback_data="skills")])
    if study_option in get_study_options():
        query.edit_message_text(
            text=skill_text, reply_markup=skills_keyboard(study_option)
        )
        return "order_choice"
    else:
        query.edit_message_text(
            text=trouble_desc, reply_markup=InlineKeyboardMarkup(trouble_keyboard)
        )
        return "troubles"


def troubles(update, context):
    query = update.callback_query
    query.answer()
    option = update.callback_query.data
    back = [[InlineKeyboardButton("Назад", callback_data="troubles")]]
    if option in trouble.keys():
        query.edit_message_text(
            text=trouble[option][1], reply_markup=InlineKeyboardMarkup(back)
        )
        return "skills"
    elif option == "skills":
        query.edit_message_text(
            text=welcome_text, reply_markup=study_options_keyboard()
        )
        return "skills"


# выбираем как ранжировать курсы
def choose_order(update, context):
    query = update.callback_query
    query.answer()
    context.user_data["skill"] = update.callback_query.data
    query.edit_message_text(
        "Как бы хотели ранжировать курсы?", reply_markup=order_choice_keyboard()
    )
    return "courses"


# вывод курсов на экран
def generate_courses(update, context):
    query = update.callback_query
    query.answer()
    order_choice = update.callback_query.data  # rating or cost
    skill_choice = context.user_data["skill"]

    res = (
        db_session.query(Skill.skill, Course)
        .filter_by(skill=skill_choice)
        .join(Course, Course.study_option_id == Skill.study_option_id)
        .order_by(asc(getattr(Course, order_choice)))
        .all()
    )

    res = " ".join([i for i in list(map(lambda x: str(*x[1:]) + "\n", res))])

    if query:
        query.edit_message_text(res)
        return ConversationHandler.END
    else:
        return ConversationHandler.END
