numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]


def f(x):
    if x > 50 and x % 2 == 1:
        return x


print(list(filter(f, numbers)))