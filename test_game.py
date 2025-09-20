import unittest
from game import board, game_move, check_winning


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        # Сбрасываем игровое поле перед каждым тестом
        for i in range(9):
            board[i] = i + 1

    def test_valid_move(self):
        """Проверка, что ход ставит X на правильное место"""
        result = game_move(1, 'X')
        self.assertTrue(result)
        self.assertEqual(board[0], 'X')

    def test_invalid_move_out_of_range(self):
        """Ход вне диапазона"""
        self.assertFalse(game_move(10, 'X'))
        self.assertFalse(game_move(0, 'O'))

    def test_invalid_move_occupied_cell(self):
        """Ход в занятую клетку"""
        game_move(1, 'X')
        self.assertFalse(game_move(1, 'O'))

    def test_winning_row(self):
        """Победа по горизонтали"""
        game_move(1, 'X')
        game_move(2, 'X')
        game_move(3, 'X')
        self.assertEqual(check_winning(), 'X')

    def test_winning_column(self):
        """Победа по вертикали"""
        game_move(1, 'O')
        game_move(4, 'O')
        game_move(7, 'O')
        self.assertEqual(check_winning(), 'O')

    def test_winning_diagonal(self):
        """Победа по диагонали"""
        game_move(1, 'X')
        game_move(5, 'X')
        game_move(9, 'X')
        self.assertEqual(check_winning(), 'X')

    def test_no_winner(self):
        """Пустое поле → победителя нет"""
        self.assertFalse(check_winning())


if __name__ == '__main__':
    unittest.main()