import pygame
pygame.init()

#colors in game
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

#game screen parameters
width = 600
height = 400

#game window
game_window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snakezzzzzzzzzzzzzzzz")
#game variables 
exit_game = False
quit_game = False

while not exit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    game_window.fill(white)
    pygame.display.update()
pygame.quit()
quit()