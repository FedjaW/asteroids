# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * # import magic numbers
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0 # delta time

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # To add all instances of a Player to two groups,
    # group_a and group_b in this example, 
    # we add a static field called containers to the class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    asteroidField = AsteroidField()

    # game loop
    # 1. wait for user input
    # 2. update game world
    # 3. draw
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updateme in updatable:
            updateme.update(dt)

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.colides_with(bullet):
                    asteroid.split()
                    bullet.kill()
            if asteroid.colides_with(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for drawme in drawable:
            drawme.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

# This line ensures the main() 
# function is only called when this file is run directly; 
# it won't run if it's imported as a module. 
# It's considered the "pythonic" way to structure an executable program in Python. 
# Technically, the program will work fine by just calling main(), 
# but you might get an angry letter from Guido van Rossum if you don't.