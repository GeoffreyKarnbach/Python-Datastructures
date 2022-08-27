import unittest
from stack import*

class TestStack(unittest.TestCase):
	def test_default(self):

		s = Stack()
		values = []

		for loop in range(1,10):
			s.push(loop)
		
		self.assertAlmostEqual(s.peek(),9)
		self.assertEqual(s.size(),9)

		while s.size() > 0:
			values.append(s.pop())

		valuesToCheck = [9,8,7,6,5,4,3,2,1]

		self.assertListEqual(values, valuesToCheck)
		self.assertEqual(s.pop(), None)

if __name__ == "__main__":
	unittest.main()