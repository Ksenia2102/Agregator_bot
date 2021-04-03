from telegram import ReplyKeyboardMarkup

from settings import SKILLS
from data_base.models import StudyOption, Skill
from data_base.db import db_session


def get_study_options():
    query_keyboard = StudyOption.query.all()
    if query_keyboard:
        study_options_list = []
        for option in query_keyboard:
            study_options_list.append(str(option))
    return study_options_list


def study_options_keyboard():
    return ReplyKeyboardMarkup(
        [get_study_options(), ['Затрудняюсь...']],
        one_time_keyboard=True, resize_keyboard=True
        )


def skills_keyboard(study_option_name):
    study_option = StudyOption.query.filter_by(study_option=study_option_name).first()
    skills = db_session.query(Skill.study_option_id, Skill.skill).filter(Skill.study_option_id == study_option.id)
    skill_keyboard = []
    for id_, skill in skills:
        skill_keyboard.append(skill)
    return ReplyKeyboardMarkup(
        [skill_keyboard], one_time_keyboard=True, resize_keyboard=True
    )
