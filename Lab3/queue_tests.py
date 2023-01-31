import unittest
#from queue_array import Queue  
from queue_linked import Queue  
   
class TestLab1(unittest.TestCase):  
    def test_queue(self):  
        '''Trivial test to ensure method names and parameters are correct'''  
        q = Queue(5)  
        self.assertEqual(q.is_empty(), True)  
        self.assertEqual(q.is_full(), False)  
        q.enqueue('thing')
        q.enqueue('that')
        # q.dequeue()  
        self.assertEqual(q.size(), 2)  
   
if __name__ == '__main__':   
    unittest.main() 
