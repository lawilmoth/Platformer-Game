import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

from player import Player
from objects import Block
from settings import Settings
from maps import Map1

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("My Platformer")
        self.settings = Settings()
        self.WIDTH = self.settings.WIDTH
        self.HEIGHT =self.settings.HEIGHT
        self.FPS = self.settings.FPS
        self.PLAYER_VEL = self.settings.PLAYER_VEL
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.player = Player(100, 100, 50, 50, self)
        self.level = 1

    def draw(self):
        for tile in self.map.background:
            self.window.blit(self.map.bg_image, tile)
 
        for obj in self.map.floor:
            obj.draw(self.window)

        self.player.draw(self.window)
        pygame.display.update()


#    def handle_vertical_collision(self):

    def handle_move(self):
        keys = pygame.key.get_pressed()
        
        self.player.x_vel = 0
        if keys[pygame.K_LEFT]:
            self.player.move_left(self.PLAYER_VEL)
        if keys[pygame.K_RIGHT]:
            self.player.move_right(self.PLAYER_VEL)


    def main(self):
        clock = pygame.time.Clock()
        if self.level == 1:
            self.map = Map1(self)


        run = True
        while run:  
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            self.player.loop()
            self.handle_move()
            self.draw()
        pygame.quit()
        quit()

if __name__ =="__main__":
    game = Game()
    game.main()