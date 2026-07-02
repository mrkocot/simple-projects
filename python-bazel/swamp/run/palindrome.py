from palindromestring.palindrome import PalindromeString
from swamp.util import version
import sys

if __name__ == '__main__':
    sys_executable = sys.executable
    sys_version = sys.version
    print(sys_executable, sys_version)

    version.print_current()

    a = PalindromeString('abcba')
    b = PalindromeString('abcde')

    print(a.check_string_is_palindrome_or_not())
    print(b.check_string_is_palindrome_or_not())
