load("@aspect_rules_py//py:defs.bzl", aspect_rules_py_binary = "py_binary")
load("@rules_python//python:py_binary.bzl", "py_binary")

aspect_rules_py_binary(
  name = "depless_weird",
  srcs = ["depless.py"],
  deps = [],
)

py_binary(
  name = "depless",
  srcs = ["depless.py"],
  deps = [],
)

py_binary(
  name = "palindrome",
  srcs = ["palindrome.py"],
  deps = [
      "//swamp/util",
      "@pypi//palindrome_string:pkg",
  ],
)

py_binary(
  name = "xpalindrome",
  srcs = ["xpalindrome.py"],
  deps = [
#       "//bog:xutil",
      "//bog:xrand",
      "@pypi//palindrome_string:pkg",
  ],
)
