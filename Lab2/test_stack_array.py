import unittest
# Use the imports below to test either your array-based stack
# or your link-based version
#from stack_array import Stack
from stack_linked import Stack


class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 0)
        #self.assertEqual(stack.head.next, None)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        #self.assertEqual(stack.head.data, 4)
        #self.assertEqual(stack.head.next, stack.node.next)
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.peek(), 4)
        with self.assertRaises(IndexError):
            stack.push(5)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.peek(), 3)
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.peek(), 2)



if __name__ == '__main__':
    unittest.main()
