def generate_fibonacci_up_to(n):
    a, b = 0, 1
    fibonacci_series = []
    while a <= n:
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

n = int(input("Enter the upper limit for the Fibonacci series: "))

fibonacci_series = generate_fibonacci_up_to(n)
print(f"Fibonacci series up to {n} is:")
print(fibonacci_series)
