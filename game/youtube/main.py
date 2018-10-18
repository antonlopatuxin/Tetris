import pygame

pygame.init()
window = pygame.display.set_mode((441,441))
pygame.display.set_caption("Змейка")
flag_game = True
head = [45,45]
var_speed = 0

while flag_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag_game = False
    window.fill(pygame.Color("Black"))
    pygame.draw.rect(window,pygame.Color("Green"),pygame.Rect(head[0],head[1],10,10))
    if var_speed % 1000 == 0:
        head[0] += 25
    var_speed += 1
    pygame.display.flip()