import os
import sys

import pytest

# Test modules shipped in this target's srcs. Bazel does not auto-discover extra
# srcs, so they are listed explicitly here.
TEST_FILES = [
    "pytest_test.py",
    "pytest_more_test.py",
]

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    args = [os.path.join(here, name) for name in TEST_FILES]

    xml_output = os.environ.get("XML_OUTPUT_FILE")
    if xml_output:
        args.append("--junitxml=" + xml_output)

    args.extend(sys.argv[1:])
    sys.exit(pytest.main(args))
