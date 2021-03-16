from db import db_session
from models import User 

user = User.query.first() # пользователь ? Удалит последнюю запись
db_session.delete(user)
db_session.commit()
