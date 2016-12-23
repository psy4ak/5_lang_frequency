import re


def load_data(filepath):
    text_words = re.findall(r'\w+', open(filepath).read().lower())
    return text_words


def get_most_frequent_words(text):
    wordcount = {}
    for word in text:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    words_list = list(wordcount.items())
    sorted_list = sorted(words_list, key=lambda item: item[1], reverse=True)
    return sorted_list[:9]


if __name__ == '__main__':
    file_path = input('Укажите путь к файлу текста: ')
    my_text = load_data(file_path)
    top_words = get_most_frequent_words(my_text)
    print('Топ 10 слов в тексте и их количество:\n', top_words)
