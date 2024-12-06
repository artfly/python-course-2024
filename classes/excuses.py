# Student
# Prof
# get_student
# choose_prof
# ExcuseGenerator
# send_message

# Написать сервис генерации отмазок для преподов

import random

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Student(User):
    pass

class Prof(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.excuses = []

def get_student():
    name = input('Введите имя: ')
    email = input('Введите email: ')
    return Student(name, email)

def choose_prof(profs):
    print('Вы можете написать отмазку одному из этих преподов:')
    for idx, prof in enumerate(profs):
        print(f'{idx + 1} - {prof.name}: {prof.email}')
    while True:
        num = input('Введите номер препода, кому пишем:')
        if num.isnumeric():
            num = int(num)
            if num <= len(profs):
                return profs[num - 1]
        print('Пишите нормально!!11!')

def send_message(excuse, prof, student):
    print(f'''
    Здравствуйте, {prof.name}!

    К сожалению, я не смогу прийти сегодня на пару: {excuse}.
    Мне очень жаль.

    С уважением, студентка {student.name}
    ''')

class ExcuseGenerator:
    def __init__(self, excuses):
        self.excuses = excuses

    def gen_excuse(self, prof):
        if len(prof.excuses) == len(self.excuses):
            return None
        while True:
            excuse = random.choice(self.excuses)
            if excuse not in prof.excuses:
                prof.excuses.append(excuse)
                return excuse

s = get_student()

profs = [Prof('Артемий', 'artfly94@gmail.com'), Prof('Антон Александрович', 'a.pivovarov1@g.nsu.ru')]
excuses = [
    'кошка рожает',
    'бабушка умерла и болит живот',
    'семейные обстоятельства',
    'парень бросил',
    'парень нашелся',
    'болею, сплю, депрессия',
    'блинчики не получились',
    'нет настроения, улетела отдыхать'
]
chosen_one = choose_prof(profs)
generator = ExcuseGenerator(excuses)
while True:
    excuse = generator.gen_excuse(chosen_one)
    if not excuse:
        print('Придется идти :(')
        break
    else:
        send_message(excuse, chosen_one, s)
