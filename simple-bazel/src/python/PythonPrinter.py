def abc(a, b, c):
    return f'{a}, {b}, {c}'


a = [
        None,
        True,
        42,
        "abc",
        [1, 2, 3],
        {'a': 1, "b": 2},
        (1, 2, 3),
        abc,
    ]
print(a)

if __name__ == '__main__':
    for i in range(1, 11, 1):
        print(i)
