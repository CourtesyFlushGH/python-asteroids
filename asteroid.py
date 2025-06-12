from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):

    containers = ()
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        self.radius -= ASTEROID_MIN_RADIUS
        vector_one = self.velocity.rotate(random_angle)
        vector_two = self.velocity.rotate(-random_angle)

        asteroid_one = Asteroid(self.position[0], self.position[1], self.radius)
        asteroid_one.velocity = vector_one
        asteroid_two = Asteroid(self.position[0], self.position[1], self.radius)
        asteroid_two.velocity = vector_two