import unittest
from unittest.mock import patch
import io
from matrix import create_matrix, edit_matrix
from matrix import create_matrix, edit_matrix, edit_all

class TestMatrixFunctions(unittest.TestCase):
    def test_create_matrix(self):
        matrix = create_matrix(10)
        self.assertEqual(len(matrix), 10)
        self.assertTrue(all(len(row) == 10 for row in matrix))
        self.assertTrue(all(cell == 0 for row in matrix for cell in row))

    def test_edit_matrix_valid_position(self):
        matrix = create_matrix(10)
        matrix = edit_matrix(matrix, 2, 3, 5)
        self.assertEqual(matrix[2][3], 5)

    def test_edit_matrix_invalid_position(self):
        matrix = create_matrix(10)
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            matrix = edit_matrix(matrix, 10, 10, 5)
            self.assertIn("Invalid position!", fake_stdout.getvalue())

    def test_edit_all(self):
        matrix = create_matrix(10)
        matrix = edit_all(matrix, 7)
        self.assertTrue(all(cell == 7 for row in matrix for cell in row))

    
if __name__ == '__main__':
    unittest.main()