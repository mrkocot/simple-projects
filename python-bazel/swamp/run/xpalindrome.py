from palindromestring.palindrome import PalindromeString
# import dafdsdsgogoorr

from bog.src.deeper.xrand import dice
# from xrand import dice
# from xrand.dice import *
from xutil import simplemath

print(dice.roll2d6())
print(simplemath.add(2, 2))

a = PalindromeString('abcba')
b = PalindromeString('abcde')

print(a.check_string_is_palindrome_or_not())
print(b.check_string_is_palindrome_or_not())

try:
    import bog.src.xutil.version
    print("+ bog.src.xutil.version")
except ModuleNotFoundError:
    print("- bog.src.xutil.version")

try:
    import src.xutil.version
    print("+ src.xutil.version")
except ModuleNotFoundError:
    print("- src.xutil.version")

try:
    import xutil.version
    print("+ xutil.version")
except ModuleNotFoundError:
    print("- xutil.version")

try:
    import version
    print("+ version")
except ModuleNotFoundError:
    print("- version")
