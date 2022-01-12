import pygame
import os

quit_btn = quitt_btn = pygame.image.load(os.path.join("assets", "quit.png"))
pygame.font.init()

class gameOver:
    def __init__(self, score):
        self.width = 1350
        self.height = 864
        self.win = pygame.display.set_mode((self.width, self.height))
        self.btn2 = (self.width/2 - quit_btn.get_width()/2, 550, quit_btn.get_width(), quit_btn.get_height())
        self.clicks = []
        self.score = score
        self.file = open("src/previous_score.json", "r")
        
    def run(self):
        '''
        main program loop for the screen. reads and saves score from and to .json file
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
                            self.file.close()
                            self.scoreKeep()
                            pygame.quit()
            self.draw()
        self.file.close()
        self.scoreKeep()
        pygame.quit()

    def draw(self):
        '''
        draws the screen
        args: NONE
        return: NONE
        '''
        myfont = pygame.font.SysFont(None, 30)
        game_over = myfont.render("Game Over", False, (255, 255, 255))
        message = ("Score:" + str(self.score))
        message_1 = ("Previous Score:" + str(self.file.readline()))
        new_score = myfont.render(message, False, (255,255,255))
        old_score = myfont.render(message_1, False, (255,255,255))
        self.win.blit(game_over, (625, self.height/2))
        self.win.blit(quit_btn, (self.btn2[0], self.btn2[1]))
        self.win.blit(new_score, (self.width/2, 0))
        self.win.blit(old_score, (self.width/2, 35))
        pygame.display.update()

    def scoreKeep(self):
        '''
        open file, writes the score, and closes file
        args: NONE
        return: NONE
        '''
        file = open("src/previous_score.json", "w")
        file.write(str(self.score))
        file.close()