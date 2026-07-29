We have a target rule that produces union of dependencies and it results in a clash between the same module names for java and python during import

```
def _impl_target_union(ctx):
    empty_jar = make_empty_jar(ctx)
    runfiles = ctx.runfiles()
    java_info = java_common.merge(
        [dep[JavaInfo] for dep in ctx.attr.deps if JavaInfo in dep],
    )
    strato_infos = [dep[StratoInfo] for dep in ctx.attr.deps if StratoInfo in dep]
    thrift_strato_infos = [
        dep[ThriftStratoInfo] for dep in ctx.attr.deps if ThriftStratoInfo in dep
    ]
    for dep in ctx.attr.deps:
        runfiles = runfiles.merge(dep[DefaultInfo].default_runfiles)
    return [
        java_info,
        PyInfo(
            transitive_sources=depset(
                transitive=[
                    dep[PyInfo].transitive_sources
                    for dep in ctx.attr.deps
                    if PyInfo in dep
                ],
            ),
        ),
        ThriftStratoInfo(
            output_dirs=depset(
                transitive=[info.output_dirs for info in thrift_strato_infos],
            ),
        ),
        StratoInfo(
            srcs=depset(transitive=[info.srcs for info in strato_infos]),
            transitive_srcs=depset(
                transitive=[info.transitive_srcs for info in strato_infos],
            ),
            config_roots=depset(
                transitive=[info.config_roots for info in strato_infos],
            ),
            compiled_config_roots=depset(
                transitive=[info.compiled_config_roots for info in strato_infos],
            ),
        ),
        DefaultInfo(
            files=depset(transitive=[dep[DefaultInfo].files for dep in ctx.attr.deps]),
            runfiles=runfiles,
        ),
        IsFilesOrAlias(),
    ]
```

# Reproduction Steps
import bazel project with the above rule in the dependency graph
