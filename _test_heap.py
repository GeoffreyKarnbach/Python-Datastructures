import unittest
from heap import*

class TestHeap(unittest.TestCase):
	def test_default(self):
		hp = Heap()

		hp.put(1)
		hp.put(6,"Prio 6")
		hp.put(10,"Prio 10")
		hp.put(5,"Prio 5")
		hp.put(8,"Prio 8")

		valuesPrio = []
		valuesInfo = []

		self.assertEqual(hp.size(), 5)
		
		while hp.size() > 0:
			retrieved = hp.get()
			valuesPrio.append(retrieved[0])
			valuesInfo.append(retrieved[1])

		self.assertListEqual(valuesPrio, [10,8,6,5,1])
		self.assertListEqual(valuesInfo, ['Prio 10', 'Prio 8', 'Prio 6', 'Prio 5', 'None'])
		
		self.assertEqual(hp.get(), None)

if __name__ == "__main__":
	unittest.main()