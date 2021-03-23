import json

with open('users.csv', 'r', encoding='utf-8') as file_1:
    users_list = list(map(str.strip, file_1.readlines()))

with open('hobby.csv', 'r', encoding='utf-8') as file_2:
    hobby_list = list(map(str.strip, file_2.readlines()))

names_dict = {}
# Повторение - мать учения.
_users_list = (el for el in users_list)
_hobby_list = (el for el in hobby_list)
# Делаем генератор-предохранитель для генератора _hobby_list.
_users_counter = (num for num in range(len(users_list)))

for counter_num, value, key in zip(_users_counter, _hobby_list, _users_list):
    names_dict[key.replace(',', ' ')] = value.replace(',', ', ')

for rest in _users_list:
    names_dict[rest.replace(',', ' ')] = None

for rest in _hobby_list:
    exit(1)

with open('users_hobby.json', 'w', encoding='utf-8') as file_3:
    json.dump(names_dict, file_3)

with open('users_hobby.json', 'r', encoding='utf-8') as file_3:
    names = json.load(file_3)

print(names, type(names))
