import os
import sys
import unittest

# Runfiles put the workspace root on sys.path, not this package's directory, so
# the sibling test modules are only importable after adding it.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import unittest_test
import unittest_more_test

# Modules are imported explicitly instead of using discovery so the suite always
# matches this target's srcs, regardless of runfiles layout.
TEST_MODULES = [
    unittest_test,
    unittest_more_test,
]

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(
        loader.loadTestsFromModule(module) for module in TEST_MODULES
    )
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
