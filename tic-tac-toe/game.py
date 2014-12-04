#!/usr/bin/env python
import os


clear = lambda: os.system('clear')


class Game:
    first_player_symbol = 'O'
    second_player_symbol = 'X'

    def __init__(self):
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def _print_board(self):
        print("Your symbol is {}, the computers symbol is {} !".format(self.first_player_symbol, self.second_player_symbol))
        print("""-------------
| {} | {} | {} |
-------------
| {} | {} | {} |
-------------
| {} | {} | {} |
-------------""".format(self.board[0], self.board[1], self.board[2], self.board[3],
                        self.board[4], self.board[5], self.board[6], self.board[7], self.board[8]))

    def _is_player_won(self, symbol):
        if (self.board[0] == self.board[1] == self.board[2] == symbol) or (self.board[3] == self.board[4] == self.board[5] == symbol) or (self.board[6] == self.board[7] == self.board[8] == symbol):
            return True
        if (self.board[0] == self.board[3] == self.board[6] == symbol) or (self.board[1] == self.board[4] == self.board[7] == symbol) or (self.board[2] == self.board[5] == self.board[8] == symbol):
            return True
        if (self.board[0] == self.board[4] == self.board[8] == symbol) or (self.board[2] == self.board[4] == self.board[6] == symbol):
            return True
        return False

    def _is_game_over(self):
        if self._is_player_won(self.first_player_symbol):
            return 1
        if self._is_player_won(self.second_player_symbol):
            return 2
        return False

    def _place_move_on_board(self, move, symbol):
        self.board[int(move)] = symbol

    def _is_position_free(self, position):
        return position in range(1, 10) and self.board[int(position) - 1] in '912345678'

    def _two_in_a_row(self, row, player):
        if player == 1:
            symbol = self.first_player_symbol
        else:
            symbol = self.second_player_symbol
        start_position = row * 3
        if self.board[start_position] == self.board[start_position + 1] == symbol and self.board[start_position + 2] == str(start_position + 2 + 1):
            self.board[start_position + 2] = self.second_player_symbol
            return True
        if self.board[start_position] == self.board[start_position + 2] == symbol and self.board[start_position + 1] == str(start_position + 1 + 1):
            self.board[start_position + 1] = self.second_player_symbol
            return True
        if self.board[start_position + 2] == self.board[start_position + 1] == symbol and self.board[start_position] == str(start_position + 1):
            self.board[start_position] = self.second_player_symbol
            return True
        return False

    def _two_in_a_col(self, col, player):
        if player == 1:
            symbol = self.first_player_symbol
        else:
            symbol = self.second_player_symbol
        start_position = col
        if self.board[start_position] == self.board[start_position + 3] == symbol and self.board[start_position + 6] == str(start_position + 6 + 1):
            self.board[start_position + 6] = self.second_player_symbol
            return True
        if self.board[start_position] == self.board[start_position + 6] == symbol and self.board[start_position + 3] == str(start_position + 3 + 1):
            self.board[start_position + 3] = self.second_player_symbol
            return True
        if self.board[start_position + 6] == self.board[start_position + 3] == symbol and self.board[start_position] == str(start_position + 1):
            self.board[start_position] = self.second_player_symbol
            return True
        return False

    def _two_in_diagonal(self, player):
        if player == 1:
            symbol = self.first_player_symbol
        else:
            symbol = self.second_player_symbol
        if self.board[0] == self.board[4] == symbol and self.board[8] == '9':
            self.board[8] = self.second_player_symbol
            return True
        if self.board[8] == self.board[4] == symbol and self.board[0] == '1':
            self.board[0] = self.second_player_symbol
            return True
        if self.board[0] == self.board[8] == symbol and self.board[4] == '5':
            self.board[4] = self.second_player_symbol
            return True

        if self.board[2] == self.board[4] == symbol and self.board[6] == '7':
            self.board[6] = self.second_player_symbol
            return True
        if self.board[6] == self.board[4] == symbol and self.board[2] == '1':
            self.board[2] = self.second_player_symbol
            return True
        if self.board[2] == self.board[6] == symbol and self.board[4] == '5':
            self.board[4] = self.second_player_symbol
            return True
        return False

    def _place_in_oposite_corner(self):
        if self.board[0] == self.first_player_symbol and self.board[8] == '9':
            self.board[8] = self.second_player_symbol
            return True
        if self.board[8] == self.first_player_symbol and self.board[0] == '1':
            self.board[0] = self.second_player_symbol
            return True
        if self.board[2] == self.first_player_symbol and self.board[6] == '7':
            self.board[6] = self.second_player_symbol
            return True
        if self.board[6] == self.first_player_symbol and self.board[2] == '3':
            self.board[2] = self.second_player_symbol
            return True
        return False

    def _place_in_empty_corner(self):
        if self.board[0] == '1':
            self.board[0] = self.second_player_symbol
            return True
        if self.board[2] == '3':
            self.board[2] = self.second_player_symbol
            return True
        if self.board[6] == '7':
            self.board[6] = self.second_player_symbol
            return True
        if self.board[8] == '9':
            self.board[8] = self.second_player_symbol
            return True
        return False

    def _double_treat(self, symbol):
        if self.board[5] == self.board[7] == symbol and self._is_position_free(9) and self._is_position_free(3) and self._is_position_free(9):
            self.board[8] = self.second_player_symbol
            return True
        if self.board[3] == self.board[7] == symbol and self._is_position_free(1) and self._is_position_free(9) and self._is_position_free(7):
            self.board[6] = self.second_player_symbol
            return True
        if self.board[1] == self.board[3] == symbol and self._is_position_free(1) and self._is_position_free(3) and self._is_position_free(7):
            self.board[0] = self.second_player_symbol
            return True
        if self.board[1] == self.board[5] == symbol and self._is_position_free(1) and self._is_position_free(3) and self._is_position_free(9):
            self.board[2] = self.second_player_symbol
            return True
        return False

    def _place_in_empty_side(self):
        if self.board[1] == '2':
            self.board[1] = self.second_player_symbol
            return True
        if self.board[3] == '4':
            self.board[3] = self.second_player_symbol
            return True
        if self.board[5] == '6':
            self.board[5] = self.second_player_symbol
            return True
        if self.board[7] == '8':
            self.board[7] = self.second_player_symbol
            return True
        return False

    def _ai_move(self):
        for row in range(0, 3):
            if self._two_in_a_row(row, 2) or self._two_in_a_col(row, 2):
                return
        if self._two_in_diagonal(2):
            return
        for row in range(0, 3):
            if self._two_in_a_col(row, 1) or self._two_in_a_row(row, 1):
                return
        if self._two_in_diagonal(1):
            return
        if self._double_treat(self.first_player_symbol):
            return
        if self._double_treat(self.second_player_symbol):
            return
        if self._is_position_free(5):
            self._place_move_on_board(4, self.second_player_symbol)
            return
        if self._place_in_oposite_corner():
            return
        if self._place_in_empty_corner():
            return
        if self._place_in_empty_side():
            return

    def start_game(self):
        clear()
        self._print_board()
        for i in range(5):
            next_move = input("Choose your next move> ")
            while(self._is_position_free(int(next_move)) is False):
                next_move = input("This position is not free ot it's out of board please choose new> ")
            self._place_move_on_board(int(next_move) - 1, self.first_player_symbol)
            if self._is_game_over():
                break
            print("Computer make move")
            self._ai_move()
            clear()
            self._print_board()
            if self._is_game_over():
                clear()
                self._print_board()
                break
        if self._is_game_over() == 1:
            print("You WON !")
        elif self._is_game_over() == 2:
            print("You lose")
        else:
            print("Draw !")


