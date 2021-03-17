from db import db_session # добавление записи в базу данных Основная
from models import Main

first=Main(direction=3, course_name='Курс Веб-аналитика', school_name=1, the_cost=35000, appraisal= 4.1,link='https://imba.ru/course/web-analytics?utm_medium=referral&utm_source=tutortop.ru&utm_campaign=partner')

#second=direct(direction='Аналитика')
#three=The_skill(skill='Машинное обучение')
#four=The_Scholl(scholl='Convert Monster')
#five = The_difinition_of_skill(course_name=1,skill=2) - Не работает 

db_session.add(five)
db_session.commit()