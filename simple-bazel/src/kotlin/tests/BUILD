# load("//src/macros:testing.bzl", "java_junit5_test", "kt_junit4_test", "kt_junit5_test")
load("//src/macros:testing.bzl", "kt_junit4_test", "kt_junit5_test", "JUNIT5_DEPS")
load("@contrib_rules_jvm//java:defs.bzl", "java_junit5_test")
load("@rules_kotlin//kotlin:jvm.bzl", "kt_jvm_test")
load("@rules_java//java:java_test.bzl", "java_test")

java_test(
    name = "MathTest_junit4",
    srcs = glob(["MathJ4Test.java"]),
    test_class = "tests.MathJ4Test",
    deps = ["@maven//:junit_junit"],
)

java_junit5_test(
    name = "MathTest_junit5",
    srcs = ["MathJ5Test.java"],
    test_class = "tests.MathJ5Test",
    deps = JUNIT5_DEPS,
)

kt_junit4_test(
    name = "Kotlin_junit4",
    srcs = ["KotlinJ4Test.kt"],
    test_class = "tests.KotlinJ4Test",
)

kt_junit5_test(
    name = "Kotlin_junit5",
    srcs = ["KotlinJ5Test.kt"],
    test_class = "tests.KotlinJ5Test",
)
