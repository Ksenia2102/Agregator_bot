from db import db_session  # обновление данных
from models import User

user = User.query.first()
user.the_cost = 90000
db_session.commit()