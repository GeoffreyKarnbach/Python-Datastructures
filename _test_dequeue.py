import unittest
from dequeue import*

class TestDequeue(unittest.TestCase):
	def test_default(self):
		dq = Dequeue()
		values = []

		for loop in range(1,10):
			dq.addLast(loop)

		self.assertEqual(dq.size(),9)
		self.assertEqual(dq.peekFirst(), 1)
		self.assertEqual(dq.peekLast(), 9)

		while dq.size() > 0:
			values.append(dq.pollFirst())

		self.assertListEqual(values, [1,2,3,4,5,6,7,8,9])
		self.assertEqual(dq.pollFirst(),None)


if __name__ == "__main__":
	unittest.main()