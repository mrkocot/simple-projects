import sys

if __name__ == '__main__':
    sys_executable = sys.executable
    sys_version = sys.version
    args = list(sys.argv)
    print(f'Arguments: {args}')
    print(sys_version, sys_executable)
