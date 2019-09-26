import pygame
from hero import Hero
from fleet import Fleet

#Game Settings
WINDOW_WIDTH = 550
WINDOW_HEIGHT = 615
GAME_SIDE_MARGIN = 20
GAME_TOP_MARGIN = 20
GAME_BOTTOM_MARGIN = 20
GAME_BORDER_WIDTH = 3

GAME_TOP_WALL = GAME_TOP_MARGIN + GAME_BORDER_WIDTH
GAME_RIGHT_WALL = WINDOW_WIDTH - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH
GAME_BOTTOM_WALL = WINDOW_HEIGHT - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH
GAME_LEFT_WALL = GAME_SIDE_MARGIN + GAME_BORDER_WIDTH

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (0, 255, 255)
LIGHT_GREEN = (128, 255, 0)
YELLOW = (255, 255, 0)

pygame.init()
#Media Files
player_image = pygame.image.load('media/XWingEdited.png')
bullet_image = pygame.image.load('media/si-bullet.gif')
enemy_image = pygame.image.load('media/TieFighterEdited.png')
laser_sound = pygame.mixer.Sound('media/si-laser.wav')
explosion_sound = pygame.mixer.Sound('media/si-explode.wav')
background_picture = pygame.image.load('media/Space8bit.jpg')
pygame.mixer.music.load('media/Star Wars Cantina Band 2.wav')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
score_font = pygame.font.SysFont('Times New Roman', 35, True)
title_font = pygame.font.SysFont('Times New Roman', 50, True)
pygame.display.set_caption('SPACE WARS 2125')
title_press_start_font = pygame.font.SysFont('Times New Roman', int (30), True)
title_copyright_font = pygame.font.SysFont('Times New Roman', int(25), True)

# Title Screen
show_title_screen = True
while show_title_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hero.is_alive = False
            show_title_screen = False
        if event.type == pygame.KEYDOWN:
            show_title_screen = False

    title_text = title_font.render('| SPACE WARS 2125 |', False, LIGHT_GREEN)
    title_press_start_text = title_press_start_font.render('PRESS TO START', False, YELLOW)
    title_copyright_text = title_copyright_font.render('©2019 RYAN SMITH | TRUECODERS', False, WHITE)
    game_display.blit(title_text, (30, 50))
    game_display.blit(title_press_start_text, (120, 100))
    game_display.blit(title_copyright_text, (70, 580))
    pygame.display.flip()
    clock.tick(30)
    

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hero.is_alive = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.set_direction_left()
            elif event.key == pygame.K_RIGHT:
                hero.set_direction_right()
            elif event.key == pygame.K_SPACE:
                laser_sound.play()
                hero.shoot(bullet_image)
            elif event.key == pygame.K_p:
                pause_game()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                hero.set_direction_none()
            elif event.key == pygame.K_RIGHT:
                hero.set_direction_none()

def pause_game():
    is_paused = True
    while is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_paused = False
                hero.is_alive = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    is_paused = False
        clock.tick(30)

hero = Hero(player_image, 200, GAME_BOTTOM_WALL - player_image.get_height())

fleet = Fleet(3, 5, 4, enemy_image, GAME_LEFT_WALL + 1, GAME_TOP_WALL + 1)

#Main Game Loop
score = 0
while hero.is_alive:

    handle_events()

    fleet.handle_wall_collision(GAME_LEFT_WALL, GAME_RIGHT_WALL)
    hero.handle_wall_collision_with_bullets(GAME_TOP_WALL)
    game_display.blit(background_picture, (0, 0))

    for bullet in hero.bullets_fired:
        for ship in fleet.ships:
            if bullet.has_collided_with(ship):
                explosion_sound.play()
                bullet.is_alive = False
                ship.is_alive = False
                score += 5

    fleet.remove_dead_ships()

    hero.move(GAME_LEFT_WALL, GAME_RIGHT_WALL)
    fleet.move_over()
    hero.move_all_bullets()

    hero.show(game_display)
    fleet.show(game_display)
    hero.show_all_bullets(game_display)
    score_text = score_font.render(str(score), False, YELLOW)
    game_display.blit(score_text, (250, 0))

    pygame.display.update()

    clock.tick(30)

pygame.quit()
    

