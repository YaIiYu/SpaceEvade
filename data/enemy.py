import random
import pygame

class Enemy:
    def __init__(self, width, height, speed=5, color=(255, 0, 0), img=None, size=50):
        self.width = width
        self.height = height
        self.enemy_size = size
        self.enemy_list = []
        self.enemy_speed = speed
        self.color = color

        if img:
            original_image = pygame.image.load(img).convert_alpha()
            self.image = pygame.transform.scale(original_image, (self.enemy_size, self.enemy_size))
        else:
            self.image = None

    def spawn_enemy(self):
        """Спавн ворога у верхній частині екрана."""
        x = random.randint(0, self.width - self.enemy_size)
        y = 0
        self.enemy_list.append([x, y])

    def move_enemies(self):
        for enemy in self.enemy_list:
            enemy[1] += self.enemy_speed
        self.enemy_list = [enemy for enemy in self.enemy_list if enemy[1] < self.height]

    def draw_enemies(self, screen):
        for enemy in self.enemy_list:
            if self.image:
                screen.blit(self.image, (enemy[0], enemy[1]))
            else:
                pygame.draw.rect(screen, self.color, (enemy[0], enemy[1], self.enemy_size, self.enemy_size))
