import unittest
from hashmap import*

class TestHashmap(unittest.TestCase):
	def test_default(self):
		hm = Hashmap()

		for loop in range(16):
			hm.put(loop, loop*2)

		self.assertEqual(hm.containsKey(10), True)
		self.assertEqual(hm.containsKey(18), False)

		self.assertEqual(hm.remove(10), True)
		self.assertEqual(hm.remove(25), False)

		self.assertEqual(hm.containsKey(10), False) 
		self.assertEqual(hm.containsKey(2), True) 

if __name__ == "__main__":
	unittest.main()