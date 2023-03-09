import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

from player import Player
from objects import Block


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("My Platformer")
        self.WIDTH = 1000
        self.HEIGHT =800
        self.FPS = 60
        self.PLAYER_VEL = 5
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.player = Player(100, 100, 50, 50, self)


    def draw(self, window, background, bg_image, player, objects):
        for tile in background:
            window.blit(bg_image, tile)
        
        for obj in objects:
            obj.draw(window)

        player.draw(window)
        pygame.display.update()

    def get_background(self, name):
        image = pygame.image.load(join('assets','Background', name))
        _, _, width, height = image.get_rect()
        tiles = []
        for i in range(self.WIDTH//width +1):
            for j in range(self.HEIGHT // height +1):
                pos = (i*width, j*width)
                tiles.append(pos)
        return tiles, image


    def handle_move(self, player):
        keys = pygame.key.get_pressed()
        
        player.x_vel = 0
        if keys[pygame.K_LEFT]:
            player.move_left(self.PLAYER_VEL)
        if keys[pygame.K_RIGHT]:
            player.move_right(self.PLAYER_VEL)


    def main(self):
        clock = pygame.time.Clock()
        background, bg_image = self.get_background('Yellow.png')
        block_size = 96

        blocks = [Block(0, self.HEIGHT- block_size, block_size, game)]

        run = True
        while run:  
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            self.player.loop(self.FPS)
            self.handle_move(self.player)
            self.draw(self.window,background, bg_image, self.player, blocks)
        pygame.quit()
        quit()

if __name__ =="__main__":
    game = Game()
    game.main()