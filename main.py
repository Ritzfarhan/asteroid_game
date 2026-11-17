import sys
from asteroid import Asteroid
import asteroidfield
from player import Player
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state,log_event
from asteroidfield import ASTEROID_MAX_RADIUS, AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2



    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)


    player1 = Player(x,y)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return
        dt = clock.tick(60)/1000
        #player1.update(dt)
        updatable.update(dt)

        for each in asteroids:
            if each.collides_with(player1):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        screen.fill("black")

        #player1.draw(screen)
        for each in drawable:
            each.draw(screen)






        #print(dt)
        pygame.display.flip()



if __name__ == "__main__":
    main()
