import unittest
from hashlist import*

class TestHashlist(unittest.TestCase):
	def test_default(self):

		hl = Hashlist()
		
		hl.put("Python")
		hl.put("C++")
		hl.put("Java")

		toCheck = ["Python","C++","C#","Java"]

		contained = []

		for item in toCheck:
			contained.append(hl.contains(item))

		self.assertEqual(contained, [True, True, False, True])

		self.assertEqual(hl.remove("Java"), True)
		self.assertEqual(hl.remove("Ruby"), False)

		self.assertEqual(hl.contains("Java"),False)

if __name__ == "__main__":
	unittest.main()