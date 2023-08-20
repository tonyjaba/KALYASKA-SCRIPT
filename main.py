import time
import webbrowser
import requests
import winsound
import re

with open("reg_exp.txt", "r", encoding="utf-8") as f:
    reg_exp = f.read()
board = input('Введите доску(например news):\n')


def get_thread():
    try:
        r = requests.get('https://2ch.hk/' + board + '/catalog_num.json').json()
        return r['threads'][0]
    except Exception as Ex:
        input('Ошибка соединения!(проверьте интернет-соединение и правильность ввода доски):\n' + Ex)


current_thread = get_thread()
while True:
    new_thread = get_thread()
    if current_thread['num'] == new_thread['num']:
        print('Нет новых тредов')
    else:
        if reg_exp:
            if re.findall(reg_exp, new_thread['comment']):
                print("Найдено: "+re.findall(reg_exp, new_thread['comment']))
                webbrowser.open('https://2ch.hk/' + board + '/res/' + str(new_thread['num']) + '.html', new=2,
                                autoraise=True)
                winsound.PlaySound("nya.wav", 0)
                current_thread = new_thread
            else:
                print('Ничего не найдено в посте')
                current_thread = new_thread
        else:
            print("Найден новый тред")
            webbrowser.open('https://2ch.hk/' + board + '/res/' + str(new_thread['num']) + '.html', new=2,
                            autoraise=True)
            winsound.PlaySound("nya.wav", 0)
            current_thread = new_thread
    time.sleep(3)
