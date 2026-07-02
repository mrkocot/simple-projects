load("@aspect_rules_py//py:defs.bzl", aspect_rules_py_binary = "py_binary")
load("@rules_python//python:py_binary.bzl", normal_py_binary = "py_binary")

aspect_rules_py_binary(
  name = "WeirdPythonPrinter",
  srcs = glob(["*.py"]) + ["subdir/ijk.py", "subdir/pqr.py"],
  main = "PythonPrinter.py",
)

normal_py_binary(
  name = "PythonPrinter",
  srcs = glob(["*.py"]),
  main = "PythonPrinter.py",
  srcs_version = "PY3"
)

normal_py_binary(
    name = "xyz",
    srcs = ["subdir/ijk.py", "subdir/pqr.py"],
    main = "ijk.py",
    srcs_version = "PY3"
)

normal_py_binary(
    name = "mno/prs",
    srcs = ["subdir/ijk.py", "subdir/pqr.py"],
    main = "ijk.py",
    srcs_version = "PY3"
)

normal_py_binary(
    name = "subdir-test",
    srcs = glob(["**/*.py"]),
    main = "ijk.py",
    srcs_version = "PY3"
)

py_test(
    name = "python_test_pytest",
    srcs = ["pytest_test.py"],
    main = "pytest_test.py",
    deps = ["@pypi//pytest:pkg",],
)

py_test(
    name = "python_test_unittest",
    srcs = ["unittest_test.py"],
    main = "unittest_test.py",
    deps = [],
)

