import pygame

from Lib.settings import *


class Game:
    def __init__(self):
        self.display_surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.board = [[0 for i in range(COLUMNS)] for j in range(ROWS)]

    def run(self):
        self.display_surface.fill((0, 0, 0))
        self.update_board()
        self.draw_board()

    def spawn_sand(self, row, col):
        if self.is_within_bounds(row, col) and self.is_empty(row, col):
            self.board[row][col] = 1
    
    def draw_board(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.board[i][j] == 1:
                    pygame.draw.rect(self.display_surface, (194, 172, 128),
                                     pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def update_board(self):
        for i in range(ROWS - 1, -1, -1):
            for j in range(COLUMNS - 1, -1, -1):
                if self.board[i][j] == 1:
                    new_row, new_col = self.update_sand(i, j)
                    self.board[i][j] = 0
                    self.board[new_row][new_col] = 1

    def update_sand(self, row, col):
        if self.is_empty(row + 1, col):
            return row + 1, col
        elif self.is_empty(row + 1, col - 1):
            return row + 1, col - 1
        elif self.is_empty(row + 1, col + 1):
            return row + 1, col + 1
        else:
            return row, col

    def is_within_bounds(self, row, col):
        return 0 <= row < ROWS and 0 <= col < COLUMNS

    def is_empty(self, row, col):
        return self.is_within_bounds(row, col) and self.board[row][col] == 0
