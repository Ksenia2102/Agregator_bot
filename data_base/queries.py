from models import StudyOption, Skill
from db import db_session




study_option = StudyOption.query.filter_by(study_option=answer).first()
print(study_option.id)


res = db_session.query(Skill.study_option_id, Skill.skill)

skill_keyboard = []
for id_, skill in res:
    if id_ == study_option.id:
        skill_keyboard.append(skill)

print(skill_keyboard)
