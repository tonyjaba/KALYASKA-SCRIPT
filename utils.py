import requests


def load_reg_exp(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read().strip()
    except IOError as e:
        print(f'Ошибка чтения файла с регулярным выражением: {e}')
        raise


def fetch_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f'Ошибка соединения: {e}')
        return None
