
# import context

import unittest
import dummy

class TestDummy(unittest.TestCase):
    def test_add(self):
        d = dummy.Dummy()
        self.assertEqual(d.add(1, 2), 3)

    def test_sub(self):
        d = dummy.Dummy()
        self.assertEqual(d.sub(1, 2), -1)

if __name__ == '__main__':
    unittest.main()
