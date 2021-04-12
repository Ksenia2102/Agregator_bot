from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from sqlalchemy.orm import joinedload

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


# клава для выбора ранжирования
def order_choice_keyboard():
    keyboard = [
        [InlineKeyboardButton('По стоимости', callback_data='cost')],
        [InlineKeyboardButton('По рейтингу', callback_data='rating')]
    ]
    return InlineKeyboardMarkup(keyboard)


# генерация списка курсов из базы
def generate_courses_list(order_choice, skill_choice):
    skill = Skill.query.filter_by(skill=skill_choice).first()

    # фильтруем курсы по таблице SkillRelation
    filtered_courses_id = SkillRelation.query.filter(SkillRelation.skill_id == skill.id).all()
    courses_id_list = [c.course_id for c in filtered_courses_id]

    # в зависимости от пролетевшего выбора от пользователя ранжируем курсы
    if order_choice == 'cost':
        courses_list = db_session.query(Course).filter(Course.id.in_(courses_id_list)).order_by(Course.cost).options(joinedload(Course.school_info)).all()
    elif order_choice == 'rating':
        courses_list = db_session.query(Course).filter(Course.id.in_(courses_id_list)).order_by(Course.rating.desc()).options(joinedload(Course.school_info)).all()

    return '\n'.join([str(c) for c in courses_list])


if __name__ == ('__main__'):
    generate_courses_list()
