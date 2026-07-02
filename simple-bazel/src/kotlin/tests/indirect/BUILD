load("@rules_java//java:java_test.bzl", "java_test")
load("@rules_java//java:java_library.bzl", "java_library")
load("@rules_java//java:java_binary.bzl", "java_binary")

java_test(
    name = "the_test",
    srcs = [],
    test_class = "tests.MathTest",
    runtime_deps = [":test_supplier"],
    deps = [],
)

java_library(
    name = "test_supplier",
    srcs = ["MathTest.java"],
    deps = ["@maven//:junit_junit"],
)

# java_binary(
#   name = "NumberPrinter1",
#   srcs = ["NumberPrinter.java"],
#   main_class = "numberer.NumberPrinter",
# )
