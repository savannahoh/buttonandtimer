import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Word Crushh")

clock = pygame.time.Clock()

counter, text = 20, '20'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

run = True
timeron = False
while run:
  screen.fill((255, 255, 255))
  pygame.draw.rect(screen, (200, 200, 0), (50, 250, 50, 50), border_radius=5)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      break

    elif event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()

            if x in range(50, 100) and y in range(250, 300):
                print("correct!")
                timeron = True
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT:
            run = False
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    if timeron == True: 
      clock.tick(60)

    pygame.display.update()
