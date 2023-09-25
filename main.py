# -*- coding: utf-8 -*-
# простой вопрос ответ
# окщнчание игрового цикла
# хранение данных вопросов и ответов в массивах
# перевод программы на функциональный стиль
import random
import time

had_learned = True
# наши реплики
# replys = ['привет', 'как тебя зовут', 'как дела', 'пока']

# ответы бота
# answers = [['Здраствуйте!', 'Hi', 'Здорово!', 'И вам не хворать', 'Вечер в хату бродяга'], ['Робот'], ['Нормально!'], ['Досвидание!']]

with open("C:\\Users\\HUAWEI\\OneDrive\\Рабочий стол\\ans.txt", encoding='UTF-8') as ansfile:
    answers = []
    for st in ansfile:
        st = st.replace('\n', '')
        answers.append(st.split(','))


with open("C:\\Users\\HUAWEI\\OneDrive\\Рабочий стол\\rep.txt", encoding='UTF-8') as repfile:
    replys = []
    for st in repfile:
        st = st.replace('\n', '')
        replys.append(st)

def exit_proc():
    global replys
    global answers
    with open("C:\\Users\\HUAWEI\\OneDrive\\Рабочий стол\\ans.txt", 'w', encoding='UTF-8') as ansfile:
        for item in answers:
            it = str(item)[1:-1].replace("'", '')
            ansfile.write(it)
            ansfile.write('\n')

    with open("C:\\Users\\HUAWEI\\OneDrive\\Рабочий стол\\rep.txt", 'w', encoding='UTF-8') as repfile:
        for item in replys:
            it = str(item).replace("'", '\n')
            repfile.write(it)
            repfile.write('\n')


def learn(an):
    global replys
    global answers
    global had_learned
    replys.append(an)
    print('Придумайте ответ: ', end=' ')
    answers.append([input()])
    had_learned = True
    print('Запомнил!')


def password(x):
    if x == '123456':
        return True


def reply(answer):
    game = True
    if answer in replys:
        index = replys.index(answer)
        print(random.choice(answers[index]))
        if answer == 'пока':
            if had_learned:
                exit_proc()
            game = False
    else:
        print('Извините, непонимаю.')
        if password(input('Введите пароль: ')):
            learn(answer)
        else:
            print('Извините, пароль неверен, обучить невозможно!')
    time.sleep(0.5)
    return game


def main():
    gameloop = True
    while gameloop:
        print('Вы: (для выхода напишите "пока")')
        rep = input().lower()
        gameloop = reply(rep)


if __name__ == '__main__':
    main()
