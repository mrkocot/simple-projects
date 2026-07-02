load("@rules_python//python:py_library.bzl", "py_library")

py_library(
  name = "xutil",
  srcs = glob(["src/xutil/*.py"]),
  visibility = ["//visibility:public"],
  imports = ["src"],
)

# a = [[b for b in range(10000000)] * 0 for c in range(100000000)]

py_library(
  name = "xrand",
  srcs = glob(["src/deeper/xrand/*.py"]),
  visibility = ["//visibility:public"],
  deps = ["//bog:xutil"],
  imports = ["src/deeper"],
)
