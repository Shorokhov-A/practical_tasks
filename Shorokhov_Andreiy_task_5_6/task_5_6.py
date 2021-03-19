names_list = []

while True:
    user_input = input()
    names_list.append(user_input)

    if not user_input:
        names_list.pop()
        break

result = set(names_list)

for el in names_list:
    if el in result:
        result.discard(el)
        print(el)
