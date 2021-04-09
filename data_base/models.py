from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from data_base.db import Base, engine


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    study_option_id = Column(Integer, ForeignKey('study_options.id'), index=True, nullable=False)
    course_name = Column(String)
    school = Column(Integer, ForeignKey('schools.id'), index=True, nullable=False)
    cost = Column(Integer)
    rating = Column(Float)
    link = Column(String)

    def __repr__(self):
        return f"{self.course_name}, {self.school}, {self.cost}, {self.rating}"


class StudyOption(Base):
    __tablename__ = 'study_options'
    id = Column(Integer, primary_key=True)
    study_option = Column(String)
    skills = relationship('Skill', lazy='joined')

    def __str__(self):
        return f'{self.study_option}'


class Skill(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    study_option_id = Column(Integer, ForeignKey('study_options.id'), index=True, nullable=False)
    skill = Column(String)
    study_option = relationship('StudyOption', lazy='joined')

    def __str__(self):
        return f'{self.skill}'


class School(Base):
    __tablename__ = 'schools'
    id = Column(Integer, primary_key=True)
    school_name = Column(String)


class SkillRelation(Base):
    __tablename__ = 'skill_relations'
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), index=True, nullable=False)
    skill_id = Column(Integer, ForeignKey('skills.id'), index=True, nullable=False)

    def __repr__(self):
        return f'Id курсов по нужному навыку {self.course_id}'



if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
