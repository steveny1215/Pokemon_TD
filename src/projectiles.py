import pygame

class projectile(pygame.sprite.Sprite):
	def __init__(self, img_file, x, y):
		'''
		initialize projectile object
		args: (x, y) position of projectile object
		      (img_file) projectile asset
		return: (NONE)
		'''

		pygame.sprite.Sprite.__init__(self)									#initialization

		#create surface object image
		self.image = pygame.image.load(img_file).convert_alpha()
		self.rect = self.image.get_rect()

		self.rect.x = x
		self.rect.y = y

	def attack(self, targ_x, targ_y):
		'''
		fire projectile
		args: (targ_x, targ_y) where the projectile will travel to
		return: (hit) if projectile collide with enemy, return true
		'''
		targ_x += 64
		targ_y += 64	
		hit = False
		while True:
			self.rect.x += targ_x/2
			self.rect.y += targ_y/2
			if pygame.sprite.collide_rect():
				hit = True
				break
		return hit