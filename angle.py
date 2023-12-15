import pygame
import calc

# setup
pygame.init()

res = (1080,720)
Screen = pygame.display.set_mode(res)
center_x = Screen.get_width()/2
center_y = Screen.get_height()/2

Clock = pygame.time.Clock()

running = True

# angle generator configuration
min_angle = 90
n_angle = 3
angles = calc.give_angles(min_angle, n_angle)
lengths = [100,100,100]

while running:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            angles = calc.give_angles(min_angle, n_angle)
            lengths = calc.get_lengths(n_angle, 10, int(min(center_y, center_x)))
            # print(angles, lengths)
    
    # screen update
    Screen.fill((0,0,0))

    # drawing n lines 
    for length in enumerate(lengths):
        pygame.draw.line(Screen, 'white', (center_x, center_y), calc.get_end_coords(center_x, center_y, length[1], sum(angles[0:length[0]])))

    pygame.display.flip()
    Clock.tick(60)

