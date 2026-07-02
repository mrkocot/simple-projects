load("@rules_kotlin//kotlin:jvm.bzl", "kt_jvm_test")

JUNIT5_DEPS = [
    "@maven//:org_junit_jupiter_junit_jupiter",
    "@maven//:org_junit_jupiter_junit_jupiter_api",
    "@maven//:org_junit_platform_junit_platform_console",
]

KOTEST_DEPS = [
    "@maven//:io_kotest_kotest_assertions_api_jvm",
    "@maven//:io_kotest_kotest_assertions_core_jvm",
    "@maven//:io_kotest_kotest_assertions_shared_jvm",
    "@maven//:io_kotest_kotest_common_jvm",
]

def java_junit5_test(test_class, deps = [], **kwargs):
    native.java_test(
        main_class = "org.junit.platform.console.ConsoleLauncher",
        deps = JUNIT5_DEPS + deps,
        args = ["--select-class=" + test_class, "--fail-if-no-tests"],
        **kwargs
    )

def kt_junit4_test(test_class, deps = [], **kwargs):
    kt_jvm_test(
        deps = deps + ["@maven//:junit_junit"] + KOTEST_DEPS,
        test_class = test_class,
        **kwargs
    )

def kt_junit5_test(test_class, deps = [], **kwargs):
    kt_jvm_test(
        main_class = "org.junit.platform.console.ConsoleLauncher",
        deps = deps + JUNIT5_DEPS + KOTEST_DEPS,
        args = ["--select-class=" + test_class, "--fail-if-no-tests"],
        **kwargs
    )
