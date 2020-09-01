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
snake_x = 65
snake_y = 95
size = 15
clock = pygame.time.Clock()
fps = 30

while not exit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x+10

            elif event.key == pygame.K_LEFT:
                snake_x = snake_x-10
            
            elif event.key == pygame.K_UP:
                snake_y = snake_y-10
            
            elif event.key == pygame.K_DOWN:
                snake_y = snake_y+10
            

    game_window.fill(white)
    pygame.draw.rect(game_window,red,[snake_x,snake_y,size,size])
    pygame.display.update()
pygame.quit()
quit()