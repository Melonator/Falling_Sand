from idlelib import window

import pygame
from sys import exit
from Lib.settings import *
from Lib.game import Game
class Main:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.game = Game()
        self.accumulated_time = 0
        self.update_threshold = 0.02
        pygame.display.set_caption('Super Astig Cellular Automata')


    def run(self):
        mouse_held_down = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_held_down = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_held_down = False

            if mouse_held_down:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row, col = mouse_y // CELL_SIZE, mouse_x // CELL_SIZE
                self.game.spawn_sand(row, col)

            pygame.display.update()
            delta_time = self.clock.tick(60) / 1000.0
            self.accumulated_time += delta_time

            if self.accumulated_time >= self.update_threshold:
                self.game.run()
                self.accumulated_time = 0

if __name__ == '__main__':
    main = Main()
    main.run()

