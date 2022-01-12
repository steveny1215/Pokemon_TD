from src.controller import Controller
import pygame
import os
import time

start_btn = pygame.image.load(os.path.join("assets", "start.png"))
help_btn = pygame.image.load(os.path.join("assets", "helpbutt.png"))
helpo = pygame.image.load(os.path.join("assets", "helpo.png"))
logo = pygame.image.load(os.path.join("assets", "logo.png"))

pygame.mixer.music.load(os.path.join("assets", "Lavender.wav"))

def load_image(name):
    img_path = os.path.join("assets", "bg", name)
    image = pygame.image.load(img_path).convert()
    return image

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('bg (1).png'))
        self.images.append(load_image('bg (2).png'))
        self.images.append(load_image('bg (3).png'))
        self.images.append(load_image('bg (4).png'))
        self.images.append(load_image('bg (5).png'))
        self.images.append(load_image('bg (6).png'))
        self.images.append(load_image('bg (7).png'))
        self.images.append(load_image('bg (8).png'))
        self.images.append(load_image('bg (9).png'))
        self.images.append(load_image('bg (10).png'))
        self.images.append(load_image('bg (11).png'))
        self.images.append(load_image('bg (12).png'))
        self.images.append(load_image('bg (13).png'))
        self.images.append(load_image('bg (14).png'))
        self.images.append(load_image('bg (15).png'))
        self.images.append(load_image('bg (16).png'))
        self.images.append(load_image('bg (17).png'))
        self.images.append(load_image('bg (18).png'))
        self.images.append(load_image('bg (19).png'))
        self.images.append(load_image('bg (20).png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 1350, 864)

    def update(self):
        '''
        updates screen
        args: NONE
        return: NONE
        '''
        time.sleep(.12)
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

class StartScreen:
    def __init__(self, win):
        self.width = 1350
        self.height = 864
        self.win = pygame.display.set_mode((self.width, self.height))
        self.btn = (self.width/2 - start_btn.get_width()/2, 500, start_btn.get_width(), start_btn.get_height())
        self.btn2 = ((self.width/2 - help_btn.get_width()/2) + 640 , 10, help_btn.get_width(), help_btn.get_height())

    def draw(self):
        '''
        draws screen
        args: NONE
        return: NONE
        '''
        self.win.blit(logo, (self.width/2 - logo.get_width()/2, 300))
        self.win.blit(start_btn, (self.btn[0], self.btn[1]))
        self.win.blit(help_btn, (self.btn2[0], self.btn2[1]))
        pygame.display.update()
        
    def run(self):
        '''
        main program loop. can open instruction screen or start the game
        args: NONE
        return: NONE
        '''
        pygame.mixer.music.play(loops=-1)
        my_sprite = TestSprite()
        my_group = pygame.sprite.Group(my_sprite)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            game = Controller()
                            game.run()
                            del game                    
                    if self.btn2[0] <= x <= self.btn2[0] + self.btn2[2]:
                        if self.btn2[1] <= y <= self.btn2[1] + self.btn2[3]:
                            self.win.blit(helpo, (0, 0))

            self.draw()
            my_group.update()
            my_group.draw(self.win)
            pygame.display.flip()


