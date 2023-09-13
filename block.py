from config import pygame
import constants

class Block:
    def __init__(self, x, y, val=None):
        self.rect = pygame.Rect(x, y, constants.BLOCK_WIDTH, constants.BLOCK_HEIGHT)
        self.val = val
        self.color = constants.BLOCK_COLOR