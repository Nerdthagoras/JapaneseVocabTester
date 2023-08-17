import pygame
import Classes
import Constants

# Initialize Pygame
pygame.init()

# Game loop
while not Classes.current_state.done:
    events = pygame.event.get()
    Classes.current_state.update()
    Classes.current_state.draw(Constants.screen)
    pygame.display.update()
    Classes.current_state.sound()
    Classes.current_state.handle_events(events)

    if Classes.current_state.done:
        if Classes.current_state == Classes.menu_state:
            Classes.current_state = Classes.game_state
        elif Classes.current_state == Classes.game_state:
            Classes.current_state = Classes.gameover_state
        elif Classes.current_state == Classes.gameover_state:
            Classes.current_state = Classes.menu_state
        else:
            pass

# Quit
pygame.quit()