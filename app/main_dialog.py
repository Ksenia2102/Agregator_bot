from telegram.ext import ConversationHandler, CallbackContext
from telegram import Update
from config import STUDY_OPTIONS, SKILLS
from .texts import welcome_text
from .utils import study_options_keybord, skills_keyboard,table_call


def start_bot(update, context):
    update.message.reply_text(
        welcome_text, reply_markup=study_options_keybord()
        )
    return 'skills'


def keyboard(update:Update,context:CallbackContext)->None:
    keyboard = [['default']] #клавиатура плейсхолдер, на случай отсуствия значения в базе 
    query= StudyOptions.query.all() #возвращает список элементов из базы
    if query: 
        keyboard=[] # если запрос что то вернул , убираем дефолтное значение ,пробегаемся по элементам базы.
        for x in query: 
            keyboard.append([x.study_oprions]) 
    update.message.replly_text('msg',reply_markup=ReplyKeyboardMarkup(keyboard))



#def generate_skills(update,context):
    #study_option = update.message.text
    #if study_option in STUDY_OPTIONS:
        #update.message.reply_text(
            #'Выберите навык, который хотите изучить.',
            #reply_markup=skills_keyboard(study_option))
        #return 'courses'


def generate_courses(update, context):
    course_name = update.message.text
    print(SKILLS.values())
    for skills in SKILLS.values():
        if course_name in skills:
            update.message.reply_text(
                f'ЗДЕСЬ БУДЕТ СПИСОК КУРСОВ ПО {course_name}'
                )
            return ConversationHandler.END