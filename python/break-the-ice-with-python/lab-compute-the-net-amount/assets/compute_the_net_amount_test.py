import unittest
import sys
from io import StringIO

# Add the path of the code file
sys.path.append("/home/labex/project")

# Import the code to be tested
from compute_the_net_amount import compute_the_net_amount


class TestYour(unittest.TestCase):
    def test_output(self):
        # Redirect standard input and output to buffer
        stdin = sys.stdin
        stdout = sys.stdout
        sys.stdin = StringIO()
        sys.stdout = StringIO()

        # Input test data
        test_input = "D 300\nD 200\nW 100\nD 50\n\n"
        sys.stdin.write(test_input)
        sys.stdin.seek(0)

        # Run the code
        compute_the_net_amount()

        # Restore standard input and output
        output = sys.stdout.getvalue()
        sys.stdin = stdin
        sys.stdout = stdout

        # Check if the output matches the expected result
        expected_output = "450\n"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
