def private_print(s: str) -> None:
    print(s)


class ShallowDependencyC1:
    def __init__(self, value):
        self.value = value

    def print_my_value_and_another_too(self, another):
        private_print(f'mine={self.value}, yours={another}')

shallow_dependency_a2 = [
        None,
        True,
        42,
        "abc",
        [1, 2, 3],
        {'a': 1, "b": 2},
        (1, 2, 3),
        private_print,
]
