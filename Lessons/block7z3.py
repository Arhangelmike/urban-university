import os
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = {}

    def get_all_words(self):
        for file_name in self.file_names:
            word = ''
            with open(file_name, encoding='utf-8') as file:
                for line in file:  # пересобрать строку без знаков пунктуации
                    for char in line:
                        if char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            word += ''
                        else:
                            word += char
                words = word.lower().split() # разбить строку на список
            self.all_words[file_name] = words
        return self.all_words

    def find(self, word):
        word = word.lower()
        find_word_pos = {}
        for name, words in self.get_all_words().items():
            if word in words:
                find_word_pos[name] = words.index(word.lower()) + 1
        return find_word_pos

    def count(self, word):
        word = word.lower()
        find_word_quant = {}
        for name, words in self.get_all_words().items():
            count = 0
            for i in words:
                if word == i:
                    count += 1
            find_word_quant[name] = count
        return find_word_quant
# положить файлы в паку с путем ниже
path = 'C:/Users/user/Downloads/All1/All/'
f = [f'{path}{file}' for file in os.listdir(path)]
# print(f) # проверка на то что получили список файлов
for filename in f:
    # print(f'{filename}') # check that IN one filename
    finder2 = WordsFinder(f'{filename}')
    print(finder2.get_all_words()) # Все слова
    print(finder2.find('TEXT')) # 3 слово по счёту
    print(finder2.count('teXT')) # 4 слова teXT в тексте всего
    # раскоментировать для другого поискового слова из проверки
    # print(finder2.find('The'))
    # print(finder2.count('the'))