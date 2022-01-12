import pygame
import os
from src.projectiles import projectile
from assets import pokemon_sprite

charmander = pygame.image.load(os.path.join("assets/pokemon_sprite/charmander_front.png"))

class pokemonTower(pygame.sprite.Sprite):
	def __init__(self, image, ref):
		'''
		initialize tower object
		args: (ref) file reference
		return: (NONE)
		'''

		pygame.sprite.Sprite.__init__(self)									#initialization
		self.file = open(ref, "r")
		#create surface object image
		self.image = image
		self.rect = self.image.get_rect()

		#attributes
		self.name = self.file.readline() + str(id(self))
		self.damage = self.file.readline()
		self.radius = self.file.readline()
		self.attackSpeed = self.file.readline()
		self.cost = self.file.readline()
		self.projectile = self.file.readline()

	def place(self, x, y):
		self.x = x
		self.y = y

	def shoot(self, ene_x, ene_y):
		'''
		generate projectile object
		args: (proj_name) name of the asset file to call
		      (ene_x, ene_y) x and y coords of the enemy position
		return: (self.projectile.attack(ene_x, ene_y)) call projectile method. 
                             If True, enemy is hit
		'''

		x = self.rect.x / 2
		y = self.rect.y / 2
		self.projectile = projectile.projectiles(self.projectile, x, y)

		while True:
			for i in range(atk_spd):
				if i == 0:
					return self.projectile.attack(ene_x, ene_y)
