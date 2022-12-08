def factorial(n):
    if n > 1:
        result = n * factorial(n-1)
        print(f"{n} = {result}")
    else:
        print(f"{n} = 1")

