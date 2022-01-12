import pygame
import os
from pygame.math import Vector2

rattata = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pokemon_sprite", "rattata_right.png")), (75, 75))
class Rattata(pygame.sprite.Sprite):
    def __init__(self, pos, waypoints):
        super().__init__()
        self.image = rattata
        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0, 0)
        self.max_speed = 3
        self.pos = Vector2(pos)
        self.waypoints = waypoints
        self.waypoint_index = 0
        self.target = self.waypoints[self.waypoint_index]
        self.target_radius = 5

    def update(self):
        '''
        updates enemy position based on coordinates
        args: NONE
        return: NONE
        '''
        # A vector pointing from self to the target.
        heading = self.target - self.pos
        distance = heading.length()  # Distance to the target.
        heading.normalize_ip()
        if distance <= 2:  # We're closer than 2 pixels.
            # Increment the waypoint index to swtich the target.
            # The modulo sets the index back to 0 if it's equal to the length.
            self.waypoint_index = (self.waypoint_index + 1) % len(self.waypoints)
            self.target = self.waypoints[self.waypoint_index]
        if distance <= self.target_radius:
            # If we're approaching the target, we slow down.
            self.vel = heading * (distance / self.target_radius * self.max_speed)
        else:  # Otherwise move with max_speed.
            self.vel = heading * self.max_speed
        '''
        moves enemy position
        args: (end_x) ending x coordinate
        return: boolean
        '''
        xo = []
        self.pos += self.vel
        self.rect.center = self.pos
        x,y = self.pos
        xo.append(y)
        return xo
