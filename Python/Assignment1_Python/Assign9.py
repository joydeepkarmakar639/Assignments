def is_perfect_number(num):
    if num < 2:
        return False
    sum_of_divisors = 1 
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    return sum_of_divisors == num


def is_armstrong_number(num):
    digits = [int(d) for d in str(num)]
    num_digits = len(digits)
    sum_of_powers = sum(d ** num_digits for d in digits)
    return sum_of_powers == num


number = int(input("Enter a number: "))


if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
