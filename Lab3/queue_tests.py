import unittest
#from queue_array import Queue  
from queue_linked import Queue  
   
class TestLab1(unittest.TestCase):  
    def test_queue(self):  
        '''Trivial test to ensure method names and parameters are correct'''  
        q = Queue(5)  
        self.assertEqual(q.is_empty(), True)  
        self.assertEqual(q.is_full(), False)  
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.size(), 5)
        with self.assertRaises(IndexError):
            q.enqueue(6)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 4)
        self.assertEqual(q.head.item, 2)
        self.assertEqual(q.tail.item, 5)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.head.item, 3)
        self.assertEqual(q.tail.item, 5)
  
   
if __name__ == '__main__':   
    unittest.main() 
