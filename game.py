import sys

import constants
from config import pygame, screen, clock
from block import Block

# Helper function to print grid for debugging purpose
def print_grid(grid):
    print("====>>>>>")
    for i in range(3):
        print(grid[i][0].val, grid[i][1].val, grid[i][2].val)
    print("<<<<<====")

def init_grid(grid):
    x, y = 0, 0
    for i in range(3):
        x = 0
        temp_list = list()
        for j in range(3):
            temp_list.append(Block(x, y))
            if j != 2:
                x += 5
            x += constants.BLOCK_WIDTH
        if i != 2:
            y += 5
        y += constants.BLOCK_HEIGHT
        grid.append(temp_list)

def validate(grid):
    win_str = ""
    draw = True
    for i in range(3):
        x, o = 0, 0
        for j in range(3):
            if grid[i][j].val is None:
                draw = False
            if grid[i][j].val == 1:
                x += 1
            elif grid[i][j].val == 0:
                o += 1
        if x == 3:
            win_str = "X won!"
        elif o == 3:
            win_str = "O won!"

    for j in range(3):
        x, o = 0, 0
        for i in range(3):
            if grid[i][j].val == 1:
                x += 1
            elif grid[i][j].val == 0:
                o += 1
        if x == 3:
            win_str = "X won!"
        elif o == 3:
            win_str = "O won!"

    if grid[0][0].val == grid[1][1].val == grid[2][2].val:
        if grid[0][0].val == 1:
            win_str = "X won!"
        elif grid[0][0] == 0:
            win_str = "O won!"
    if grid[0][2].val == grid[1][1].val == grid[2][0].val:
        if grid[0][2].val == 1:
            win_str = "X won!"
        elif grid[0][2].val == 0:
            win_str = "O won!"

    if draw and win_str == "":
        win_str = "Draw!"
    return win_str

def main():
    # Initialize all required variables
    grid = list()
    init_grid(grid)
    color = [(229, 210, 131), (79, 112, 156)]
    player = ["O", "X"]
    turn = 0
    score_x, score_o = 0, 0
    start = pygame.font.SysFont("comicsans", 40).render("START", True, "white", (33, 53, 85))
    reset = pygame.font.SysFont("comicsans", 40).render("RESET", True, "white", (120, 67, 46))
    start_rect = start.get_rect().move((50, constants.BLOCK_HEIGHT*3 + 20))
    reset_rect = reset.get_rect().move((150 + start.get_width(), constants.BLOCK_HEIGHT * 3 + 20))

    # Start screen
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                # Mouse clicked on grid
                for r in grid:
                    for g in r:
                        if (g.rect.left <= x <= g.rect.right) and (g.rect.top <= y <= g.rect.bottom) and g.val is None:
                            g.color = color[turn % 2]
                            g.val = turn % 2
                            turn += 1
                # Mouse clicked on start or reset
                if (start_rect.left <= x <= start_rect.right) and (start_rect.top <= y <= start_rect.bottom):
                    grid = list()
                    init_grid(grid)
                    turn = 0
                if (reset_rect.left <= x <= reset_rect.right) and (reset_rect.top <= y <= reset_rect.bottom):
                    grid = list()
                    init_grid(grid)
                    turn, score_x, score_o = 0, 0, 0

        # Draw grid
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(screen, grid[i][j].color, grid[i][j].rect)

        # Draw turn and score buttons
        turn_score_color = (255, 245, 224)
        turn_text = pygame.font.SysFont("comicsans", 20).render("Turn", True, turn_score_color)
        turn_text_rect = turn_text.get_rect().move((constants.BLOCK_WIDTH*3 + 30, 10))
        screen.blit(turn_text, turn_text_rect)
        score_text = pygame.font.SysFont("comicsans", 20).render("Score", True, turn_score_color)
        score_text_rect = score_text.get_rect().move((constants.BLOCK_WIDTH * 3 + 40 + turn_text.get_width(), 10))
        screen.blit(score_text, score_text_rect)

        turn_color = (250, 240, 230)
        no_turn_color = (53, 47, 68)
        turn_o = pygame.font.SysFont('comicsans', 40).render("O", True, no_turn_color if turn%2 else turn_color)
        screen.blit(turn_o, (turn_text_rect.left, turn_text_rect.bottom + 20))
        score_o_text = pygame.font.SysFont("comicsans", 40).render(str(score_o), True, "yellow")
        screen.blit(score_o_text, (score_text_rect.left + 10, score_text_rect.bottom + 20))
        turn_x = pygame.font.SysFont('comicsans', 40).render("X", True, turn_color if turn%2 else no_turn_color)
        screen.blit(turn_x, (turn_text_rect.left, turn_text_rect.bottom + turn_o.get_height() + 40))
        score_x_text = pygame.font.SysFont("comicsans", 40).render(str(score_x), True, "yellow")
        screen.blit(score_x_text, (score_text_rect.left + 10, score_text_rect.bottom + score_o_text.get_height() + 40))

        # Draw start and reset button
        screen.blit(start, start_rect)
        screen.blit(reset, reset_rect)

        # Validate grid
        win_str = validate(grid)
        if win_str != "":
            if win_str.startswith("X"):
                score_x += 1
            elif win_str.startswith("O"):
                score_o += 1
            win_text = pygame.font.SysFont('comicsans', 100).render(win_str, True, (53, 47, 68))
            screen.blit(win_text, (
            (constants.BLOCK_WIDTH*3 - win_text.get_width()) // 2, (constants.BLOCK_HEIGHT*3 - win_text.get_height()) // 2))
            pygame.display.update()
            pygame.time.delay(1000)
            grid = list()
            init_grid(grid)
            turn = 0
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()