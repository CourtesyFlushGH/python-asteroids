
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    frame_limit = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)
    Shot.containers = (shot_group, drawable_group, updatable_group)

    # call player class
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = (frame_limit.tick(60)) / 1000

        # make background black
        screen.fill("black")
        
        updatable_group.update(dt)

        for drawable in drawable_group:
            drawable.draw(screen)

        for object in asteroid_group:
            if object.collision(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroid_group:
            for shot in shot_group:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        # call last
        pygame.display.flip()

if __name__ == "__main__":
    main()
