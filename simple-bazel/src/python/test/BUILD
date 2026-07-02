load("@aspect_rules_py//py:defs.bzl", aspect_rules_py_test = "py_test")
load("@rules_python//python:py_test.bzl", normal_py_test = "py_test")

aspect_rules_py_test(
    name = "aspect_python_test_pytest",
    srcs = ["pytest_test.py"],
    main = "pytest_test.py",
    deps = ["@pypi//pytest:pkg",],
)

normal_py_test(
    name = "python_test_pytest",
    srcs = ["pytest_test.py"],
    main = "pytest_test.py",
    deps = ["@pypi//pytest:pkg",],
)

normal_py_test(
    name = "python_test_unittest",
    srcs = ["unittest_test.py"],
    main = "unittest_test.py",
    deps = [],
)

normal_py_test(
    name = "test_foo",
    srcs = ["test_foo.py"],
)

