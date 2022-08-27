import unittest
from queue import*

class TestQueue(unittest.TestCase):
	def test_default(self):
		
		q = Queue()
		values = []

		for loop in range(1,10):
			q.add(loop)

		self.assertEqual(q.peek(),1)
		self.assertEqual(q.size(),9)

		while q.size() > 0:
			values.append(q.poll())

		self.assertListEqual(values, [1,2,3,4,5,6,7,8,9])
		self.assertEqual(q.peek(), None)

if __name__ == "__main__":
	unittest.main()