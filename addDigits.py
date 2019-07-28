def addDigits(a, b, n):
        for i in range(n) :
                for j in range(0,10) :
                        r = int(str(a) + str(j))
                        if r % b == 0 :
                                a = r
                                break
        return a

'''
import unittest
class AddDigits(unittest.TestCase) :
        def test_case1(self) :
                self.assertEqual(addDigits(12,11,2),1210)
                print('Test case1 passed')
        def test_case2(self) :
                self.assertEqual(addDigits(9,8,2),960)
                print('Test case2 passed')

if __name__ == '__main__':
        unittest.main()
'''
~          

