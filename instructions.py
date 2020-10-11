import pygame
import colors


def main():
    """
    Display Instructions
    :return:
        none
    """
    while True:
        WIDTH = 500
        WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
        pygame.display.set_caption("Pathfinding")

        image = pygame.image.load(r'instructions.jpg').convert()

        WINDOW.fill(colors.ORANGE_YELLOW)
        WINDOW.blit(image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                return None

        pygame.display.update()
