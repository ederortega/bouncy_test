import unittest
from bouncy import IntegerClass, BouncyProportion


class TestNumberClass(unittest.TestCase):

    def test_increasingNumber(self):
        iclass = IntegerClass()
        self.assertTrue(iclass.isIncreasing(134468))
        self.assertTrue(iclass.isIncreasing(12456))
        self.assertTrue(iclass.isIncreasing(22467889))
        self.assertTrue(iclass.isIncreasing(789))

        self.assertFalse(iclass.isIncreasing(66420))
        self.assertFalse(iclass.isIncreasing(538))

    def test_decreasingNumber(self):
        iclass = IntegerClass()
        self.assertTrue(iclass.isDecreasing(66420))
        self.assertTrue(iclass.isDecreasing(9631))
        self.assertTrue(iclass.isDecreasing(85442))
        self.assertTrue(iclass.isDecreasing(543321))

        self.assertFalse(iclass.isDecreasing(134468))
        self.assertFalse(iclass.isDecreasing(538))

    def test_bouncyNumber(self):
        iclass = IntegerClass()
        self.assertTrue(iclass.isBouncy(583))
        self.assertTrue(iclass.isBouncy(9671))
        self.assertTrue(iclass.isBouncy(85945))
        self.assertTrue(iclass.isBouncy(549361))

        self.assertFalse(iclass.isBouncy(134468))
        self.assertFalse(iclass.isBouncy(66420))


class TestBouncyProportion(unittest.TestCase):

    def test_count(self):
        bouncyP = BouncyProportion()
        self.assertEqual(bouncyP.count(100, 1000), 525)

    def test_proportion(self):
        bouncyP = BouncyProportion()
        self.assertEqual(bouncyP.leastBouncy(50, 1000), 538)
        self.assertEqual(bouncyP.leastBouncy(90, 30000), 21780)


if __name__ == '__main__':
    unittest.main()
