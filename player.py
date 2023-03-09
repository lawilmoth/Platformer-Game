import pygame
from os import listdir
from os.path import isfile, join





class Player(pygame.sprite.Sprite):
    COLOR = (255, 0 , 0)
    GRAVITY = 1
    ANIMATION_DELAY = 3


    def __init__(self, x, y, width, height, game):
        super().__init__()
        self.window = game.window
        self.rect = pygame.Rect(x,y,width,height)
        self.SPRITES = self.load_sprite_sheets("MainCharacters", "PinkMan", 32, 32, True)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animaiton_count = 0
        self.fall_count = 0
    
    def flip(self, sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

    def load_sprite_sheets(self, dir1, dir2, width, height, direction=False):
        path = join("assets",dir1,dir2)
        images = [f for f in listdir(path) if isfile(join(path,f))]

        all_sprites = {}

        for image in images:
            sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

            sprites = []
            for i in range(sprite_sheet.get_width()//width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i*width, 0, width, height)
                surface.blit(sprite_sheet, (0,0), rect)
                sprites.append(pygame.transform.scale2x(surface))

            if direction:
                all_sprites[image.replace('.png','')+ "_right"] = sprites
                all_sprites[image.replace('.png','')+ "_left"] = self.flip(sprites)

            else:
                all_sprites[image.replace('.png','')+ ""] = sprites
            
        return all_sprites



    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = 'left'
            self.animaiton_count = 0


    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = 'right'
            self.animaiton_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count/fps) *self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1
        self.update_sprite()

    def update(self):
        self.rect = self.sprite.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)


    def draw(self, win):
        win.blit(self.sprite, (self.rect.x, self.rect.y))

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.x_vel !=0:
            sprite_sheet = "run"
        
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animaiton_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animaiton_count += 1
        self.update()


