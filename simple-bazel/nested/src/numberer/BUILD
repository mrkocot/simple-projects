load("@rules_java//java:java_binary.bzl", "java_binary")
load("@rules_kotlin//kotlin:jvm.bzl", "kt_jvm_binary")
load("@aspect_rules_py//py:defs.bzl", aspect_rules_py_binary = "py_binary")
load("@rules_python//python:py_binary.bzl", normal_py_binary = "py_binary")

aspect_rules_py_binary(
  name = "WeirdPythonPrinter",
  srcs = glob(["*.py"]) + ["subdir/ijk.py", "subdir/pqr.py"],
  main = "PythonPrinter.py",
)

normal_py_binary(
  name = "PythonPrinter",
  srcs = glob(["*.py"]) + ["subdir/ijk.py", "subdir/pqr.py"],
  srcs_version = "PY3"
)

java_binary(
  name = "NumberPrinter1",
  srcs = glob(["**/*.java"]),
  main_class = "numberer.NumberPrinter"
)

java_binary(
  name = "LargeNumberPrinter",
  srcs = ["LargeNumberPrinter.java"],
  main_class = "numberer.LargeNumberPrinter"
)

