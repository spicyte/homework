import unittest
import os

class TestFileContextManager(unittest.TestCase):
    def test_file_context_manager(self):
        filename = 'test_file.txt'

        with TestFileContextManager(filename, 'w') as file:
            file.write("Testing FileContextManager")

        with TestFileContextManager(filename, 'r') as file1, \
                TestFileContextManager(filename, 'r') as file2:
            self.assertEqual(file1.read(), "Testing FileContextManager")
            self.assertEqual(file2.read(), "Testing FileContextManager")

        self.assertFalse(os.path.isfile(filename))

if __name__ == '__main__':
    unittest.main()


