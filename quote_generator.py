import requests
from requests.exceptions import RequestException

def get_language_choice():
    # Функция для выбора языка пользователя
    while True:
        lang = input("Выбери язык на котором будет сгенерирована цитата (en - англ./ru - рус.): ").lower()
        if lang in ['en', 'ru']:
            return lang
        else:
            print("Пожалуйста, введите корректный язык.")

def fetch_quote(lang):
    # Функция для получения цитаты с использованием Forismatic API
    quote_api_url = f"http://api.forismatic.com/api/1.0/?method=getQuote&lang={lang}&format=json"

    try:
        response = requests.get(quote_api_url)
        response.raise_for_status()
        return response.json()

    except RequestException as error:
        print(f"Error while fetching a quote: {error}")
        return None

def get_random_quote(lang):
    # Функция для получения случайной цитаты с возможностью нескольких попыток
    max_retries = 3
    for _ in range(max_retries):
        quote_data = fetch_quote(lang)

        if quote_data:
            quote = quote_data.get('quoteText', '')
            author = quote_data.get('quoteAuthor', '')

            if author:
                return f'"{quote}" - {author}'
            else:
                return f'"{quote}"'

    return "Unable to fetch a quote after multiple attempts."
