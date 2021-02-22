dictionary = ['процент', 'процента', 'процентов']
percent_value_list = []
idx = 0

while idx <= 20:
    percent_value_list.append(idx)
    idx += 1

print(percent_value_list)

for percent_value in percent_value_list:
    value_mod = percent_value

    if value_mod < 0:
        value_mod *= -1

    if value_mod % 10 == 0 or value_mod % 10 > 4 or 11 <= value_mod % 100 <= 14:
        print(percent_value, dictionary[2])

    elif value_mod % 10 == 1:
        print(percent_value, dictionary[0])

    else:
        print(percent_value, dictionary[1])
