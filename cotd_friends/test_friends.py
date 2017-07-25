import unittest
import friends


class TestFriends(unittest.TestCase):
    def test_Friends(self):
        self.assertEqual(1, friends.friends(1))



if __name__=='__main__':
    unittest.main(verbosity=2)