from TwoSum import Solution
import unittest.test.test_program

class TestProgram(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution().twoSum([3,5,-4,8,11,1,-1,6],10), [-1, 11])

    def test_1(self):
        self.assertEqual(Solution().twoSum([3,5,-4,8,11,1,-1,6,1,5,-9,-4,-6.6,8],20), [8, 11])

    def test_1(self):
        self.assertEqual(Solution().twoSum([3,5,-4,8,11,1,-1,6,1,5,-9,-4,-6.6,8],11), [3, 8])



if __name__=="__main__":
    unittest.main()

