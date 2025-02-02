import unittest
from unittest.mock import patch
import sys


sys.path.append("/home/labex/project")
from recursive_functions import f


class TestMyCode(unittest.TestCase):
    def test_f(self):
        # Simulate user input
        user_input = 5
        expected_output = 500

        # Redirect standard input to simulate user input
        with patch("builtins.input", return_value=user_input):
            # Call the function and check the output
            self.assertEqual(f(user_input), expected_output)


if __name__ == "__main__":
    unittest.main()
