import unittest
from ancestor import ancestor


class AncestorTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.vs = [
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [11, 8],
            [10, 1]
        ]

    def test(self):
        self.assertEqual(ancestor(self.vs, 6), 10)
        self.assertEqual(ancestor(self.vs, 8), 4)
        self.assertEqual(ancestor(self.vs, 11), -1)                


if __name__ == '__main__':
    unittest.main()
