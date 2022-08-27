import unittest
from linkedlist import*

class TestLinkedlist(unittest.TestCase):
	def test_default(self):
		ll = LinkedList()
		values = []

		ll.addLast(1)
		ll.addLast(2)
		ll.addLast(4)

		ll.add(3,2)

		self.assertEqual(ll.getFirst(),1)
		self.assertEqual(ll.getLast(),4)
		self.assertEqual(ll.size(),4)
		self.assertEqual(ll.indexOf(3),2)

		for loop in range(ll.size()):
			values.append(ll.get(loop))

		self.assertEqual(ll.pollFirst(),1)
		self.assertListEqual(values, [1,2,3,4])

if __name__ == "__main__":
	unittest.main()