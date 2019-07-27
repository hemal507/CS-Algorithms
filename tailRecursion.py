def tailRecursionFactorial(n) :
        return tailFact(n,1)

def tailFact(number,break_value) :
        if number == 1 :
                return break_value
        return tailFact(number-1 , number * break_value)


import unittest
class TailRecursion(unittest.TestCase) :
	def test_case1(self) :
		self.assertEqual(tailRecursionFactorial(1),1)
		print('Test case 1 passed')

	def test_case2(self) :
		self.assertEqual(tailRecursionFactorial(10),3628800)
		print('Test case2 passed')

if __name__ == '__main__' :
	unittest.main()
