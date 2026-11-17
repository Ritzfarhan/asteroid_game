
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import pygame
import random



class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        #position = [self.x,self.y]
        pygame.draw.circle(screen, "white",self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.move(dt)

    def move(self,dt:float) -> None:
        unit_vector = pygame.Vector2(self.position)
       #rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = self.velocity * dt
        self.position += rotated_with_speed_vector

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        path1 = self.velocity.rotate(angle)
        path2 = self.velocity.rotate(angle*-1)


        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_roid1 = Asteroid(self.position.x,self.position.y,new_radius)
        new_roid2 = Asteroid(self.position.x,self.position.y,new_radius)

        new_roid1.velocity = path1 * 1.2
        new_roid2.velocity = path2 * 1.2
