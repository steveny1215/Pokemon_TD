import pygame
import os

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Pokemon Tower Defense')
    icon = pygame.image.load(os.path.join("assets", "pokemon_icons", "rattata_icon.png"))
    pygame.display.set_icon(icon)
    win = pygame.display.set_mode((1350, 864))
    from src.startScreen import StartScreen
    startScreen = StartScreen(win)
    startScreen.run()
