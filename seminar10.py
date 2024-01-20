# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сделать без встроенных ф-ций, например,get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

# Решение:

import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot_data = data.copy()
one_hot_data['robot'] = (data['whoAmI'] == 'robot').astype(int)
one_hot_data['human'] = (data['whoAmI'] == 'human').astype(int)

print(one_hot_data.head())