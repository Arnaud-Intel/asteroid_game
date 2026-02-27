import pygame # pyright: ignore[reportMissingImports]
from constants import *
from circleshape import *
from logger import log_event
import random

# Base class for game objects
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        first_vector = self.velocity.rotate(new_angle)
        second_vector = self.velocity.rotate(-new_angle)
        self.radius -= ASTEROID_MIN_RADIUS
        smaller1 = Asteroid(self.position.x, self.position.y, self.radius)
        smaller2 = Asteroid(self.position.x, self.position.y, self.radius)
        smaller1.velocity = first_vector * 1.2
        smaller2.velocity = second_vector * 1.2


