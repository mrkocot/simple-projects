JUNIT5_DEPS = [
    "@maven//:org_junit_jupiter_junit_jupiter",
    "@maven//:org_junit_jupiter_junit_jupiter_api",
    "@maven//:org_junit_platform_junit_platform_console",
]

java_test(
    name = "MathTest",
    srcs = ["MathTest.java"],
    test_class = "src.tests.MathTest",
    deps = ["@maven//:junit_junit"],
)

java_test(
    name = "MathTest_junit5",
    main_class = "org.junit.platform.console.ConsoleLauncher",
    deps = JUNIT5_DEPS,
    args = ["--select-class=" + "tests.MathJ5Test", "--fail-if-no-tests"],
    srcs = ["MathJ5Test.java"],
)
