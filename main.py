import time
import webbrowser
import requests
import winsound

board = input('Введите доску(например news):\n')
def get_thread():
    try:
        r = requests.get('https://2ch.hk/'+board+'/catalog_num.json').json()
        return r['threads'][0]['num']
    except Exception as Ex:
        print('Ошибка соединения!(проверьте интернет-соединение и правильность ввода доски):\n' + Ex)


current_thread = get_thread()
while True:
    if current_thread == get_thread():
        print('Нет новых тредов')
    else:
        webbrowser.open('https://2ch.hk/'+board+'/res/' + str(get_thread()) + '.html', new=2, autoraise=True)
        winsound.PlaySound("nya.wav", 0)
        current_thread = get_thread()
    time.sleep(3)
