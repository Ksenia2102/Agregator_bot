import random


opt = ['Прог', 'Диз', 'Лит']
skl = ['Py', 'jv', 'draw', 'anlz']
sch = ['gkbr', 'yand', 'sklbox']


def generate_data(num_rows=10):
    all_data = []
    for row in range(num_rows):
        course = {
            'study_options': random.choice()
            random.choice(opt), random.choice(skl), 'Название курса', 
            random.choice(skl), random.randint(20000, 200000), round(random.uniform(1, 5), 1),
            'Ccылка'
        }
        all_data.append(course)
    return(all_data)


if __name__ == "__main__":
    print(generate_data())
