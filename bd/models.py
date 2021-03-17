from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db import Base, engine


class Direction(Base): # 2 . направление
    __tablename__ = 'dire' # когда меняешь имя меняется и таблица
    id = Column(Integer, primary_key=True) # primary первичный ключ 
    flow = Column(String) # течение

    def __repr__(self):
        return f"User {self.flow}"

class Skill(Base): #3
    __tablename__ = 'experience' # (опыт) когда меняешь имя меняется и таблица
    id = Column(Integer, primary_key=True) # primary первичный ключ 
    knowledge = Column(String) # перевод знания
    
    def __repr__(self):
        return f"User {self.knowledge}"

class Scholl(Base): #4
    __tablename__ = 'studio'
    id = Column(Integer, primary_key=True) # primary первичный ключ 
    scholl = Column(String) # школа

    def __repr__(self):
        return f"User {self.school}"

class DifinitionOfSkill(Base): #5
    __tablename__ = 'skillratio' # соотношение навыков
    id = Column(Integer, primary_key=True)
    course_name = Column(Integer,ForeignKey('coursetable.id'), index=True, nullable=False)
    skill = Column(Integer,ForeignKey('experience.id'), index=True, nullable=False)
     
    def __repr__(self):
        return f"User {self.course_name},{self.skill}"

class Courses(Base): #1
    __tablename__ = 'coursetable' # когда меняешь имя меняется и таблица
    id = Column(Integer, primary_key=True) # primary первичный ключ 
    direction = Column(Integer,ForeignKey('dire.id'), index=True, nullable=False) # направление
    course_name = Column(String) #название курсов
    school_name = Column(Integer,ForeignKey('studio.id'), index=True, nullable=False) #имя школы
    the_cost = Column(Integer) # стоимость
    appraisal = Column(Float) # оценка
    link = Column(String(400), unique=True) # уникальна не может быть одинаковой ссылки

    def __repr__(self):
        return f"User {self.direction}, {self.course_name},{self.school.name},{self.the_cost},{self.appraisal},{self.link}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  