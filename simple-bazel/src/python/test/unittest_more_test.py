import unittest


class TestDictMethods(unittest.TestCase):
    def another_test_wrong(self):
        self.assertTrue(False)

    def test_get_default(self):
        d = {'a': 1}
        self.assertEqual(d.get('b', 0), 0)

    def test_keys(self):
        d = {'a': 1, 'b': 2}
        self.assertEqual(sorted(d.keys()), ['a', 'b'])

    def test_missing_key_raises(self):
        d = {}
        with self.assertRaises(KeyError):
            d['nope']


if __name__ == "__main__":
    unittest.main()
