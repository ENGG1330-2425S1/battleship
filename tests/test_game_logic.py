import io
import unittest
from unittest.mock import patch
from game_logic import handle_place_ships, ship_labels

class TestPlaceShips(unittest.TestCase):

    def setUp(self):
        self.empty_matrix = [["~"] * 10 for _ in range(10)]

    def test_place_ship_horizontally_success(self):
        matrix = [row[:] for row in self.empty_matrix]
        result = handle_place_ships(matrix, "destroyer", "H", 0, 0)
        expected = [["D", "D"] + ["~"] * 8] + [["~"] * 10 for _ in range(9)]
        self.assertEqual(result, expected)

    def test_place_ship_vertically_success(self):
        matrix = [row[:] for row in self.empty_matrix]
        result = handle_place_ships(matrix, "submarine", "V", 0, 0)
        expected = [["S"] + ["~"] * 9, ["S"] + ["~"] * 9, ["S"] + ["~"] * 9] + [["~"] * 10 for _ in range(7)]
        self.assertEqual(result, expected)

    def test_place_ship_out_of_horizontal_bounds(self):
        matrix = [row[:] for row in self.empty_matrix]
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = handle_place_ships(matrix, "carrier", "H", 0, 6)
            self.assertIn("Warning: Ship placement is out of horizontal bounds.", fake_stdout.getvalue())
        self.assertEqual(result, self.empty_matrix)

    def test_place_ship_out_of_vertical_bounds(self):
        matrix = [row[:] for row in self.empty_matrix]
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = handle_place_ships(matrix, "battleship", "V", 7, 0)
            self.assertIn("Warning: Ship placement is out of vertical bounds.", fake_stdout.getvalue())
        self.assertEqual(result, self.empty_matrix)

    def test_place_ship_on_occupied_position(self):
        matrix = [row[:] for row in self.empty_matrix]
        matrix[0][0] = ship_labels["cruiser"]
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = handle_place_ships(matrix, "destroyer", "H", 0, 0)
            self.assertIn("Warning: Position already occupied by cruiser.", fake_stdout.getvalue())
        self.assertEqual(result, matrix)

if __name__ == '__main__':
    unittest.main()