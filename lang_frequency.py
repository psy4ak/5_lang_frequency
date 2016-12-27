import re
from collections import Counter


def load_data(filepath):
    text_words = re.findall(r'\w+', open(filepath).read().lower())
    return text_words


def get_most_frequent_words(text):
    number_of_top = 10
    top_text_words = Counter(text).most_common(number_of_top)
    return top_text_words


if __name__ == '__main__':
    file_path = input('Укажите путь к файлу текста: ')
    my_text = load_data(file_path)
    top_words = get_most_frequent_words(my_text)
    print('Топ 10 слов в тексте и их количество:\n', top_words)
