odd_number_list = []
idx = 1
number_sum = 0

while idx < 1000:
    if idx % 2 != 0:
        odd_number_list.append(idx ** 3)
    idx += 1

print('Cписок, состоящий из кубов нечётных чисел от 1 до 1000:')
print(odd_number_list)

for number in odd_number_list:
    digits_sum = 0
    idx = number

    while idx > 0:
        digit = idx % 10
        digits_sum += digit
        idx = idx // 10

    if digits_sum % 7 == 0:
        number_sum += number

print('Cумма тех чисел из списка, сумма цифр которых делится нацело на 7 =', number_sum)

number_sum = 0

for number in range(len(odd_number_list)):
    odd_number_list[number] += 17
    digits_sum = 0
    idx = odd_number_list[number]

    while idx > 0:
        digit = idx % 10
        digits_sum += digit
        idx = idx // 10

    if digits_sum % 7 == 0:
        number_sum += odd_number_list[number]

print('Cписок, состоящий из кубов нечётных чисел от 1 до 1000, каждый элемент которого увеличен на 17:')
print(odd_number_list)
print('Cумма тех чисел из нового списка, сумма цифр которых делится нацело на 7 =', number_sum)
