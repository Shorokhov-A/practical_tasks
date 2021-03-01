basket = [57.8, 46.51, 97, 18.83, 61.5, 85, 93.76, 25.14, 12.3, 71.23,
          53, 5.91, 31.51, 52.14, 73.02, 41, 81.09, 42.07, 27.02, 18]

print(id(basket))
# 5_A
result = ''

for idx in range(len(basket)):

    ruble = basket[idx] // 1
    penny = basket[idx] % 1 * 100
    price_text = f'{int(ruble)} руб {penny:02.0f} коп, '
    if idx is len(basket) - 1:
        price_text = price_text.removesuffix(', ')
    result += price_text

print(result)

# 5_B
result = ''
basket.sort()
print(id(basket))

for idx in range(len(basket)):

    ruble = basket[idx] // 1
    penny = basket[idx] % 1 * 100
    price_text = f'{int(ruble)} руб {penny:02.0f} коп, '
    if idx is len(basket) - 1:
        price_text = price_text.removesuffix(', ')
    result += price_text

print(result)
# 5_C
result = ''
basket_reversed = sorted(basket, reverse=True)
# 5_D
basket_reversed = basket_reversed[:5]
basket_reversed.reverse()

for idx in range(len(basket_reversed)):

    ruble = basket_reversed[idx] // 1
    penny = basket_reversed[idx] % 1 * 100
    price_text = f'{int(ruble)} руб {penny:02.0f} коп, '
    if idx is len(basket_reversed) - 1:
        price_text = price_text.removesuffix(', ')
    result += price_text

print(result)
