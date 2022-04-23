import random
import pandas as pd


def words_getter():
    file = 'Добрые пожелания.xlsx'
    word_list = []
    xl = pd.read_excel(file, 0)
    my_dict = xl.to_dict()['Пожелания']
    for key, value in my_dict.items():
        word_list.append(value)
    return random.sample(word_list, len(word_list))





