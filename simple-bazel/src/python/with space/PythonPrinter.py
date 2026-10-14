from colorama.ansi import Fore, Style
from deep_deps_b import DeepDependencyB1, numbers_one_to_ten

# from deep_deps_b import numbers_one_to_ten, DeepDependencyB1
# from src.python.deps.deep_deps_a import DeepDependencyA1

if __name__ == '__main__':
    # a = DeepDependencyA1()
    b = DeepDependencyB1()
    for i in numbers_one_to_ten:
        if i % 2 == 0:
            print(f'{Fore.CYAN}{i}{Style.RESET_ALL}')
        else:
            print(f'{Fore.RED}{i}{Style.RESET_ALL}')
