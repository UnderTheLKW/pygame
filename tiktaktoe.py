import time

import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (220, 220, 220)
blue = (240, 248, 255)

screen = pygame.display.set_mode((1024, 1024))
screen.fill("grey")
def game_field():
    pygame.draw.line(screen, black, [75, 683], [949, 683], 4)
    pygame.draw.line(screen, black, [341, 75], [341, 949], 4)
    pygame.draw.line(screen, black, [683, 75], [683, 949], 4)
    pygame.draw.line(screen, black, [75, 341], [949, 341], 4)

right = 3
# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()


pygame.display.set_caption("tik tak toe")

board_state = [False, False, False,
               False, False, False,
               False, False, False]

# textcreation

font = pygame.font.Font('freesansbold.ttf', 72)
text = font.render('Spieler Rot hat gewonnen', True, red, grey)
textRect = text.get_rect(center = pygame.display.get_surface().get_rect().center)

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Schleife Hauptprogramm

while spielaktiv:

     # Refresh-Zeiten festlegen
    clock.tick(60)
     # Spielfeld

    game_field()
    '''
    if board_state[0]:
        pygame.draw.circle(screen, red, [200, 200], 100, 8)
    if board_state[1]:
        pygame.draw.circle(screen, red, [516, 200], 100, 8)
    if board_state[2]:
        pygame.draw.circle(screen, red, [835, 200], 100, 8)
    if board_state[3]:
        pygame.draw.circle(screen, red, [200, 516], 100, 8)
    if board_state[4]:
        pygame.draw.circle(screen, red, [516, 516], 100, 8)
    if board_state[5]:
        pygame.draw.circle(screen, red, [835, 516], 100, 8)
    if board_state[6]:
        pygame.draw.circle(screen, red, [200, 835], 100, 8)
    if board_state[7]:
        pygame.draw.circle(screen, red, [516, 835], 100, 8)
    if board_state[8]:
        pygame.draw.circle(screen, red, [835, 835], 100, 8)'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("spieler hat das Spiel beendet")
        elif event.type == pygame.MOUSEBUTTONUP:
            print(event.pos)
            print("Spieler hat was gedrückt")
            if event.pos[0] < 341 and event.pos[1] <= 341:
                print("1")
                board_state[0] = True
                pygame.draw.circle(screen, red, [200, 200], 100, 8)
            if event.pos[0] < 682 and event.pos[0] > 341 and event.pos[1] < 341 and event.pos[1] > 0:
                print("2")
                board_state[1] = True
                pygame.draw.circle(screen, red, [516, 200], 100, 8)
            if event.pos[0] < 1024 and event.pos[0] > 682 and event.pos[1] < 341 and event.pos[1] > 0:
                print("3")
                board_state[2] = True
                pygame.draw.circle(screen, red, [835, 200], 100, 8)
            if event.pos[0] < 341 and event.pos[0] > 0 and event.pos[1] < 682 and event.pos[1] > 341:
                print("4")
                board_state[3] = True
                pygame.draw.circle(screen, red, [200, 516], 100, 8)
            if event.pos[0] < 682 and event.pos[0] > 341 and event.pos[1] < 682 and event.pos[1] > 341:
                print("5")
                board_state[4] = True
                pygame.draw.circle(screen, red, [516, 516], 100, 8)
            if event.pos[0] < 1024 and event.pos[0] > 682 and event.pos[1] < 682 and event.pos[1] > 341:
                print("6")
                board_state[5] = True
                pygame.draw.circle(screen, red, [835, 516], 100, 8)
            if event.pos[0] < 341 and event.pos[0] > 0 and event.pos[1] < 1024 and event.pos[1] > 682:
                print("7")
                board_state[6] = True
                pygame.draw.circle(screen, red, [200, 835], 100, 8)
            if event.pos[0] < 682 and event.pos[0] > 341 and event.pos[1] < 1024 and event.pos[1] > 682:
                print("8")
                board_state[7] = True
                pygame.draw.circle(screen, red, [516, 835], 100, 8)
            if event.pos[0] < 1024 and event.pos[0] > 682 and event.pos[1] < 1024 and event.pos[1] > 682:
                print("9")
                board_state[8] = True
                pygame.draw.circle(screen, red, [835, 835], 100, 8)
            #wagerecht
            if board_state[0] and board_state[1] and board_state[2]:
                pygame.draw.line(screen, black, [75, 200], [950, 200], 10)
                screen.blit(text, textRect)
                pygame.display.flip()
                time.sleep(2)
                board_state = [False, False, False, False, False, False, False, False, False]
                game_field()
                screen.fill("grey")
                pygame.display.flip()
            if board_state[3] and board_state[4] and board_state[5]:
                pygame.draw.line(screen, black, [75, 510], [950, 510], 10)
            if board_state[6] and board_state[7] and board_state[8]:
                pygame.draw.line(screen, black, [75, 850], [950, 850], 10)
            #senkrecht
            if board_state[0] and board_state[3] and board_state[6]:
                pygame.draw.line(screen, black, [200, 75], [200, 950], 10)
            if board_state[1] and board_state[4] and board_state[7]:
                pygame.draw.line(screen, black, [511, 75], [511, 950], 10)
            if board_state[2] and board_state[5] and board_state[8]:
                pygame.draw.line(screen, black, [845, 75], [845, 950], 10)
            #kreuz
            if board_state[0] and board_state[4] and board_state[8]:
                pygame.draw.line(screen, black, [75, 75], [950, 950], 10)
            if board_state[2] and board_state[4] and board_state[6]:
                pygame.draw.line(screen, black, [950, 75], [75, 950], 10)
        #if event.type == pygame.MOUSEBUTTONUP and event.button == right:
            #screen.fill("blue")

    pygame.display.flip()
#spiel Beenden
pygame.quit()

