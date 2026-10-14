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
