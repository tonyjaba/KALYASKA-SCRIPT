import time
import argparse
from utils import load_reg_exp, fetch_json
from handlers import handle_post_update, handle_thread_update
from config import REG_EXP_FILE, DEFAULT_DELAY


def get_thread(board, thread=None):
    url = f'https://2ch.hk/{board}/catalog_num.json'
    data = fetch_json(url)
    if data:
        if thread:
            for t in data['threads']:
                if t['num'] == thread:
                    return t
        else:
            return data['threads'][0]
    return None


def get_post(board, thread):
    url = f'https://2ch.hk/{board}/res/{thread}.json'
    data = fetch_json(url)
    if data:
        return data['threads'][0].get('posts')
    return None


def check_for_updates(board, thread, reg_exp, delay, play_sound, open_browser):
    current_post = None
    current_thread = None

    while True:
        if thread:
            new_post = get_post(board, thread)
            if new_post:
                new_post = new_post[-1]
                if current_post and new_post['num'] == current_post['num']:
                    print('Нет новых постов')
                else:
                    handle_post_update(new_post, reg_exp, play_sound)
                    current_post = new_post
        else:
            new_thread = get_thread(board)
            if new_thread:
                if current_thread and new_thread['num'] == current_thread['num']:
                    print('Нет новых тредов')
                else:
                    handle_thread_update(board, new_thread, reg_exp, play_sound, open_browser)
                    current_thread = new_thread
        time.sleep(delay)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Мониторинг доски на 2ch.hk.')
    parser.add_argument('board', type=str, help='Название доски (например, news)')
    parser.add_argument('--thread', type=int, help='Номер треда (оставьте пустым для поиска по всей борде)')
    parser.add_argument('--delay', type=int, default=DEFAULT_DELAY, help='Задержка между запросами в секундах')
    parser.add_argument('--nosound', action='store_true', help='Отключить воспроизведение звука')
    parser.add_argument('--nobrowser', action='store_true', help='Отключить открытие ссылок в браузере')
    args = parser.parse_args()

    reg_exp = load_reg_exp(REG_EXP_FILE)
    check_for_updates(args.board, args.thread, reg_exp, args.delay, not args.nosound, not args.nobrowser)
