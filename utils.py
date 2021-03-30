from telegram import ReplyKeyboardMarkup

from settings import SKILLS
from data_base.models import StudyOption


STUDY_OPTIONS = StudyOption.query.all()

# СТАРАЯ КЛАВИАТУРАБ УДАЛЮ ВСКОРЕ 
# def study_options_keybord():
#     return ReplyKeyboardMarkup(
#         [STUDY_OPTIONS, ['Затрудняюсь...']],
#         one_time_keyboard=True, resize_keyboard=True
#         )


def study_options_keyboard(update, context):
    study_options_keyboard = [['default']]
    query_keyboard = StudyOption.query.all()
    if query_keyboard:
        study_options_keyboard = []
        for option in query_keyboard:
            study_options_keyboard.append(option)
    return ReplyKeyboardMarkup(
        [study_options_keyboard, ['Затрудняюсь...']],
        one_time_keyboard=True, resize_keyboard=True
        )


def skills_keyboard(study_option):
    skills = SKILLS[study_option]
    return ReplyKeyboardMarkup(
        [skills], one_time_keyboard=True, resize_keyboard=True
    )
