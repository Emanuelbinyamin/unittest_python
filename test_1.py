import unittest  # Import the unittest module for writing and running tests.
import Testing_unittest_1  # Import the module that contains the function to be tested.

class Test_main(unittest.TestCase):  # Define a test case class derived from unittest.TestCase.
    
    def test_A(self):  # Define a test method.
        test_param = 10  # Set up the test input.
        result = Testing_unittest_1.adds(test_param)  # Call the function with the test input.
        self.assertEqual(result, 15)  # Check if the result is 15, which is the expected output for the input 10.
    
    def test_B(self):  # Define another test method.
        test_param = "asdfg"  # Set up test input that is not a valid number.
        result = Testing_unittest_1.adds(test_param)  # Call the function with the invalid input.
        self.assertIsInstance(result, ValueError)  # Check if the result is an instance of ValueError, as the function should raise this error for invalid inputs.
    
    def test_C(self):  # Define another test method.
        test_param = "10"  # Set up test input as a string that represents a valid number.
        result = Testing_unittest_1.adds(test_param)  # Call the function with the string input.
        self.assertEqual(result, 15)  # Check if the result is 15, which is the expected output after converting the string "10" to an integer and adding 5.
    
    def test_D(self):  # Define another test method.
        test_param = None  # Set up test input as None.
        result = Testing_unittest_1.adds(test_param)  # Call the function with None as input.
        self.assertEqual(result, "please enter a number")  # Check if the result matches the expected message for None input.
    
    def test_E(self):  # Define another test method.
        test_param = ""  # Set up test input as an empty string.
        result = Testing_unittest_1.adds(test_param)  # Call the function with an empty string.
        self.assertEqual(result, "please enter a number")  # Check if the result matches the expected message for an empty string input.

if __name__ == '__main__':  # This block runs the tests if the script is executed directly.
    unittest.main()  # Run all the test methods defined in the Test_main class.
