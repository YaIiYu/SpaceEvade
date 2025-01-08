import pygame
import random
import sys
import os
from data.character_class import Character
from data.enemy import Enemy
from data.FPS import FramePS

image_folder = "img//"
pygame.init()

# Параметри вікна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Evade")
programIcon = pygame.image.load(os.path.join(image_folder,"spaceship.png"))
pygame.display.set_icon(programIcon)

# Базові кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Шрифт для бокового тексту
font = pygame.font.Font(None, 36)

# Перевірка колізії
def check_collision(player_pos, enemies, enemy_size):
    for enemy in enemies:
        if (player_pos[0] < enemy[0] + enemy_size and
            player_pos[0] + enemy_size > enemy[0] and
            player_pos[1] < enemy[1] + enemy_size and
            player_pos[1] + enemy_size > enemy[1]):
            return True
    return False

def main():
    # Ініціалізація гравця
    player = Character(
        x=WIDTH // 2,
        y=HEIGHT - 100,
        size=60,
        speed=5,
        img=os.path.join(image_folder, 'spaceship.png'),
        color=RED
    )

    # Ініціалізація ворогів
    enemy = Enemy(
        size=30,
        width=WIDTH,
        height=HEIGHT,
        speed=5,
        color=RED,
        img=os.path.join(image_folder, 'meteor.png'),
    )

    # Ініціалізація FPS
    fps = FramePS

    score = 0

    while True:
        # Вихід
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Управління гравця
        keys = pygame.key.get_pressed()
        player.handle_movement(keys, WIDTH, HEIGHT)

        # Спавн ворогів
        if random.randint(1, 20) == 1:
            enemy.spawn_enemy()

        # Рух ворогів
        enemy.move_enemies()

        # Перевірка колізії
        if check_collision([player.x, player.y], enemy.enemy_list, enemy.enemy_size):
            print(f"Гра закінчена! Твій рахунок: {score // 10}")
            pygame.quit()
            sys.exit()

        # Оновлення рахунку
        score += 1

        if score % 500 == 0:
            enemy.enemy_speed += 1

        # Малювання об'єктів
        screen.fill(BLACK)
        player.draw(screen)
        enemy.draw_enemies(screen)

        # Відображення рахунку збоку
        score_text = font.render(f"Рахунок: {score // 10}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Оновлення екрану
        pygame.display.flip()

        # Обмеження FPS
        fps.clock.tick(fps.FpS)

# Запуск гри
if __name__ == "__main__":
    main()
