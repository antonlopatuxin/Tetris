import pygame
from settings import Settings
from control import Control
from gui import GUI
from shape import Shape
from phisics import Physics
from button import Button_Exit
from  button import Button_Play
from button import Button_Pause

def main():
    pygame.init()
    clock = pygame.time.Clock()
    settings = Settings()
    physics = Physics()
    shape = Shape()
    shape.shape_name = shape.get_shape_form()
    shape.next_shape = shape.get_shape_form()
    shape.next_color = shape.get_color()
    shape.shape_form = shape.get_shape()
    shape.shape_color = shape.get_color()
    play_button = Button_Play("images/play.jpg","images/button_play_click.jpg",555,590)
    pause_button = Button_Pause("images/pause.jpg","images/pause_click.jpg",555,654)
    exit_button = Button_Exit("images/exit.jpg","images/exit_click.jpg",555,714)
    control = Control()
    gui = GUI()
    screen = pygame.display.set_mode((settings.window_size[0],settings.window_size[1]))
    pygame.display.set_caption(settings.caption_window)
    pygame.display.set_icon(settings.icon_window)
    gui.init_gui()
    screen.blit(gui.interface2, (500, 0))
    screen.blit(gui.grid, (25, 25))
    pygame.display.update()
    var = 0 #для сокращения скорости передвижения фигуры

    while control.play:
        exit_button.exit(control)
        pause_button.pause(control,settings)
        play_button.play(control,settings)
        shape.shape_form.check_rotate_resolution()
        control.control_game(shape)
        play_button.draw_button(screen, control)
        pause_button.draw_button(screen, control)
        exit_button.draw_button(screen, control)
        screen.blit(gui.menu_window, (550, 50))
        gui.draw_indicator(screen)
        gui.draw_segment_indicator(screen)
        gui.draw_score(screen)
        if settings.play_game:
            gui.draw_next_shape(screen, shape)
            screen.blit(gui.grid, (25, 25))
            physics.add_brick_list(shape)
            physics.draw_bottom_brick(screen)
            physics.check_bottom(shape,control)
            physics.check_collision(shape,control)
            if var % control.speed_variable == 0 :
                shape.shape_control()
                shape.shape_moove(settings, physics)
            shape.draw_shape(shape.shape_color, screen)
            physics.logic_game(screen,gui)
            var += 1
        screen.blit(gui.interface, (0, 0))
        pygame.display.flip()
        clock.tick(settings.FPS)


main()