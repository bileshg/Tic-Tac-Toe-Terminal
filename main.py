import os

from terminaltables import SingleTable
from termcolor import colored


class TicTacToe:
    def __init__(self):
        self.board = [[f'{i * 3 + j + 1}' for j in range(3)] for i in range(3)]
        self.turn = 0

    def play(self):
        while True:
            self.display_board()
            box = int(input("Box: ".rjust(12)))
            winner = self._play_helper(box)
            if winner is not None:
                self.display_board()
                if winner == 'Tie':
                    print(" Tied! ".center(13, '='))
                else:
                    print(f"{winner} wins!")
                break

    def _play_helper(self, box):
        row, col = (box - 1) // 3, (box - 1) % 3
        if box < 1 or box > 9 or self.board[row][col] in ['X', 'O']:
            print("Invalid move!!! Play again...")
            return None
        else:
            self.board[row][col] = colored('X', 'blue') if self.turn % 2 == 0 else colored('O', 'red')
            self.turn += 1

            winner = self.get_winner()

            if winner is not None:
                return winner
            elif self.turn == 9:
                return 'Tie'
            else:
                return None

    def get_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            elif self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]

        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        else:
            return None

    def display_board(self):
        table = SingleTable(self.board)
        table.inner_row_border = True
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + table.table)


if __name__ == '__main__':
    TicTacToe().play()
