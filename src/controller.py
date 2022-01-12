import pygame
import os
from src.button import TowerMenu
from src.towers import pokemonTower
from src.over import gameOver
from src.enemy import Rattata
pygame.init()
pygame.font.init()


#Loads the assets
music = pygame.image.load(os.path.join("assets", "music.png"))
mute = pygame.image.load(os.path.join("assets", "mute.png"))
heart = pygame.image.load(os.path.join("assets", "heart.png"))
candy = pygame.image.load(os.path.join("assets", "candy.png"))
side_img = pygame.transform.scale(pygame.image.load(os.path.join("assets","box.png")), (120, 500))
bulbasaur = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pokemon_icons", "bulbasaur_icon.png")), (75, 75))
charmander = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pokemon_icons", "charmander_icon.png")), (75, 75))
charmander_sprite = pygame.image.load(os.path.join("assets/pokemon_sprite/charmander_front.png"))
pidgey = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pokemon_icons", "pidgey_icon.png")), (75, 75))
pygame.mixer.music.load(os.path.join("assets", "Lavender.wav"))

class Controller:
    def __init__(self):
        self.width = 1350
        self.height = 700
        self.music = (0, 0, music.get_width(), music.get_height())
        self.mute = (0, 100, mute.get_width(), mute.get_height())
        self.win = pygame.display.set_mode((self.width, self.height))
        self.towers = pygame.sprite.Group()
        self.lives = 600
        self.money = 50 
        self.menu = TowerMenu(self.width - side_img.get_width() + 70, 250, side_img)
        bulb_btn = self.menu.add_btn(bulbasaur, "bulbasaur", 50)
        char_btn = self.menu.add_btn(charmander, "charmander", 35)
        pidg_btn = self.menu.add_btn(pidgey, "pidgey", 40)
        self.bg = pygame.image.load(os.path.join("assets", "level.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = []
        self.font = pygame.font.SysFont("comicsans", 70)
        self.towerSprite = {}

    def run(self):
        '''
        main program loop. detects clicks. place tower. Enemy spawn and movement.
        args: NONE
        return: NONE
        '''
        self.waypoints = [(174, 248),(177, 377),(245, 375), (243, 311), (416, 310), (415, 537), (970, 541), (969, 505), (1182, 507),  (1187, 316),  (1335, 317), (1385, -50), (-50,-50), (174,-50), (174,248)]
        self.enemy = pygame.sprite.Group(Rattata((170, 250), self.waypoints))
        run = True
        clock = pygame.time.Clock()
        self.win.blit(self.bg, (0,0))
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if self.music[0] <= x <= self.music[0] + self.music[2]:
                        if self.music[1] <= y <= self.music[1] + self.music[3]:
                            pygame.mixer.music.unpause()
                    if self.mute[0] <= x <= self.mute[0] + self.mute[2]:
                        if self.mute[1] <= y <= self.mute[1] + self.mute[3]:
                            pygame.mixer.music.pause()
                    if 1260 <= x <= 1335:
                        if 270 <= y <= 345:
                            if self.money >= 35:
                                print("Tower clicked")
                                self.towers.add(pokemonTower(charmander, "src/charmander.json"))

                if len(self.towers) > 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        #self.towers.place(x, y)
                        self.towerSprite[charmander_sprite] = (x, y)
                        self.money -= 35
                    '''
                    for i in self.towers:
                        if pygame.sprite.spritecollide(i, self.enemy, False, pygame.sprite.collide_circle):
                            if self.towers[i].shoot(self.enemy.self.x, self.enemy.self.y):							#need to pass in enemy coords
                                self.win.blit(self.towers[i].img,(self.towers[i].x,self.towers[i].y))
                                self.enemy.health -= self.towers[i].damage
                                if self.enemy.health == 0:
                                    self.money += 3
                                    self.enemy.kill()
                    '''
            
                                
                            
                    
            self.enemy.update()
            self.win.blit(self.bg, (0,0))
            self.enemy.draw(self.win)

            if str(self.waypoints) >= str(1315):
                self.lives -= 1
                if self.lives == 0:
                    score = pygame.time.get_ticks() / 1000
                    pygame.mixer.music.stop()
                    over = gameOver(score)
                    over.run()
                    del over

                    

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicks.append(pos)
                print(self.clicks)
            
            self.draw()
            
        pygame.quit()
    def draw(self):
        '''
        draws all sprites updates the screen
        args: NONE
        return: NONE
        '''
        #Draw Tower
        for k,v in self.towerSprite.items():
            self.win.blit(k, (v))
        #Draw red dots on click
        for p in self.clicks:
            pygame.draw.circle(self.win, (255,0,0), (p[0], p[1]), 5, 0)

        #Draw music & mute button
        self.win.blit(music, (self.music[0], self.music[1]))
        self.win.blit(mute, (self.mute[0], self.mute[1]))
            
        #Draw lives & text
        text = self.font.render(str(self.lives), 1, (255,255,255))                  
        life = pygame.transform.scale(heart, (32,32))
        start_x = self.width - life.get_width() - 10
                                
        self.win.blit(text, (start_x - text.get_width() - 10, 10))
        self.win.blit(life, (start_x, 10))

        #Draw money & text                 
        money = pygame.transform.scale(candy, (32,32))
        text = self.font.render(str(self.money), 1, (255,255,255))
                                
        self.win.blit(text, (start_x - text.get_width() - 10, 50))
        self.win.blit(money, (start_x, 50))

        #Draw menu
        self.menu.draw(self.win)

        #Updates the content of the display
        pygame.display.update()
