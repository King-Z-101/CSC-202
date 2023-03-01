import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)
        self.assertTrue(t_list.is_empty())
        t_list.add(20)
        t_list.add(30)
        self.assertEqual(t_list.python_list(), [20, 30])
        t_list.add(25)
        self.assertEqual(t_list.python_list(), [20, 25, 30])
        self.assertEqual(t_list.python_list_reversed(), [30, 25, 20])
        self.assertEqual(t_list.size(), 3)
        with self.assertRaises(IndexError):
            t_list.pop(5)


if __name__ == '__main__':
    unittest.main()
