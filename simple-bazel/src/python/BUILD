load("@aspect_rules_py//py:defs.bzl", aspect_rules_py_binary = "py_binary")
load("@rules_python//python:py_binary.bzl", normal_py_binary = "py_binary")
load("@rules_python//python:py_test.bzl", "py_test")

aspect_rules_py_binary(
  name = "WeirdPythonPrinter",
  srcs = glob(["*.py"]) + ["subdir/ijk.py", "subdir/pqr.py"],
  deps = ["//src/python/deps:weird_deep_deps", "@pypi//colorama:pkg"],
  main = "PythonPrinter.py",
)

normal_py_binary(
  name = "PythonPrinter",
  srcs = glob(["*.py"]),
  deps = ["//src/python/deps:normal_deep_deps", "@pypi//colorama:pkg"],
  main = "PythonPrinter.py",
  srcs_version = "PY3"
)

normal_py_binary(
  name = "AnotherPythonPrinter",
  srcs = glob(["*.py"]),
  deps = ["//src/python/deps:deep_deps_but_only_A", "//src/python/deps:deep_deps_but_only_B", "@pypi//colorama:pkg"],
  main = "AnotherPythonPrinter.py",
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
