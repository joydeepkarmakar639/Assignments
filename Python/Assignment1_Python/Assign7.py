def is_divisible_by_7_not_5(num):
    return num % 7 == 0 and num % 5 != 0


print("Numbers between 1000 and 2000 that are divisible by 7 but not multiples of 5:")
for number in range(1000, 2001):
    if is_divisible_by_7_not_5(number):
        print(number, end=' ')
