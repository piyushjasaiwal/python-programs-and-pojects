import pygame
pygame.init()
game_window = pygame.display.set_mode((1200,500))

pygame.display.set_caption("Event Handling")

exit_game = False

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print("You have pressed the down arrow key")

pygame.quit()
quit()