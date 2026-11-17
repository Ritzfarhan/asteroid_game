
from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame



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
