from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from data_base.models import StudyOption, Skill, SkillRelation, Course
from data_base.db import db_session


def get_study_options():
    query_keyboard = StudyOption.query.all()
    if query_keyboard:
        study_options_list = []
        for option in query_keyboard:
            study_options_list.append(str(option))
    return study_options_list


def study_options_keyboard():
    keyboard = []
    for option in get_study_options():
        keyboard.append([InlineKeyboardButton(option, callback_data=option)])
    keyboard.append([InlineKeyboardButton('Затрудняюсь', callback_data='Go to description')])
    return InlineKeyboardMarkup(keyboard)


def skills_keyboard(study_option_name):
    study_option = StudyOption.query.filter_by(study_option=study_option_name).first()
    skills = db_session.query(Skill.study_option_id, Skill.skill).filter(Skill.study_option_id == study_option.id)
    skill_keyboard = []
    for id_, skill in skills:
        skill_keyboard.append([InlineKeyboardButton(skill, callback_data=skill)])
    return InlineKeyboardMarkup(skill_keyboard)

# WIP будущая функция генерации курсов 

# def generate_courses_list():
#     """
#     таблица 5
#     id навыка -> id курсов
#     таблица 1 
#     все курсы по нужному id 
#     order by cost или rating 
#     вывод 
#     Лучшие курсы  по направлению (название)
#     1. Имя курса, имя школы, стоимость, оценка, ссылка 
#     2. 
#     """

#     answer = 'Web-разработка'

#     skill = Skill.query.filter_by(skill=answer).first()
    
#     list_courses = SkillRelation.query.filter_by(skill.id == SkillRelation.skill_id)

#     print(list_courses)


# if __name__ == ('__main__'):
#     generate_courses_list()
