import unittest
import Testing_unittest_1

class Test_main(unittest.TestCase):
    def test_A(self):        
        test_param=10
        result=Testing_unittest_1.adds(test_param)
        self.assertEqual(result,15)
       
    def test_B(self):        
        test_param="asdfg"
        result=Testing_unittest_1.adds(test_param)
        self.assertIsInstance(result,ValueError)    

    def test_C(self):        
        test_param="10"
        result=Testing_unittest_1.adds(test_param)
        self.assertEqual(result,15)    
    
    def test_D(self):        
        test_param=None
        result=Testing_unittest_1.adds(test_param)
        self.assertEqual(result,"please enter a number")    
    def test_E(self):        
        test_param=""
        result=Testing_unittest_1.adds(test_param)
        self.assertEqual(result,"please enter a number")    

if __name__ == '__main__':
    unittest.main()
