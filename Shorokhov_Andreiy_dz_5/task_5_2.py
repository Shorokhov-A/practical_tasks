max_num = 15
odd_nums = (num for num in range(1, max_num + 1, 2))

print(*odd_nums, sep=' ')
