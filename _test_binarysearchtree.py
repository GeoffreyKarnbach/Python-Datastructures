import unittest
from binarysearchtree import*

class TestBinarysearchtree(unittest.TestCase):
	def test_default(self):
		bst = BinarySearchTree()

		self.assertEqual(bst.put(5,10), None)
		self.assertEqual(bst.put(2,4), None)
		self.assertEqual(bst.put(7,14), None)
		self.assertEqual(bst.put(1,2), None)
		self.assertEqual(bst.put(3,6), None)

		self.assertEqual(bst.get(6), None)
		self.assertEqual(bst.get(2), 4)
		self.assertEqual(bst.contains(10), False)
		self.assertEqual(bst.contains(5), True)

if __name__ == "__main__":
	unittest.main()