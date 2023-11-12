from quote_generator import get_language_choice, get_random_quote

def main():
    # Основная функция, вызывающая другие функции
    lang = get_language_choice()
    random_quote = get_random_quote(lang)
    print(random_quote)

if __name__ == "__main__":
    main()
