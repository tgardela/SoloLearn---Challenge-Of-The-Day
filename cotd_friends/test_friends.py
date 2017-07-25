import unittest
import friends


class TestFriends(unittest.TestCase):

    def test_GetDividers(self):
        testCases = [ [[1], 2], [[1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110], 220], [[1, 2, 4, 71, 142], 284]]
        for i in range (0, len(testCases)):
            self.assertEqual([1], friends.getDividers(2))


    def test_getNumbersAndDividerSumDict(self):
        testCases = [ [{2:1}, 2], [{220:284}, 220], [{284:220}, 284]]
        for i in range(0, len(testCases)):
            self.assertEqual(testCases[i][0], friends.getNumberAndDividerSumDict(testCases[i][1]))


    def test_getDictOfNumbersAndTheirDividerSums(self):
        testCases = [ [{2:1}, 3], [{2:1, 3:1}, 4], [{2:1, 3:1, 4:3, 5:1, 6:6, 7:1, 8:7}, 9]]
        for i in range(0, len(testCases)):
            self.assertEqual(testCases[i][0], friends.getDictOfNumbersAndTheirDividerSums(testCases[i][1]))


    def test_Friends(self):
        self.assertEqual(1, friends.friends(1))






if __name__=='__main__':
    unittest.main(verbosity=2)