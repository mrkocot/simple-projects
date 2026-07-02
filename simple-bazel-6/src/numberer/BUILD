load("//src/macros:simple.bzl", "multiple_java_binaries")
load("@io_bazel_rules_kotlin//kotlin:jvm.bzl", "kt_jvm_binary")


java_binary(
  name = "NumberPrinter1",
  srcs = glob(["*.java"]),
  main_class = "src.numberer.NumberPrinter"
)

java_binary(
  name = "NumberPrinter2",
  srcs = ["NumberPrinter.java"],
  main_class = "src.numberer.NumberPrinter"
)

java_binary(
  name = "Number.Printer3",
  srcs = glob(["NumberPrinter*"]),
  main_class = "src.numberer.NumberPrinter"
)

multiple_java_binaries(
  number = 4,
  name = "MultipliedNumberPrinter",
  srcs = ["NumberPrinter.java"],
  main_class = "src.numberer.NumberPrinter"
)

# multiple_java_binaries(
#   number = 2,
#   name = "MultipliedLargeNumberPrinter",
#   srcs = ["LargeNumberPrinter.java"],
#   main_class = "src.numberer.LargeNumberPrinter"
# )

java_binary(
  name = "LargeNumberPrinter",
  srcs = ["LargeNumberPrinter.java"],
  main_class = "src.numberer.LargeNumberPrinter"
)

py_binary(
  name = "PythonPrinter",
  srcs = glob(["*.py"]),
  main = "PythonPrinter.py",
  srcs_version = "PY3"
)

# kt_jvm_binary(
#   name = "KotlinPrinter",
#   srcs = ["KotlinPrinter.kt", "NumberPrinter.java"],
#   main_class = "src.numberer.KotlinPrinter"
# )

