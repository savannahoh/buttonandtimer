import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Word Crushh")

clock = pygame.time.Clock()

counter= 20
text = '20'.rjust(20)


pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

run = True
timeron = False
while run:
  screen.fill((255, 255, 255))
  pygame.draw.rect(screen, (50, 50, 0), (30, 10, 30, 30), border_radius=5)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      break       
    if event.type == pygame.USEREVENT:
      counter -= 1
      text = str(counter).rjust(20) if counter > 0 else 'times up!'.rjust(20)
      

    elif event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()

            if x in range(30, 60) and y in range(10, 40):
                print("correct!")
                timeron = True


    screen.blit(font.render(text, True, (0, 0, 0)), (32, 10))
    #pygame.display.flip()
    if timeron == True: 
      clock.tick(60)

    pygame.display.update()
