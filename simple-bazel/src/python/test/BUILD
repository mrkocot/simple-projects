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
    name = "pytest_special_cases",
    srcs = ["pytest_special_cases_test.py"],
    main = "pytest_special_cases_test.py",
    deps = ["@pypi//pytest:pkg",],
    args = ["-p", "no:cacheprovider"],
)

# Targets below bundle two test files each: `main` is a small runner that
# explicitly executes every test module listed in `srcs`.

aspect_rules_py_test(
    name = "aspect_python_test_pytest_multi",
    srcs = [
        "pytest_more_test.py",
        "pytest_runner.py",
        "pytest_test.py",
    ],
    main = "pytest_runner.py",
    deps = ["@pypi//pytest:pkg",],
)

normal_py_test(
    name = "python_test_pytest_multi",
    srcs = [
        "pytest_more_test.py",
        "pytest_runner.py",
        "pytest_test.py",
    ],
    main = "pytest_runner.py",
    deps = ["@pypi//pytest:pkg",],
)

normal_py_test(
    name = "python_test_unittest_multi",
    srcs = [
        "unittest_more_test.py",
        "unittest_runner.py",
        "unittest_test.py",
    ],
    main = "unittest_runner.py",
    deps = [],
)

