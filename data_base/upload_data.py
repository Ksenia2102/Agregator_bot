import csv
import random

from db import db_session
from models import Course, School, Skill, StudyOption, SkillRelation


def read_data(filename, fields):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, fields, delimiter=';')
        data = []
        for row in reader:
            data.append(row)
        return data


def upload_study_options(data):
    all_study_options = []
    for row in data:
        study_option = {
            'study_option': row['study_option']
        }
        all_study_options.append(study_option)
    db_session.bulk_insert_mappings(StudyOption, all_study_options, return_defaults=True)
    db_session.commit()


def upload_skills(data):
    all_skills = []
    for row in data:
        list_of_skills = row['skills'].split(',')
        for skill in list_of_skills:
            each_skill = {
                'skill': skill
            }
            all_skills.append(each_skill)
    db_session.bulk_insert_mappings(Skill, all_skills, return_defaults=True)
    db_session.commit()


def upload_schools(data):
    all_schools = []
    for row in data:
        school = {
            'school_name': row['school']
        }
        all_schools.append(school)
    db_session.bulk_insert_mappings(School, all_schools, return_defaults=True)
    db_session.commit()


def upload_skills_relations(num):
    relation_data = generate_skills_relations(num)
    db_session.bulk_insert_mappings(SkillRelation, relation_data, return_defaults=True)
    db_session.commit()


def upload_courses(num):
    course_data = generate_course_data(num)
    db_session.bulk_insert_mappings(Course, course_data, return_defaults=True)
    db_session.commit()


def generate_skills_relations(num_rows):
    all_data = []
    for row in range(num_rows):
        relation = {
            'course_id': random.randint(15, 44),
            'skill_id': random.randint(19, 33)
        }
        all_data.append(relation)
    return all_data


def generate_course_data(num_rows):
    all_data = []
    for row in range(num_rows):
        course = {
            'study_option_id': random.randint(4, 6),
            'course_name': 'Название курса',
            'school': random.randint(1, 15),
            'cost': random.randint(20000, 200000),
            'rating': round(random.uniform(1, 5), 1),
            'link': 'Ccылка'
        }
        all_data.append(course)
    return all_data


if __name__ == "__main__":
    # study_options_and_skills_data = read_data('study_options_and_skills.csv', ['study_option', 'skills'])
    # upload_study_options(study_options_and_skills_data)
    # upload_skills(study_options_and_skills_data)
    # schools_data = read_data('schools.csv', ['school'])
    # upload_schools(schools_data)
    # upload_skills_relations(30)
