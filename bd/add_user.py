from db import db_session # добавление записи в базу данных Основная
from models import DifinitionOfSkill

#first=Courses(direction=3, course_name='Курс Веб-аналитика', school_name=11, the_cost=38000, appraisal= 4.2,link='https://imba.ru/course/web-analytics?utm_medium=referral&utm_source=tutortop.ru&utm_campaign=partner')

#second=Direction(flow='Аналитика')
#three=Skill(knowledge='Машинное обучение') 
#four=Scholl(scholl='Convert Monster')
five =DifinitionOfSkill(course_name=1,skill=2) #Не работает 

db_session.add(five)
db_session.commit()