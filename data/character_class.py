import pygame

class Character:
    def __init__(self, speed, color=(255, 255, 255), img=None, x=50, y=50, size=50):
        self.x = x
        self.y = y
        self.size = size  # Розмір гравця
        self.speed = speed
        self.color = color

        if img:
            self.view = pygame.image.load(img).convert_alpha()
            self.image = pygame.transform.scale(self.view, (self.size, self.size))
        else:
            self.image = None

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def handle_movement(self, keys, screen_width, screen_height):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < screen_width - self.size:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < screen_height - self.size:
            self.y += self.speed
