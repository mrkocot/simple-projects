# File for testing how things are rendered in Starlark

0                               # int
123                             # decimal int
0x7f                            # hexadecimal int
0o755                           # octal int

0.0                # float
0.
.0
1e10
1e+10
1e-10
1.1e10
1.1e+10
1.1e-10

"""abc
def
ghi"""

"hello"
'hello'            # string
'''hello'''
"""hello"""        # triple-quoted string
r'hello'
r"hello"           # raw string literal

b"hello"
b'hello'           # bytes
b'''hello'''
b"""hello"""       # triple-quoted bytes
rb'hello'
br"hello"         # raw bytes literal

