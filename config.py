import pygame

import constants

pygame.init()
pygame.display.set_caption("Tic tac toe")
size = width, height = constants.WIDTH, constants.HEIGHT
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

