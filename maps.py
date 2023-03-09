from objects import *


def get_background(name,game):
    image = pygame.image.load(join('assets','Background', name))
    _, _, width, height = image.get_rect()
    tiles = []
    for i in range(game.WIDTH//width +1):
        for j in range(game.HEIGHT // height +1):
            pos = (i*width, j*width)
            tiles.append(pos)
    return tiles, image

class Map():
    block_size = 96
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.window = game.window


class Map1(Map):
    
    def __init__(self, game):
        super().__init__(game)
        self.background, self.bg_image = get_background('Yellow.png',self.game)
                            
        self.floor = [Block(i *self.block_size, self.game.HEIGHT - self.block_size, self.block_size, self.game)
        for i in range(-self.game.WIDTH // self.block_size, (self.game.WIDTH *2)//self.block_size)]