"Создайте функцию генератор чисел Фибоначчи"

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 2] + fib[i - 1])
        yield fib[i]


print("0 1", end=" ")
for i in fibonacci(10):
    print(i, end=" ")
