import unittest
from binaryTree import *


#Creating a method to store the initialization of binary tree and its parents/children nodes
def setup():
    numTree = binaryTree()
    numTree.add_Node(43)
    numTree.add_Node(15)
    numTree.add_Node(60)
    numTree.add_Node(8)
    numTree.add_Node(30)
    numTree.add_Node(20)
    numTree.add_Node(36)
    numTree.add_Node(50)
    numTree.add_Node(82)
    numTree.add_Node(70)
    numTree.add_Node(7)
    numTree.add_Node(12)
    numTree.add_Node(45)
    numTree.add_Node(55)
    numTree.add_Node(120)
    return numTree.root


class TestLab7(unittest.TestCase):
    def test_preorder_recursive(self):
        alist = []
        self.assertEqual(preorder_recursive(setup(), alist), [43, 15, 8, 7, 12, 30, 20, 36, 60, 50, 45, 55, 82, 70, 120])

    def test_inorder_recursive(self):
        alist = []
        self.assertEqual(inorder_recursive(setup(), alist), [7, 8, 12, 15, 20, 30, 36, 43, 45, 50, 55, 60, 70, 82, 120])

    def test_postorder_recursive(self):
        alist = []
        self.assertEqual(postorder_recursive(setup(), alist), [7, 12, 8, 20, 36, 30, 15, 45, 55, 50, 70, 120, 82, 60, 43])

    def test_preorder_iteration(self):
        alist = []
        self.assertEqual(preorder_iteration(setup(), alist), [43, 15, 8, 7, 12, 30, 20, 36, 60, 50, 45, 55, 82, 70, 120])

    def test_inorder_iteration(self):
        alist = []
        self.assertEqual(inorder_iteration(setup(), alist), [7, 8, 12, 15, 20, 30, 36, 43, 45, 50, 55, 60, 70, 82, 120])

    def test_postorder_iteration(self):
        alist = []
        self.assertEqual(postorder_iteration(setup(), alist), [7, 12, 8, 20, 36, 30, 15, 45, 55, 50, 70, 120, 82, 60, 43])


if __name__ == '__main__':
    unittest.main()




