import pygame
import os

next_btn = pygame.image.load(os.path.join("assets", "logo.png"))

class Help:
    def __init__(self):
        self.width = 1350
        self.height = 864
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load(os.path.join("assets", "help.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.btn2 = (self.width/2 - next_btn.get_width()/2, 750, next_btn.get_width(), next_btn.get_height())
        self.clicks = []

    def run(self):
        '''
        main program loop
        args: NONE
        return: NONE
        '''
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(24)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    print(self.clicks)
                    if self.btn2[0] <= x <= self.btn2[0] + self.btn2[2]:
                        if self.btn2[1] <= y <= self.btn2[1] + self.btn2[3]:
                            nexto = Next()
                            nexto.run()
                            del nexto
            self.draw()
        pygame.quit()

    def draw(self):
        '''
        draws the screen
        args: NONE
        return: NONE
        '''
        self.win.blit(self.bg, (0,0))
        self.win.blit(next_btn, (self.btn2[0], self.btn2[1]))
        for p in self.clicks:
            pygame.draw.circle(self.win, (255,0,0), (p[0], p[1]), 5, 0)
        pygame.display.update()

