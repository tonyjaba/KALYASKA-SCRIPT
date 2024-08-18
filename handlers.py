import re
import winsound
import webbrowser
from config import SOUND_FILE


def handle_post_update(post, reg_exp, play_sound=True):
    if reg_exp:
        matches = re.findall(reg_exp, post['comment'])
        if matches:
            print(f"Найдено: {matches}\n{post['comment']}")
            if play_sound:
                winsound.PlaySound(SOUND_FILE, winsound.SND_FILENAME)
            return
        else:
            print('Ничего не найдено в посте')
        return

    print(f"Найден новый пост:\n{post['comment']}")
    if play_sound:
        winsound.PlaySound(SOUND_FILE, winsound.SND_FILENAME)


def handle_thread_update(board, thread, reg_exp, play_sound=True, open_browser=True):
    if reg_exp:
        matches = re.findall(reg_exp, thread['comment'])
        if matches:
            print(f"Найдено: {matches}")
            print(f'https://2ch.hk/{board}/res/{thread["num"]}.html')
            if open_browser:
                webbrowser.open(f'https://2ch.hk/{board}/res/{thread["num"]}.html', new=2, autoraise=True)
            if play_sound:
                winsound.PlaySound(SOUND_FILE, winsound.SND_FILENAME)
            return
        else:
            print('Ничего не найдено в треде')
            return

    print("Найден новый тред")
    print(f'https://2ch.hk/{board}/res/{thread["num"]}.html')
    if open_browser:
        webbrowser.open(f'https://2ch.hk/{board}/res/{thread["num"]}.html', new=2, autoraise=True)
    if play_sound:
        winsound.PlaySound(SOUND_FILE, winsound.SND_FILENAME)