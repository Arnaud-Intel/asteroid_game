import pygame # pyright: ignore[reportMissingImports]
import sys
from constants import *
from logger import log_state
from player import *
from asteroid import *
from asteroidfield import *
from logger import log_event
from shot import *

def main():
#Welcome message
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
#Game init and variable settings
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Let's define some groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
#Set the player instance
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()
#Game loop
    while True:
        for event in pygame.event.get(): #quit detection loop
            if event.type == pygame.QUIT:
                return
        log_state()     #logman
        screen.fill("black")        #background
        updatable.update(dt)        #updates round
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        for anything in drawable:   #draw loop
            anything.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000



if __name__ == "__main__":
    main()
