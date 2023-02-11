# Sklenda
# Originally by Petr Janik
# Idea by Zdenek Sklenar

import pygame
import sys
from pygame.locals import *

BOARD_WIDTH = 4  
BOARD_HEIGHT = 4  
TILE_SIZE = 80
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
FPS = 30
BLANK = None

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (252, 201, 106)
BROWN = (96, 46, 8)
RED = (255, 0, 0)

BG_COLOR = BLACK
TILE_COLOR = WHITE
TEXT_COLOR = WHITE
BORDER_COLOR = BLACK
POINT_COLOR = RED
BASIC_FONT_SIZE = 20

CIRCLE = 'circle'
SQUARE = 'square'
SMALL = 'small'
BIG = 'big'
FALSE= False
TRUE = True

FPS_CLOCK = None
DISPLAY_SURFACE = None
BASIC_FONT = None
BUTTONS = None



def main():
    global FPS_CLOCK, DISPLAY_SURFACE, BASIC_FONT, BUTTONS

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Sklenda')
    BASIC_FONT = pygame.font.Font('freesansbold.ttf', BASIC_FONT_SIZE)

    while True:
        run_game()

def terminate():
    pygame.quit()
    sys.exit()
   
def run_game():
    icons = [
        [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            ],
        [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            ],
        [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            ],
        [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
           ]
            ]
    icons2 = [
        [
            [CIRCLE, YELLOW, FALSE, SMALL],
            [CIRCLE, YELLOW, FALSE, BIG],
            [CIRCLE, YELLOW, TRUE, SMALL],
            [CIRCLE, YELLOW, TRUE, BIG],
            ],
        [
            [CIRCLE, BROWN, FALSE, SMALL],
            [CIRCLE, BROWN, FALSE, BIG],
            [CIRCLE, BROWN, TRUE, SMALL],
            [CIRCLE, BROWN, TRUE, BIG],
            ],
        [
            [SQUARE, YELLOW, FALSE, SMALL],
            [SQUARE, YELLOW, FALSE, BIG],
            [SQUARE, YELLOW, TRUE, SMALL],
            [SQUARE, YELLOW, TRUE, BIG],
            ],
        [
            [SQUARE, BROWN, FALSE, SMALL],
            [SQUARE, BROWN, FALSE, BIG],
            [SQUARE, BROWN, TRUE, SMALL],
            [SQUARE, BROWN, TRUE, BIG],
           ]
            ]    
    WIN = False
    choosed = False
    placed = 0
    shape, color, point, size = None, None, None, None
    game_state = 1
    new_surf, new_rect = make_text('New Game', BLACK, TILE_COLOR, WINDOW_WIDTH - 145, WINDOW_HEIGHT - 50)
    while True:    
        if game_state == 1:
            message = "Player 1 chooses block."
        elif game_state == 2:
            message = "Player 2 places block."
            player = "2"
        elif game_state == 3:
            message = "Player 2 chooses block."
        elif game_state == 4:
            message = "Player 1 places block."
            player = "1"

        if placed == 16:
            message = "It is a tie! Press New Game to play again."
            
        if WIN:
            message = "Player " + player + " wins!"
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if new_rect.collidepoint(event.pos):
                        return
                
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == pygame.MOUSEBUTTONUP:
                
                if game_state == 1 or game_state == 3:
                    if get_tile_clicked2(event.pos[0], event.pos[1]) != (None, None):
                        tile_x, tile_y = get_tile_clicked2(event.pos[0], event.pos[1])
                        if icons2[tile_x][tile_y][0] != None:
                            shape, color, point, size = icons2[tile_x][tile_y][0], icons2[tile_x][tile_y][1], icons2[tile_x][tile_y][2], icons2[tile_x][tile_y][3]
                            icons2[tile_x][tile_y] = [None, None, None, None]
                            choosed = True
                            if game_state == 1:
                                game_state = 2
                            elif game_state == 3:
                                game_state = 4
                            
                elif game_state == 2 or game_state == 4:
                    if get_tile_clicked(event.pos[0], event.pos[1]) != (None, None):
                        tile_x, tile_y = get_tile_clicked(event.pos[0], event.pos[1])
                        if icons[tile_x][tile_y][0] == None:
                            choosed = False
                            icons[tile_x][tile_y] = [shape, color, point, size]
                            placed += 1
                            WIN = check_for_quit(icons, tile_x, tile_y)
                            if game_state == 2:
                                game_state = 3
                            elif game_state == 4:
                                game_state = 1
    
                if new_rect.collidepoint(event.pos):
                    return
                
        draw_board(icons, icons2, shape, color, point, size, choosed, new_surf, new_rect, message)

        pygame.display.update()
        FPS_CLOCK.tick(FPS)

def get_left_top_of_tile(tile_x, tile_y):
    left = (tile_x * TILE_SIZE) + 40
    top = (tile_y * TILE_SIZE) + 110
    return (left, top)

def get_left_top_of_tile2(tile_x, tile_y):
    left = (tile_x * TILE_SIZE) + 440
    top = (tile_y * TILE_SIZE) + 110
    return (left, top)

def draw_tile(tile_x, tile_y):
    left, top = get_left_top_of_tile(tile_x, tile_y)
    pygame.draw.rect(DISPLAY_SURFACE, TILE_COLOR, (left, top, TILE_SIZE, TILE_SIZE))
    pygame.draw.rect(DISPLAY_SURFACE, BORDER_COLOR, (left-1, top-1, TILE_SIZE+2, TILE_SIZE+2), 1)

def draw_tile2(tile_x, tile_y):
    left, top = get_left_top_of_tile2(tile_x, tile_y)
    pygame.draw.rect(DISPLAY_SURFACE, TILE_COLOR, (left, top, TILE_SIZE, TILE_SIZE))
    pygame.draw.rect(DISPLAY_SURFACE, BORDER_COLOR, (left-1, top-1, TILE_SIZE+2, TILE_SIZE+2), 1)

def make_text(text, color, bg_color, top, left):
    text_surf = BASIC_FONT.render(text, True, color, bg_color)
    text_rect = text_surf.get_rect()
    text_rect.topleft = (top, left)
    return (text_surf, text_rect)

def draw_board(icons, icons2, shape, color, point, size, choosed, new_surf, new_rect, message=""):
    DISPLAY_SURFACE.fill(BG_COLOR)
    text_surf, text_rect = make_text(message, TEXT_COLOR, BG_COLOR, 40, 40)
    DISPLAY_SURFACE.blit(text_surf, text_rect)

    if choosed:            
        display_choosed(icons2, shape, color, point, size)
        
    for tile_x in range(BOARD_WIDTH):
        for tile_y in range(BOARD_WIDTH):
                draw_tile(tile_x, tile_y)
                
    for tile_x in range(BOARD_WIDTH):
        for tile_y in range(BOARD_WIDTH):
                draw_tile2(tile_x, tile_y)

    for tile_x in range(BOARD_WIDTH):
        for tile_y in range(BOARD_WIDTH):
                draw_icon(icons, tile_x, tile_y)

    for tile_x in range(BOARD_WIDTH):
        for tile_y in range(BOARD_WIDTH):
                draw_icon2(icons2, tile_x, tile_y)

    DISPLAY_SURFACE.blit(new_surf, new_rect)

def display_choosed(list, shape, color, point, size):
    left, top = 280, 20
    if shape == CIRCLE:
        center_point = (left + 40, top + 40)
        if size == SMALL:
            pygame.draw.circle(DISPLAY_SURFACE, color, center_point, 20)
        elif size == BIG:
            pygame.draw.circle(DISPLAY_SURFACE, color, center_point, 30)
        if point:
            pygame.draw.circle(DISPLAY_SURFACE, POINT_COLOR, center_point, 10)
    elif shape == SQUARE:
        center_point = (left + 40, top + 40)
        if size == SMALL:
            rect = (left + 20, top + 20, 40, 40)
        elif size == BIG:
            rect = (left + 10, top + 10, 60, 60)
        pygame.draw.rect(DISPLAY_SURFACE, color, rect)
        if point:
            pygame.draw.circle(DISPLAY_SURFACE, POINT_COLOR, center_point, 10)

def draw_icon(list, tile_x, tile_y):
    shape, color, point, size = list[tile_x][tile_y][0], list[tile_x][tile_y][1], list[tile_x][tile_y][2], list[tile_x][tile_y][3]
    left, top = get_left_top_of_tile(tile_x, tile_y)
    if shape == CIRCLE:
        center_point = (left + 40, top + 40)
        if size == SMALL:
            pygame.draw.circle(DISPLAY_SURFACE, color, center_point, 20)
        elif size == BIG:
            pygame.draw.circle(DISPLAY_SURFACE, color, center_point, 30)
        if point:
            pygame.draw.circle(DISPLAY_SURFACE, POINT_COLOR, center_point, 10)
    elif shape == SQUARE:
        center_point = (left + 40, top + 40)
        if size == SMALL:
            rect = (left + 20, top + 20, 40, 40)
        elif size == BIG:
            rect = (left + 10, top + 10, 60, 60)
        pygame.draw.rect(DISPLAY_SURFACE, color, rect)
        if point:
            pygame.draw.circle(DISPLAY_SURFACE, POINT_COLOR, center_point, 10)
            
def draw_icon2(list, tile_x, tile_y):
    shape, color, point, size = list[tile_x][tile_y][0], list[tile_x][tile_y][1], list[tile_x][tile_y][2], list[tile_x][tile_y][3]
    left, top = get_left_top_of_tile2(tile_x, tile_y)
    if shape == CIRCLE:
        center_point = (left + 40, top + 40)
        if size == SMALL:
            pygame.draw.circle(DISPLAY_SURFACE, color, center_point, 20)
        elif size == BIG:
            pygame.draw.circle(DISPLAY_SURFACE, color, center_point, 30)
        if point:
            pygame.draw.circle(DISPLAY_SURFACE, POINT_COLOR, center_point, 10)
    elif shape == SQUARE:
        center_point = (left + 40, top + 40)
        if size == SMALL:
            rect = (left + 20, top + 20, 40, 40)
        elif size == BIG:
            rect = (left + 10, top + 10, 60, 60)
        pygame.draw.rect(DISPLAY_SURFACE, color, rect)
        if point:
            pygame.draw.circle(DISPLAY_SURFACE, POINT_COLOR, center_point, 10)

def get_tile_clicked(x, y):
    for tile_x in range(BOARD_WIDTH):
        for tile_y in range(BOARD_HEIGHT):
            left, top = get_left_top_of_tile(tile_x, tile_y)
            tile_rect = pygame.Rect(left, top, TILE_SIZE, TILE_SIZE)
            if tile_rect.collidepoint(x, y):
                return (tile_x, tile_y)
    return (None, None)

def get_tile_clicked2(x, y):
    for tile_x in range(BOARD_WIDTH):
        for tile_y in range(BOARD_HEIGHT):
            left, top = get_left_top_of_tile2(tile_x, tile_y)
            tile_rect = pygame.Rect(left, top, TILE_SIZE, TILE_SIZE)
            if tile_rect.collidepoint(x, y):
                return (tile_x, tile_y)
    return (None, None)

def check_for_quit(icons, tile_x, tile_y):
    list = [None, None, None, None]
    lp_icon = icons[tile_x][tile_y]
    top_left = True
    top_right = True
    bottom_left = True
    bottom_right = True
    for i in range(4): #checks horizontal line
        icon = icons[i][tile_y]
        list[i] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
    if compare(list):
        return True
    for i in range(4): #checks vertical line
        icon = icons[tile_x][i]
        list[i] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
    if compare(list):
        return True
    if tile_x == 0:
        top_left = False
        bottom_left = False
    if tile_x == 3:
        top_right = False
        bottom_right = False
    if tile_y == 0:
        top_left = False
        top_right = False
    if tile_y == 3:
        bottom_left = False
        bottom_right = False
    if top_left:
        icon = icons[tile_x][tile_y]
        list[0] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
        icon = icons[tile_x][tile_y - 1]
        list[1] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
        icon = icons[tile_x - 1][tile_y - 1]
        list[2] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
        icon = icons[tile_x - 1][tile_y]
        list[3] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
    if compare(list):
        return True
    if top_right:
        icon = icons[tile_x][tile_y]
        list[0] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
        icon = icons[tile_x][tile_y - 1]
        list[1] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
        icon = icons[tile_x + 1][tile_y - 1]
        list[2] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
        icon = icons[tile_x + 1][tile_y]
        list[3] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
    if compare(list):
        return True
    if bottom_left:
        icon = icons[tile_x][tile_y]
        list[0] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
        icon = icons[tile_x][tile_y + 1]
        list[1] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
        icon = icons[tile_x - 1][tile_y + 1]
        list[2] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
        icon = icons[tile_x - 1][tile_y]
        list[3] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
    if compare(list):
        return True
    if bottom_right:
        icon = icons[tile_x][tile_y]
        list[0] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
        icon = icons[tile_x][tile_y + 1]
        list[1] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
        icon = icons[tile_x + 1][tile_y + 1]
        list[2] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
        icon = icons[tile_x + 1][tile_y]
        list[3] = check_if_same(icons, lp_icon, icon, tile_x, tile_y)
    if compare(list):
        return True
    return False

def check_if_same(icons, lp_icon, icon, tile_x, tile_y):
    values = []
    for i in range(4):
        if icon[i] == lp_icon[i]:
            values.append(1)
        else:
            values.append(0)
    return (values)

def compare(list):
    for i in range(4):
        count = 0
        for j in range(4):
            count += list[j][i]
            if count == 4:
                return True
    return False    
        
if __name__ == '__main__':
    main()
