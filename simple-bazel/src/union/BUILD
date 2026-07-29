load("@rules_java//java:java_library.bzl", "java_library")
load("@rules_python//python:py_binary.bzl", "py_binary")
load("//src/macros:target_union.bzl", "target_union")

java_library(
    name = "java_dep",
    srcs = ["UnionJava.java"],
)

py_binary(
    name = "python_dep",
    srcs = ["union_py.py"],
    main = "union_py.py",
    srcs_version = "PY3",
)

target_union(
    name = "java_python_union",
    deps = [
        ":java_dep",
        ":python_dep",
    ],
)
