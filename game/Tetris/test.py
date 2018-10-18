import pygame

surf = pygame.Surface((145,25))
indicator_left = pygame.image.load("images/indicator_left.jpg")
indicator_center = pygame.image.load("images/indicator_center.jpg")
indicator_right = pygame.image.load("images/indicator_right.jpg")
surf.blit(indicator_left,(0,0))
surf.blit(indicator_center,(40,2))
surf.blit(indicator_center,(72,2))
surf.blit(indicator_right,(104,0))
pygame.image.save(surf,"images/indicator.jpg")