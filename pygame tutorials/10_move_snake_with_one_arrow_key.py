import pygame
pygame.init()

#colors in game
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

#game screen parameters
width = 900
height = 600

#game window
game_window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snakezzzzzzzzzzzzzzzz")

#game variables 
exit_game = False
quit_game = False
snake_x = 65
snake_y = 95
size = 15
clock = pygame.time.Clock()
fps = 30
velocity_x = 0
velocity_y = 0

while not exit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 7
                velocity_y = 0

            elif event.key == pygame.K_LEFT:
                velocity_x = -7
                velocity_y = 0
            elif event.key == pygame.K_UP:
                velocity_y = -7
                velocity_x = 0
                
            elif event.key == pygame.K_DOWN:
                velocity_y = 7
                velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y

    game_window.fill(white)
    pygame.draw.rect(game_window,red,[snake_x,snake_y,size,size])
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()