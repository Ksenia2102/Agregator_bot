from telegram import ReplyKeyboardMarkup

from settings import SKILLS, STUDY_OPTIONS


def study_options_keybord():
    return ReplyKeyboardMarkup(
        [STUDY_OPTIONS, ['Затрудняюсь...']],
        one_time_keyboard=True, resize_keyboard=True # one time - клавитура проподает,resize-маштаб эстетитка 
        )


def skills_keyboard(study_option):
    skills = SKILLS[study_option]
    return ReplyKeyboardMarkup(
        [skills], one_time_keyboard=True, resize_keyboard=True
    )
