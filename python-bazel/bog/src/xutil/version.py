import sys

def current() -> str:
    return sys.version.split()[0]

def print_current() -> None:
    print(f'Running on Python {current()}')
