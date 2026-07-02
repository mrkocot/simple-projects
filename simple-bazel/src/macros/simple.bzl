load("//src/macros:another.bzl", "add_numbers", "wait_millions")
load("@rules_java//java:java_binary.bzl", "java_binary")

top_level = [False, 42]

def multiple_java_binaries(number, name, srcs, main_class):
    abc = [
        None,
        True,
        42,
        "abc",
        [1, 2, 3],
        {'a': 1, "b": 2},
        (1, 2, 3),
        add_numbers,
    ]
    very_long = [abc, abc, abc, abc, abc, abc, abc]
    summ1 = add_numbers(2, 2)
    summ2 = add_numbers(2, 2)
    wait_millions(1000)  # for tesing "pause"
    for i in range(number):
        if i == 0:
            full_name = name
        else:
            full_name = name + str(i + 1)
        
        java_binary(
            name = full_name,
            srcs = srcs,
            main_class = main_class,
        )
        
        
