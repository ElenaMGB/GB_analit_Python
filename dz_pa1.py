# Знакомство с языком Python (семинары)
# Задание 1. one hot
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это
# сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

# Решение
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
data.shape
print(data)

#добавляем столбцы в one hot кодировке
data['human'] = data['whoAmI'].apply(lambda x: 0 if x=='robot' else 1)
data['robot'] = data['whoAmI'].apply(lambda x: 1 if x=='robot' else 0)
print(data)

#проверка
pd.get_dummies(data)

# # Идеальное решение
# import pandas as pd
# import random
# # Генерация DataFrame
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})
# # Создание one-hot кодирования
# unique_values = data['whoAmI'].unique() # Находим уникальные значения
# one_hot = pd.DataFrame()
# for value in unique_values:
#     one_hot[value] = (data['whoAmI'] == value).astype(int)
# # Объединение one-hot кодирования с исходным DataFrame (опционально)
# data = pd.concat([data, one_hot], axis=1)
# print(data.head())