from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db import Base, engine


class direct(Base):
    __tablename__ = 'direction' # когда меняешь имя меняется и таблица
    id = Column(Integer, primary_key=True) # primary первичный ключ 
    direction = Column(String) # направление

    def __repr__(self):
        return f"User {self.name}, {self.the_cost}"

class The_skill(Base):
    __tablename__ = 'skill' # когда меняешь имя меняется и таблица
    id = Column(Integer, primary_key=True) # primary первичный ключ 
    skill = Column(String) # навыки
    
    def __repr__(self):
        return f"User {self.name}, {self.the_cost}"

class The_Scholl(Base):
    __tablename__ = 'scholl'
    id = Column(Integer, primary_key=True) # primary первичный ключ 
    scholl = Column(String) # навыки

    def __repr__(self):
        return f"User {self.name}, {self.the_cost}"

class The_difinition_of_skill(Base):
    __tablename__ = 'difinition_of_skill'
    id = Column(Integer, primary_key=True)
    course_name = Column(Integer,ForeignKey('the_main.id'), index=True, nullable=False)
    skill = Column(Integer,ForeignKey('skill.id'), index=True, nullable=False)
     
    def __repr__(self):
        return f"User {self.name}, {self.the_cost}"

class Main(Base):
    __tablename__ = 'the_main' # когда меняешь имя меняется и таблица
    id = Column(Integer, primary_key=True) # primary первичный ключ 
    direction = Column(Integer,ForeignKey('direction.id'), index=True, nullable=False) # направление
    course_name = Column(String) #название курсов
    school_name = Column(Integer,ForeignKey('scholl.id'), index=True, nullable=False) #имя школы
    the_cost = Column(Integer) # стоимость
    appraisal = Column(Float) # оценка
    link = Column(String(400), unique=True) # уникальна не может быть одинаковой ссылки

    def __repr__(self):
        return f"User {self.name}, {self.the_cost}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  