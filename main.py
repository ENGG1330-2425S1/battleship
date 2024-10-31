# entrypoint

from cli import matrix_output_preprocess
from game_logic import welcome
from matrix import create_matrix, edit_all


def main():
    welcome()
    # Set up the ocean grid for both players
    player1_grid = edit_all(create_matrix(10), "~")

    # Place ships on the grid
    print(matrix_output_preprocess(player1_grid))
    print("-" * 20)
    # TODO: Implement ship placement cli

if __name__ == "__main__":
    main()