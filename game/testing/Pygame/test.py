import pygame
import os
import random

pygame.init()
FOLDER = 'images'


pretty_background = pygame.image.load(os.path.join(FOLDER,'800px-La_naissance_de_Venus.jpg'))
ugly_background = pygame.image.load(os.path.join(FOLDER,'background800x470.jpg'))
snake_surface = pygame.image.load(os.path.join(FOLDER,'snake.gif'))

screen = pygame.display.set_mode((800,470))
screen_rect = screen.get_rect()
pretty_background = pretty_background.convert()
ugly_background = ugly_background.convert()
background = ugly_background.copy()
snake_surface = snake_surface.convert_alpha()
snake_rect = snake_surface.get_rect()

x = 1
y = 1
dx = 40
dy = 85

screen.blit(ugly_background,(0,0))
screen.blit(snake_surface,(x,y))
clock = pygame.time.Clock()
mainloop = True
FPS = 60
play_time = 0.0
painting = False
dirty = False

while mainloop:
    milliseconds = clock.tick(FPS)
    second = milliseconds / 1000.0
    play_time = second + play_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            elif event.key == pygame.K_RIGHT:
                background = ugly_background.copy()
                screen.blit(ugly_background,(0,0))
                print("Картина восстановлена")
            elif event.key == pygame.K_LEFT:
                painting = not painting
                print("painting is now set to {}".format(painting))
            elif event.key == pygame.K_DOWN:
                dirty = not dirty
                print("dirty is now set to {}".format(dirtyrect))

    pygame.display.set_caption("FPS: {:.2f} dx:{} dy:{} [p]aint ({}) "
                               "paint, [d]irtyrect ({}), [r]estore".format(clock.get_fps(), dx,
                                                                           dy, painting, dirty))
    if not dirty:
        dirtyrect = background.subsurface((x,y,snake_rect.width,screen_rect.height))
        screen.blit(dirtyrect,(x,y))
    x += dx * second
    y += dy * second
    if x < 0:
        x = 0
        dx *= -1
        dx += random.randint(-15,15)
    elif x + snake_rect.width >= screen_rect.width:
        ballx = screen_rect.width - snake_rect.width
        dx *= -1
        dx += random.randint(-15,15)
    if y < 0:
        y = 0
        dy *= -1
        dy += random.randint(-15, 15)
    elif y + snake_rect.height >= screen_rect.height:
        y = screen_rect.height - snake_rect.height
        dy *= -1
        dy += random.randint(-15, 15)
        # paint the snake
    screen.blit(snake_surface, (x, y))
    # TV corner: paint a subsurface on the screen of this part of prettybackground
    # where snake is at the moment (rect argument)
    try:
        tvscreen = pretty_background.subsurface((x, y, snake_rect.width, snake_rect.height))
    except:
        print("some problem with subsurface")
    screen.blit(tvscreen, (0, 0))  # blit into screen like a tv
    if painting:
        background.blit(tvscreen, (x, y))  # blit from pretty background into background
    pygame.display.flip()  # flip the screen 30 times a second
print("This 'game' was played for {:.2f} seconds".format(play_time))
