import pygame
from os.path import join

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name = None):
        super().__init__()
    
        self.rect = pygame.Rect(x,y,width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Block(Object):
    def __init__(self,x, y, size, game):
        super().__init__(x, y, size, size)
        self.window = game.window
        block = get_block(size, "gold")
        self.image.blit(block, (0,0))
        self.mask = pygame.mask.from_surface(self.image)

def get_block(size, type = "grassy"):
    '''creates a block. Choose between: grassy, cave, brick, diamond_rock, gold, pink_grass'''
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    if type == "grassy":    
        rect = pygame.Rect(96, 0, size, size) #loads grassy mountain
    if type == "pink_grass":
        rect = pygame.Rect(96, 127, size, size) #loads grassy mountain    
    if type == "cave":
        rect = pygame.Rect(0, 0, size, size) #cave
    if type == "brick":
        rect = pygame.Rect(272, 64, size, size) #loads grassy mountain
    if type == "diamond_rock":
        rect = pygame.Rect(192, 0, size, size) #loads grassy mountain
    if type == "gold":
        rect = pygame.Rect(272, 126, size, size) #loads grassy mountain

    surface.blit(image, (0,0), rect)
    return pygame.transform.scale2x(surface)