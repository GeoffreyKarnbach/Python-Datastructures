import unittest
from dictionary import*

class TestDictionary(unittest.TestCase):
	def test_default(self):
		assoc = Dictionary()

		self.assertEqual(assoc.put("France", "Pari"), None)
		self.assertEqual(assoc.put("Germany", "Berlin"), None)
		self.assertEqual(assoc.put("Austria", "Vienna"), None)

		self.assertEqual(assoc.put("France", "Paris"), "Pari")
		self.assertEqual(assoc.remove("England"), None)
		self.assertEqual(assoc.remove("Germany"), "Berlin")

		self.assertEqual(assoc.containsKey("England"), False)
		self.assertEqual(assoc.containsKey("France"), True)

		self.assertEqual(assoc.containsValue("London"), False)
		self.assertEqual(assoc.containsValue("Paris"), True)

		self.assertEqual(assoc.size(),2)

if __name__ == "__main__":
	unittest.main()