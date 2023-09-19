import pygame
import sys
import os
import random
import engine

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

# =========================Initialization of images, fonts, etc.=========================

pygame.display.set_caption('Perfect Chord')

screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
display = pygame.Surface((600, 400))

tfont = pygame.font.Font('fonts/font.ttf', 48)
font = pygame.font.Font('fonts/font.ttf', 32)
sfont = pygame.font.Font('fonts/font.ttf', 24)
vsfont = pygame.font.Font('fonts/font.ttf', 16)

pygame.mixer.set_num_channels(25)
pygame.mixer.Channel(11).set_volume(0.2)

red1 = pygame.mixer.Sound("sounds/RED.mp3")
yellow2 = pygame.mixer.Sound("sounds/YELLOW.mp3")
blue3 = pygame.mixer.Sound("sounds/BLUE.mp3")
white4 = pygame.mixer.Sound("sounds/WHITE.mp3")
green5 = pygame.mixer.Sound("sounds/GREEN.mp3")
orange6 = pygame.mixer.Sound("sounds/ORANGE.mp3")
purple7 = pygame.mixer.Sound("sounds/PURPLE.mp3")
pink8 = pygame.mixer.Sound("sounds/PINK.mp3")
brown9 = pygame.mixer.Sound("sounds/BROWN.mp3")

A2_sound = pygame.mixer.Sound("sounds/A2.mp3")
A3_sound = pygame.mixer.Sound("sounds/A3.mp3")
B2_sound = pygame.mixer.Sound("sounds/B2.mp3")
B3_sound = pygame.mixer.Sound("sounds/B3.mp3")
C3_sound = pygame.mixer.Sound("sounds/C3.mp3")
C4_sound = pygame.mixer.Sound("sounds/C4.mp3")
D3_sound = pygame.mixer.Sound("sounds/D3.mp3")
D4_sound = pygame.mixer.Sound("sounds/D4.mp3")
E3_sound = pygame.mixer.Sound("sounds/E3.mp3")
E4_sound = pygame.mixer.Sound("sounds/E4.mp3")
F3_sound = pygame.mixer.Sound("sounds/F3.mp3")
G3_sound = pygame.mixer.Sound("sounds/G3.mp3")

white = (255, 255, 255)

answered_num_save = 0
correct_num_save = 0


# <========================= all Main Menu features =========================>
def menu():
    run = True

    play_button = engine.Button(display.get_width() // 2 - 90 // 2, 170, 90, 35, font, white, 'Play')
    exit_button = engine.Button(display.get_width() // 2 - 90 // 2, 240, 90, 35, font, white, 'Exit')

    while run:

        display.fill((0, 0, 0))

        w = screen.get_size()[0] / 600
        h = screen.get_size()[1] / 400

        mpos = list(pygame.mouse.get_pos())
        mpos[0] = mpos[0] / w
        mpos[1] = mpos[1] / h

        text = tfont.render('Perfect Chord', True, white)
        display.blit(text, (display.get_width() // 2 - text.get_width() // 2, 80))

        if play_button.is_over(mpos):
            play_button.draw(display, (255, 255, 255, 100))
        else:
            play_button.draw(display, (50, 50, 50, 0))
        if exit_button.is_over(mpos):
            exit_button.draw(display, (255, 255, 255, 100))
        else:
            exit_button.draw(display, (50, 50, 50, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.is_over(mpos):
                    level_picker()
                if exit_button.is_over(mpos):
                    sys.exit()

        surf = pygame.transform.scale(display, screen.get_size())
        screen.blit(surf, (0, 0))
        pygame.display.update()


def level_picker():
    run = True

    Level1_button = engine.Button(35, 50, 130, 35, font, white, 'Level 1')
    Level2_button = engine.Button(235, 50, 130, 35, font, white, 'Level 2')
    Level3_button = engine.Button(435, 50, 130, 35, font, white, 'Level 3')
    Level4_button = engine.Button(35, 130, 130, 35, font, white, 'Level 4')
    Level5_button = engine.Button(235, 130, 130, 35, font, white, 'Level 5')
    Level6_button = engine.Button(435, 130, 130, 35, font, white, 'Level 6')
    Level7_button = engine.Button(35, 210, 130, 35, font, white, 'Level 7')
    Level8_button = engine.Button(235, 210, 130, 35, font, white, 'Level 8')

    while run:

        display.fill((0, 0, 0))

        w = screen.get_size()[0] / 600
        h = screen.get_size()[1] / 400

        mpos = list(pygame.mouse.get_pos())
        mpos[0] = mpos[0] / w
        mpos[1] = mpos[1] / h

        if Level1_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (35 - i, 50 - i, 130, 35), 1)
            Level1_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (35 - i, 50 - i, 130, 35), 1)
            Level1_button.draw(display, (50, 50, 50, 0))
        if Level2_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (235 - i, 50 - i, 130, 35), 1)
            Level2_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (235 - i, 50 - i, 130, 35), 1)
            Level2_button.draw(display, (50, 50, 50, 0))
        if Level3_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (435 - i, 50 - i, 130, 35), 1)
            Level3_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (435 - i, 50 - i, 130, 35), 1)
            Level3_button.draw(display, (50, 50, 50, 0))
        if Level4_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (35 - i, 130 - i, 130, 35), 1)
            Level4_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (35 - i, 130 - i, 130, 35), 1)
            Level4_button.draw(display, (50, 50, 50, 0))
        if Level5_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (235 - i, 130 - i, 130, 35), 1)
            Level5_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (235 - i, 130 - i, 130, 35), 1)
            Level5_button.draw(display, (50, 50, 50, 0))
        if Level6_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (435 - i, 130 - i, 130, 35), 1)
            Level6_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (435 - i, 130 - i, 130, 35), 1)
            Level6_button.draw(display, (50, 50, 50, 0))
        if Level7_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (35 - i, 210 - i, 130, 35), 1)
            Level7_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (35 - i, 210 - i, 130, 35), 1)
            Level7_button.draw(display, (50, 50, 50, 0))
        if Level8_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (235 - i, 210 - i, 130, 35), 1)
            Level8_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255), (235 - i, 210 - i, 130, 35), 1)
            Level8_button.draw(display, (50, 50, 50, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Level1_button.is_over(mpos):
                    level1(0, 0, 'inactive')
                if Level2_button.is_over(mpos):
                    level2(0, 0, 'inactive')
                if Level3_button.is_over(mpos):
                    level3(0, 0, 'inactive')
                if Level4_button.is_over(mpos):
                    level4(0, 0, 'inactive')
                if Level5_button.is_over(mpos):
                    level5(0, 0, 'inactive')
                if Level6_button.is_over(mpos):
                    level6(0, 0, 'inactive')
                if Level7_button.is_over(mpos):
                    level7(0, 0, 'inactive')
                if Level8_button.is_over(mpos):
                    level8(0, 0, 'inactive')
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        surf = pygame.transform.scale(display, screen.get_size())
        screen.blit(surf, (0, 0))
        pygame.display.update()


# change all function to have another chord
def channel_check():
    for i in range(25):
        if pygame.mixer.Channel(i).get_busy():
            return False
        else:
            continue
    return True


def answered_counter(nm, x, y):
    answered = sfont.render(f'Answered: {nm}', True, white)
    display.blit(answered, (x - answered.get_width() // 2, y))


def correct_counter(nm, x, y):
    correct_answered = sfont.render(f'Correct: {nm}', True, white)
    display.blit(correct_answered, (x - correct_answered.get_width() // 2, y))


def active_channel_check_off():
    for i in range(25):
        if pygame.mixer.Channel(i).get_busy():
            pygame.mixer.Channel(i).stop()


def incorrect_func(answ, answered_num, correct_num, level, guessing_mode):
    run = True

    C3_active = False
    A2_active = False
    A3_active = False
    B2_active = False
    B3_active = False
    C4_active = False
    D3_active = False
    D4_active = False
    E3_active = False
    E4_active = False
    F_active = False
    G_active = False

    close_button = engine.Button(display.get_width() // 2 - 90 // 2, 230, 90, 35, font, white, 'Close')

    C3 = pygame.image.load('images/C3-city.png')
    C3_rect = C3.get_rect()
    C3_button = engine.Button(1000, 1000, C3_rect.width, C3_rect.height, font, white)

    E3 = pygame.image.load('images/E3-eagle.png')
    E3_rect = E3.get_rect()
    E3_button = engine.Button(1000, 1000, E3_rect.width, E3_rect.height, font, white)

    G = pygame.image.load('images/G-giraffe.png')
    G_rect = G.get_rect()
    G_button = engine.Button(1000, 1000, G_rect.width, G_rect.height, font, white)

    A2 = pygame.image.load('images/A2-ape.png')
    A2_rect = A2.get_rect()
    A2_button = engine.Button(1000, 1000, A2_rect.width, A2_rect.height, font, white)

    A3 = pygame.image.load('images/A3-ape.png')
    A3_rect = A3.get_rect()
    A3_button = engine.Button(1000, 1000, A3_rect.width, A3_rect.height, font, white)

    B2 = pygame.image.load('images/B2-bee.png')
    B2_rect = B2.get_rect()
    B2_button = engine.Button(1000, 1000, B2_rect.width, B2_rect.height, font, white)

    B3 = pygame.image.load('images/B3-bee.png')
    B3_rect = B3.get_rect()
    B3_button = engine.Button(1000, 1000, B3_rect.width, B3_rect.height, font, white)

    C4 = pygame.image.load('images/C4-city.png')
    C4_rect = C4.get_rect()
    C4_button = engine.Button(1000, 1000, C4_rect.width, C4_rect.height, font, white)

    D3 = pygame.image.load('images/D3-deer.png')
    D3_rect = D3.get_rect()
    D3_button = engine.Button(1000, 1000, D3_rect.width, D3_rect.height, font, white)

    D4 = pygame.image.load('images/D4-deer.png')
    D4_rect = D4.get_rect()
    D4_button = engine.Button(1000, 1000, D4_rect.width, D4_rect.height, font, white)

    E4 = pygame.image.load('images/E4-eagle.png')
    E4_rect = E4.get_rect()
    E4_button = engine.Button(1000, 1000, E4_rect.width, E4_rect.height, font, white)

    F = pygame.image.load('images/F-fish.png')
    F_rect = F.get_rect()
    F_button = engine.Button(1000, 1000, F_rect.width, F_rect.height, font, white)

    while run:

        display.fill((0, 0, 0))

        w = screen.get_size()[0] / 600
        h = screen.get_size()[1] / 400

        mpos = list(pygame.mouse.get_pos())
        mpos[0] = mpos[0] / w
        mpos[1] = mpos[1] / h

        text = font.render('The Answer Is:', True, white)
        display.blit(text, (display.get_width() // 2 - text.get_width() // 2, 80))

        if answ == 'red1':

            pygame.draw.rect(display, (255, 0, 0), (display.get_width() // 2 - 50 // 2, 140, 50, 50))

            display.blit(C3, (170, 290))
            C3_button.x = 170
            C3_button.y = 290
            if C3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (C3_button.x - i, C3_button.y - i, C3_button.width, C3_button.height), 1)

            display.blit(E3, (270, 290))
            E3_button.x = 270
            E3_button.y = 290
            if E3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (E3_button.x - i, E3_button.y - i, E3_button.width, E3_button.height), 1)

            display.blit(G, (370, 290))
            G_button.x = 370
            G_button.y = 290
            if G_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (G_button.x - i, G_button.y - i, G_button.width, G_button.height), 1)
        if answ == 'yellow2':

            pygame.draw.rect(display, (255, 255, 0), (display.get_width() // 2 - 50 // 2, 140, 50, 50))

            display.blit(C3, (170, 290))
            C3_button.x = 170
            C3_button.y = 290
            if C3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (C3_button.x - i, C3_button.y - i, C3_button.width, C3_button.height), 1)

            display.blit(F, (270, 290))
            F_button.x = 270
            F_button.y = 290
            if F_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (F_button.x - i, F_button.y - i, F_button.width, F_button.height), 1)

            display.blit(A3, (370, 290))
            A3_button.x = 370
            A3_button.y = 290
            if A3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (A3_button.x - i, A3_button.y - i, A3_button.width, A3_button.height), 1)
        if answ == 'blue3':

            pygame.draw.rect(display, (0, 0, 255), (display.get_width() // 2 - 50 // 2, 140, 50, 50))

            display.blit(B2, (170, 290))
            B2_button.x = 170
            B2_button.y = 290
            if B2_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (B2_button.x - i, B2_button.y - i, B2_button.width, B2_button.height), 1)

            display.blit(D3, (270, 290))
            D3_button.x = 270
            D3_button.y = 290
            if D3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (D3_button.x - i, D3_button.y - i, D3_button.width, D3_button.height), 1)

            display.blit(G, (370, 290))
            G_button.x = 370
            G_button.y = 290
            if G_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (G_button.x - i, G_button.y - i, G_button.width, G_button.height), 1)
        if answ == 'white4':

            pygame.draw.rect(display, (255, 255, 255), (display.get_width() // 2 - 50 // 2, 140, 50, 50))

            display.blit(A2, (170, 290))
            A2_button.x = 170
            A2_button.y = 290
            if A2_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (A2_button.x - i, A2_button.y - i, A2_button.width, A2_button.height), 1)

            display.blit(C3, (270, 290))
            C3_button.x = 270
            C3_button.y = 290
            if C3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (C3_button.x - i, C3_button.y - i, C3_button.width, C3_button.height), 1)

            display.blit(F, (370, 290))
            F_button.x = 370
            F_button.y = 290
            if F_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (F_button.x - i, F_button.y - i, F_button.width, F_button.height), 1)
        if answ == 'green5':

            pygame.draw.rect(display, (0, 255, 0), (display.get_width() // 2 - 50 // 2, 140, 50, 50))

            display.blit(D3, (170, 290))
            D3_button.x = 170
            D3_button.y = 290
            if D3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (D3_button.x - i, D3_button.y - i, D3_button.width, D3_button.height), 1)

            display.blit(G, (270, 290))
            G_button.x = 270
            G_button.y = 290
            if G_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (G_button.x - i, G_button.y - i, G_button.width, G_button.height), 1)

            display.blit(B3, (370, 290))
            B3_button.x = 370
            B3_button.y = 290
            if B3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (B3_button.x - i, B3_button.y - i, B3_button.width, B3_button.height), 1)
        if answ == 'orange6':

            pygame.draw.rect(display, (255, 69, 0), (display.get_width() // 2 - 50 // 2, 140, 50, 50))

            display.blit(E3, (170, 290))
            E3_button.x = 170
            E3_button.y = 290
            if E3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (E3_button.x - i, E3_button.y - i, E3_button.width, E3_button.height), 1)

            display.blit(G, (270, 290))
            G_button.x = 270
            G_button.y = 290
            if G_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (G_button.x - i, G_button.y - i, G_button.width, G_button.height), 1)

            display.blit(C4, (370, 290))
            C4_button.x = 370
            C4_button.y = 290
            if C4_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (C4_button.x - i, C4_button.y - i, C4_button.width, C4_button.height), 1)
        if answ == 'purple7':

            pygame.draw.rect(display, (119, 0, 200), (display.get_width() // 2 - 50 // 2, 140, 50, 50))

            display.blit(F, (170, 290))
            F_button.x = 170
            F_button.y = 290
            if F_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (F_button.x - i, F_button.y - i, F_button.width, F_button.height), 1)

            display.blit(A3, (270, 290))
            A3_button.x = 270
            A3_button.y = 290
            if A3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (A3_button.x - i, A3_button.y - i, A3_button.width, A3_button.height), 1)

            display.blit(C4, (370, 290))
            C4_button.x = 370
            C4_button.y = 290
            if C4_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (C4_button.x - i, C4_button.y - i, C4_button.width, C4_button.height), 1)
        if answ == 'pink8':

            pygame.draw.rect(display, (255, 105, 180), (display.get_width() // 2 - 50 // 2, 140, 50, 50))

            display.blit(G, (170, 290))
            G_button.x = 170
            G_button.y = 290
            if G_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (G_button.x - i, G_button.y - i, G_button.width, G_button.height), 1)

            display.blit(B3, (270, 290))
            B3_button.x = 270
            B3_button.y = 290
            if B3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (B3_button.x - i, B3_button.y - i, B3_button.width, B3_button.height), 1)

            display.blit(D4, (370, 290))
            D4_button.x = 370
            D4_button.y = 290
            if D4_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (D4_button.x - i, D4_button.y - i, D4_button.width, D4_button.height), 1)
        if answ == 'brown9':

            pygame.draw.rect(display, (150, 75, 0), (display.get_width() // 2 - 50 // 2, 140, 50, 50))

            display.blit(G, (170, 290))
            G_button.x = 170
            G_button.y = 290
            if G_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (G_button.x - i, G_button.y - i, G_button.width, G_button.height), 1)

            display.blit(C4, (270, 290))
            C4_button.x = 270
            C4_button.y = 290
            if C4_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (C4_button.x - i, C4_button.y - i, C4_button.width, C4_button.height), 1)

            display.blit(E4, (370, 290))
            E4_button.x = 370
            E4_button.y = 290
            if E4_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (E4_button.x - i, E4_button.y - i, E4_button.width, E4_button.height), 1)

        replay_sound_img = pygame.image.load('replay_sound.bmp')
        replay_sound_img = pygame.transform.scale(replay_sound_img, (40, 45))
        replay_sound_img_rect = replay_sound_img.get_rect()

        replay_sound_button = engine.Button(400, 140, replay_sound_img_rect.width, replay_sound_img_rect.height, font,
                                            white)

        display.blit(replay_sound_img, (400, 140))
        if replay_sound_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (replay_sound_button.x - i, replay_sound_button.y - i,
                                  replay_sound_button.width, replay_sound_button.height), 1)

        if C3_active and E3_active and G_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if C3_active and F_active and A3_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if B2_active and D3_active and G_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if A2_active and C3_active and F_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if D3_active and G_active and B3_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if E3_active and G_active and C4_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if F_active and A3_active and C4_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if G_active and B3_active and D4_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if G_active and C4_active and E4_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.is_over(mpos):
                    active_channel_check_off()
                    level(answered_num, correct_num, guessing_mode)
                if replay_sound_button.is_over(mpos):
                    if answ == 'red1':
                        pygame.mixer.Channel(1).play(red1)
                    if answ == 'yellow2':
                        pygame.mixer.Channel(2).play(yellow2)
                    if answ == 'blue3':
                        pygame.mixer.Channel(3).play(blue3)
                    if answ == 'white4':
                        pygame.mixer.Channel(4).play(white4)
                    if answ == 'green5':
                        pygame.mixer.Channel(5).play(green5)
                    if answ == 'orange6':
                        pygame.mixer.Channel(6).play(orange6)
                    if answ == 'purple7':
                        pygame.mixer.Channel(7).play(purple7)
                    if answ == 'pink8':
                        pygame.mixer.Channel(8).play(pink8)
                    if answ == 'brown9':
                        pygame.mixer.Channel(9).play(brown9)
                if C3_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(C3_sound)
                    C3_active = True
                if E3_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(E3_sound)
                    E3_active = True
                if G_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(G3_sound)
                    G_active = True
                if A2_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(A2_sound)
                    A2_active = True
                if A3_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(A3_sound)
                    A3_active = True
                if B2_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(B2_sound)
                    B2_active = True
                if B3_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(B3_sound)
                    B3_active = True
                if C4_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(C4_sound)
                    C4_active = True
                if D3_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(D3_sound)
                    D3_active = True
                if D4_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(D4_sound)
                    D4_active = True
                if E4_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(E4_sound)
                    E4_active = True
                if F_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(F3_sound)
                    F_active = True

        surf = pygame.transform.scale(display, screen.get_size())
        screen.blit(surf, (0, 0))
        pygame.display.update()


def correct_answ_screen(answered_num, correct_num, level, guessing_md, played_sound):
    run = True

    C3_active = False
    A2_active = False
    A3_active = False
    B2_active = False
    B3_active = False
    C4_active = False
    D3_active = False
    D4_active = False
    E3_active = False
    E4_active = False
    F_active = False
    G_active = False

    close_button = engine.Button(display.get_width() // 2 - 90 // 2, 220, 90, 35, font, white, 'Close')

    C3 = pygame.image.load('images/C3-city.png')
    C3_rect = C3.get_rect()
    C3_button = engine.Button(1000, 1000, C3_rect.width, C3_rect.height, font, white)

    E3 = pygame.image.load('images/E3-eagle.png')
    E3_rect = E3.get_rect()
    E3_button = engine.Button(1000, 1000, E3_rect.width, E3_rect.height, font, white)

    G = pygame.image.load('images/G-giraffe.png')
    G_rect = G.get_rect()
    G_button = engine.Button(1000, 1000, G_rect.width, G_rect.height, font, white)

    A2 = pygame.image.load('images/A2-ape.png')
    A2_rect = A2.get_rect()
    A2_button = engine.Button(1000, 1000, A2_rect.width, A2_rect.height, font, white)

    A3 = pygame.image.load('images/A3-ape.png')
    A3_rect = A3.get_rect()
    A3_button = engine.Button(1000, 1000, A3_rect.width, A3_rect.height, font, white)

    B2 = pygame.image.load('images/B2-bee.png')
    B2_rect = B2.get_rect()
    B2_button = engine.Button(1000, 1000, B2_rect.width, B2_rect.height, font, white)

    B3 = pygame.image.load('images/B3-bee.png')
    B3_rect = B3.get_rect()
    B3_button = engine.Button(1000, 1000, B3_rect.width, B3_rect.height, font, white)

    C4 = pygame.image.load('images/C4-city.png')
    C4_rect = C4.get_rect()
    C4_button = engine.Button(1000, 1000, C4_rect.width, C4_rect.height, font, white)

    D3 = pygame.image.load('images/D3-deer.png')
    D3_rect = D3.get_rect()
    D3_button = engine.Button(1000, 1000, D3_rect.width, D3_rect.height, font, white)

    D4 = pygame.image.load('images/D4-deer.png')
    D4_rect = D4.get_rect()
    D4_button = engine.Button(1000, 1000, D4_rect.width, D4_rect.height, font, white)

    E4 = pygame.image.load('images/E4-eagle.png')
    E4_rect = E4.get_rect()
    E4_button = engine.Button(1000, 1000, E4_rect.width, E4_rect.height, font, white)

    F = pygame.image.load('images/F-fish.png')
    F_rect = F.get_rect()
    F_button = engine.Button(1000, 1000, F_rect.width, F_rect.height, font, white)

    while run:

        display.fill((0, 0, 0))

        w = screen.get_size()[0] / 600
        h = screen.get_size()[1] / 400

        mpos = list(pygame.mouse.get_pos())
        mpos[0] = mpos[0] / w
        mpos[1] = mpos[1] / h

        checkmark_img = pygame.image.load('checkmark.bmp')
        checkmark_img = pygame.transform.scale(checkmark_img, (60, 60))

        display.blit(checkmark_img, (display.get_width() // 2 - checkmark_img.get_width() // 2, 50))

        text = font.render('Correct:', True, white)
        display.blit(text, (200, 150))

        if played_sound == 'red1':
            pygame.draw.rect(display, (255, 0, 0), (350, 140, 50, 50))

            display.blit(C3, (170, 290))
            C3_button.x = 170
            C3_button.y = 290
            if C3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (C3_button.x - i, C3_button.y - i, C3_button.width, C3_button.height), 1)

            display.blit(E3, (270, 290))
            E3_button.x = 270
            E3_button.y = 290
            if E3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (E3_button.x - i, E3_button.y - i, E3_button.width, E3_button.height), 1)

            display.blit(G, (370, 290))
            G_button.x = 370
            G_button.y = 290
            if G_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (G_button.x - i, G_button.y - i, G_button.width, G_button.height), 1)

        if played_sound == 'yellow2':
            pygame.draw.rect(display, (255, 255, 0), (350, 140, 50, 50))

            display.blit(C3, (170, 290))
            C3_button.x = 170
            C3_button.y = 290
            if C3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (C3_button.x - i, C3_button.y - i, C3_button.width, C3_button.height), 1)

            display.blit(F, (270, 290))
            F_button.x = 270
            F_button.y = 290
            if F_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (F_button.x - i, F_button.y - i, F_button.width, F_button.height), 1)

            display.blit(A3, (370, 290))
            A3_button.x = 370
            A3_button.y = 290
            if A3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (A3_button.x - i, A3_button.y - i, A3_button.width, A3_button.height), 1)

        if played_sound == 'blue3':
            pygame.draw.rect(display, (0, 0, 255), (350, 140, 50, 50))

            display.blit(B2, (170, 290))
            B2_button.x = 170
            B2_button.y = 290
            if B2_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (B2_button.x - i, B2_button.y - i, B2_button.width, B2_button.height), 1)

            display.blit(D3, (270, 290))
            D3_button.x = 270
            D3_button.y = 290
            if D3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (D3_button.x - i, D3_button.y - i, D3_button.width, D3_button.height), 1)

            display.blit(G, (370, 290))
            G_button.x = 370
            G_button.y = 290
            if G_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (G_button.x - i, G_button.y - i, G_button.width, G_button.height), 1)

        if played_sound == 'white4':
            pygame.draw.rect(display, (255, 255, 255), (350, 140, 50, 50))

            display.blit(A2, (170, 290))
            A2_button.x = 170
            A2_button.y = 290
            if A2_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (A2_button.x - i, A2_button.y - i, A2_button.width, A2_button.height), 1)

            display.blit(C3, (270, 290))
            C3_button.x = 270
            C3_button.y = 290
            if C3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (C3_button.x - i, C3_button.y - i, C3_button.width, C3_button.height), 1)

            display.blit(F, (370, 290))
            F_button.x = 370
            F_button.y = 290
            if F_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (F_button.x - i, F_button.y - i, F_button.width, F_button.height), 1)

        if played_sound == 'green5':
            pygame.draw.rect(display, (0, 255, 0), (350, 140, 50, 50))

            display.blit(D3, (170, 290))
            D3_button.x = 170
            D3_button.y = 290
            if D3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (D3_button.x - i, D3_button.y - i, D3_button.width, D3_button.height), 1)

            display.blit(G, (270, 290))
            G_button.x = 270
            G_button.y = 290
            if G_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (G_button.x - i, G_button.y - i, G_button.width, G_button.height), 1)

            display.blit(B3, (370, 290))
            B3_button.x = 370
            B3_button.y = 290
            if B3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (B3_button.x - i, B3_button.y - i, B3_button.width, B3_button.height), 1)

        if played_sound == 'orange6':
            pygame.draw.rect(display, (255, 69, 0), (350, 140, 50, 50))

            display.blit(E3, (170, 290))
            E3_button.x = 170
            E3_button.y = 290
            if E3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (E3_button.x - i, E3_button.y - i, E3_button.width, E3_button.height), 1)

            display.blit(G, (270, 290))
            G_button.x = 270
            G_button.y = 290
            if G_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (G_button.x - i, G_button.y - i, G_button.width, G_button.height), 1)

            display.blit(C4, (370, 290))
            C4_button.x = 370
            C4_button.y = 290
            if C4_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (C4_button.x - i, C4_button.y - i, C4_button.width, C4_button.height), 1)

        if played_sound == 'purple7':
            pygame.draw.rect(display, (119, 0, 200), (350, 140, 50, 50))

            display.blit(F, (170, 290))
            F_button.x = 170
            F_button.y = 290
            if F_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (F_button.x - i, F_button.y - i, F_button.width, F_button.height), 1)

            display.blit(A3, (270, 290))
            A3_button.x = 270
            A3_button.y = 290
            if A3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (A3_button.x - i, A3_button.y - i, A3_button.width, A3_button.height), 1)

            display.blit(C4, (370, 290))
            C4_button.x = 370
            C4_button.y = 290
            if C4_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (C4_button.x - i, C4_button.y - i, C4_button.width, C4_button.height), 1)

        if played_sound == 'pink8':
            pygame.draw.rect(display, (255, 105, 180), (350, 140, 50, 50))

            display.blit(G, (170, 290))
            G_button.x = 170
            G_button.y = 290
            if G_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (G_button.x - i, G_button.y - i, G_button.width, G_button.height), 1)

            display.blit(B3, (270, 290))
            B3_button.x = 270
            B3_button.y = 290
            if B3_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (B3_button.x - i, B3_button.y - i, B3_button.width, B3_button.height), 1)

            display.blit(D4, (370, 290))
            D4_button.x = 370
            D4_button.y = 290
            if D4_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (D4_button.x - i, D4_button.y - i, D4_button.width, D4_button.height), 1)

        if played_sound == 'brown9':
            pygame.draw.rect(display, (150, 75, 0), (350, 140, 50, 50))

            display.blit(G, (170, 290))
            G_button.x = 170
            G_button.y = 290
            if G_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (G_button.x - i, G_button.y - i, G_button.width, G_button.height), 1)

            display.blit(C4, (270, 290))
            C4_button.x = 270
            C4_button.y = 290
            if C4_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (C4_button.x - i, C4_button.y - i, C4_button.width, C4_button.height), 1)

            display.blit(E4, (370, 290))
            E4_button.x = 370
            E4_button.y = 290
            if E4_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (E4_button.x - i, E4_button.y - i, E4_button.width, E4_button.height), 1)

        replay_sound_img = pygame.image.load('replay_sound.bmp')
        replay_sound_img = pygame.transform.scale(replay_sound_img, (40, 45))
        replay_sound_img_rect = replay_sound_img.get_rect()

        replay_sound_button = engine.Button(420, 140, replay_sound_img_rect.width, replay_sound_img_rect.height, font,
                                            white)

        display.blit(replay_sound_img, (420, 140))
        if replay_sound_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (replay_sound_button.x - i, replay_sound_button.y - i,
                                  replay_sound_button.width, replay_sound_button.height), 1)

        if C3_active and E3_active and G_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if C3_active and F_active and A3_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if B2_active and D3_active and G_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if A2_active and C3_active and F_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if D3_active and G_active and B3_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if E3_active and G_active and C4_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if F_active and A3_active and C4_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if G_active and B3_active and D4_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        if G_active and C4_active and E4_active:
            if close_button.is_over(mpos):
                close_button.draw(display, (255, 255, 255, 100))
            else:
                close_button.draw(display, (50, 50, 50, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.is_over(mpos):
                    active_channel_check_off()
                    level(answered_num, correct_num, guessing_md)
                if replay_sound_button.is_over(mpos):
                    if played_sound == 'red1':
                        pygame.mixer.Channel(1).play(red1)
                    if played_sound == 'yellow2':
                        pygame.mixer.Channel(2).play(yellow2)
                    if played_sound == 'blue3':
                        pygame.mixer.Channel(3).play(blue3)
                    if played_sound == 'white4':
                        pygame.mixer.Channel(4).play(white4)
                    if played_sound == 'green5':
                        pygame.mixer.Channel(5).play(green5)
                    if played_sound == 'orange6':
                        pygame.mixer.Channel(6).play(orange6)
                    if played_sound == 'purple7':
                        pygame.mixer.Channel(7).play(purple7)
                    if played_sound == 'pink8':
                        pygame.mixer.Channel(8).play(pink8)
                    if played_sound == 'brown9':
                        pygame.mixer.Channel(9).play(brown9)
                if C3_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(C3_sound)
                    C3_active = True
                if E3_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(E3_sound)
                    E3_active = True
                if G_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(G3_sound)
                    G_active = True
                if A2_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(A2_sound)
                    A2_active = True
                if A3_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(A3_sound)
                    A3_active = True
                if B2_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(B2_sound)
                    B2_active = True
                if B3_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(B3_sound)
                    B3_active = True
                if C4_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(C4_sound)
                    C4_active = True
                if D3_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(D3_sound)
                    D3_active = True
                if D4_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(D4_sound)
                    D4_active = True
                if E4_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(E4_sound)
                    E4_active = True
                if F_button.is_over(mpos):
                    pygame.mixer.Channel(11).play(F3_sound)
                    F_active = True

        surf = pygame.transform.scale(display, screen.get_size())
        screen.blit(surf, (0, 0))
        pygame.display.update()


def active_channel_check():
    for i in range(25):
        if pygame.mixer.Channel(i).get_busy():
            played_sound = i
            return played_sound


def stats(answered_num, correct_num):
    run = True

    back_button = engine.Button(display.get_width() // 2 - 90 // 2, 250, 90, 35, font, white, '<--')

    while run:

        display.fill((0, 0, 0))

        w = screen.get_size()[0] / 600
        h = screen.get_size()[1] / 400

        mpos = list(pygame.mouse.get_pos())
        mpos[0] = mpos[0] / w
        mpos[1] = mpos[1] / h

        answered_text = tfont.render(f'Answered: {answered_num}', True, white)
        correct_text = tfont.render(f'Correct: {correct_num}', True, white)
        display.blit(answered_text, (display.get_width() // 2 - answered_text.get_width() // 2, 60))
        display.blit(correct_text, (display.get_width() // 2 - correct_text.get_width() // 2, 120))

        if back_button.is_over(mpos):
            back_button.draw(display, (50, 50, 50, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (back_button.x - i, back_button.y - i, back_button.width, back_button.height),
                                 1)
        else:
            back_button.draw(display, (50, 50, 50, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_over(mpos):
                    level_picker()

        surf = pygame.transform.scale(display, screen.get_size())
        screen.blit(surf, (0, 0))
        pygame.display.update()


def level1(answered_num_save, correct_num_save, guessing_md):
    run = True

    answered_num = answered_num_save
    correct_num = correct_num_save

    played_sound = ''

    guessing_mode = guessing_md

    listen_button = engine.Button(display.get_width() // 2 - 200 // 2, 170, 200, 35, font, white, 'Play Sound')
    red_button = engine.Button(display.get_width() // 2 - 150 // 2, 240, 50, 50, font, white)
    yellow_button = engine.Button(display.get_width() // 2 + 25, 240, 50, 50, font, white)
    back_button = engine.Button(50, 50, 55, 40, font, white, '<--')

    while run:
        display.fill((0, 0, 0))

        w = screen.get_size()[0] / 600
        h = screen.get_size()[1] / 400

        mpos = list(pygame.mouse.get_pos())
        mpos[0] = mpos[0] / w
        mpos[1] = mpos[1] / h

        replay_sound_img = pygame.image.load('replay_sound.bmp')
        replay_sound_img = pygame.transform.scale(replay_sound_img, (40, 45))
        replay_sound_img_rect = replay_sound_img.get_rect()

        replay_sound_button = engine.Button(450, 160, replay_sound_img_rect.width, replay_sound_img_rect.height, font,
                                            white)

        if guessing_mode == 'active':
            display.blit(replay_sound_img, (450, 160))
            if replay_sound_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (replay_sound_button.x - i, replay_sound_button.y - i,
                                      replay_sound_button.width, replay_sound_button.height), 1)

        if back_button.is_over(mpos):
            back_button.draw(display, (50, 50, 50, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (back_button.x - i, back_button.y - i, back_button.width, back_button.height),
                                 1)
        else:
            back_button.draw(display, (50, 50, 50, 0))

        if listen_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (50, 50, 50, 0))

        if red_button.is_over(mpos):
            red_button.draw(display, (255, 0, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (red_button.x - i, red_button.y - i, red_button.width, red_button.height),
                                 1)
        else:
            red_button.draw(display, (255, 0, 0))

        if yellow_button.is_over(mpos):
            yellow_button.draw(display, (255, 255, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (yellow_button.x - i, yellow_button.y - i, yellow_button.width, yellow_button.height),
                                 1)
        else:
            yellow_button.draw(display, (255, 255, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.is_over(mpos):
                    if not channel_check():
                        pygame.mixer.Channel(active_channel_check()).stop()
                        level_picker()
                    else:
                        level_picker()

                if listen_button.is_over(mpos):
                    randomsoundlvl1 = random.choice([red1, yellow2])
                    if randomsoundlvl1 == red1 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(1).play(red1)
                        played_sound = 'red1'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == yellow2 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(2).play(yellow2)
                        played_sound = 'yellow2'
                        guessing_mode = 'active'

                if replay_sound_button.is_over(mpos):
                    if played_sound == 'red1':
                        pygame.mixer.Channel(1).play(red1)
                    if played_sound == 'yellow2':
                        pygame.mixer.Channel(2).play(yellow2)

                if red_button.is_over(mpos) and played_sound == 'red1':
                    pygame.mixer.Channel(1).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level1, guessing_mode, played_sound)
                if red_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if red_button.is_over(mpos) and played_sound != 'red1':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level1, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level1, guessing_mode)

                if yellow_button.is_over(mpos) and played_sound == 'yellow2':
                    pygame.mixer.Channel(2).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level1, guessing_mode, played_sound)
                if yellow_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if yellow_button.is_over(mpos) and played_sound != 'yellow2':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level1, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level1, guessing_mode)

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        answered_counter(answered_num, display.get_width() // 2, 60)
        correct_counter(correct_num, display.get_width() // 2, 100)

        if answered_num == 30:
            stats(answered_num, correct_num)

        surf = pygame.transform.scale(display, screen.get_size())
        screen.blit(surf, (0, 0))
        pygame.display.update()


def level2(answered_num_save, correct_num_save, guessing_md):
    run = True

    answered_num = answered_num_save
    correct_num = correct_num_save

    played_sound = ''

    guessing_mode = guessing_md

    listen_button = engine.Button(display.get_width() // 2 - 200 // 2, 170, 200, 35, font, white, 'Play Sound')
    red_button = engine.Button(195, 240, 50, 50, font, white)
    yellow_button = engine.Button(275, 240, 50, 50, font, white)
    blue_button = engine.Button(355, 240, 50, 50, font, white)
    back_button = engine.Button(50, 50, 55, 40, font, white, '<--')

    while run:
        display.fill((0, 0, 0))

        w = screen.get_size()[0] / 600
        h = screen.get_size()[1] / 400

        mpos = list(pygame.mouse.get_pos())
        mpos[0] = mpos[0] / w
        mpos[1] = mpos[1] / h

        replay_sound_img = pygame.image.load('replay_sound.bmp')
        replay_sound_img = pygame.transform.scale(replay_sound_img, (40, 45))
        replay_sound_img_rect = replay_sound_img.get_rect()

        replay_sound_button = engine.Button(450, 160, replay_sound_img_rect.width, replay_sound_img_rect.height, font,
                                            white)

        if guessing_mode == 'active':
            display.blit(replay_sound_img, (450, 160))
            if replay_sound_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (replay_sound_button.x - i, replay_sound_button.y - i,
                                      replay_sound_button.width, replay_sound_button.height), 1)

        if back_button.is_over(mpos):
            back_button.draw(display, (50, 50, 50, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (back_button.x - i, back_button.y - i, back_button.width, back_button.height),
                                 1)
        else:
            back_button.draw(display, (50, 50, 50, 0))

        if listen_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (50, 50, 50, 0))

        if red_button.is_over(mpos):
            red_button.draw(display, (255, 0, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (red_button.x - i, red_button.y - i, red_button.width, red_button.height),
                                 1)
        else:
            red_button.draw(display, (255, 0, 0))

        if yellow_button.is_over(mpos):
            yellow_button.draw(display, (255, 255, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (yellow_button.x - i, yellow_button.y - i, yellow_button.width, yellow_button.height),
                                 1)
        else:
            yellow_button.draw(display, (255, 255, 0))

        if blue_button.is_over(mpos):
            blue_button.draw(display, (0, 0, 255))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (blue_button.x - i, blue_button.y - i, blue_button.width, blue_button.height),
                                 1)
        else:
            blue_button.draw(display, (0, 0, 255))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.is_over(mpos):
                    if not channel_check():
                        pygame.mixer.Channel(active_channel_check()).stop()
                        level_picker()
                    else:
                        level_picker()

                if listen_button.is_over(mpos):
                    randomsoundlvl1 = random.choice([red1, yellow2, blue3])
                    if randomsoundlvl1 == red1 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(1).play(red1)
                        played_sound = 'red1'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == yellow2 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(2).play(yellow2)
                        played_sound = 'yellow2'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == blue3 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(3).play(blue3)
                        played_sound = 'blue3'
                        guessing_mode = 'active'

                if replay_sound_button.is_over(mpos):
                    if played_sound == 'red1':
                        pygame.mixer.Channel(1).play(red1)
                    if played_sound == 'yellow2':
                        pygame.mixer.Channel(2).play(yellow2)
                    if played_sound == 'blue3':
                        pygame.mixer.Channel(3).play(blue3)

                if red_button.is_over(mpos) and played_sound == 'red1':
                    pygame.mixer.Channel(1).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level2, guessing_mode, played_sound)
                if red_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if red_button.is_over(mpos) and played_sound != 'red1':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level2, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level2, guessing_mode)

                if yellow_button.is_over(mpos) and played_sound == 'yellow2':
                    pygame.mixer.Channel(2).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level2, guessing_mode, played_sound)
                if yellow_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if yellow_button.is_over(mpos) and played_sound != 'yellow2':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level2, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level2, guessing_mode)

                if blue_button.is_over(mpos) and played_sound == 'blue3':
                    pygame.mixer.Channel(3).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level2, guessing_mode, played_sound)
                if blue_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if blue_button.is_over(mpos) and played_sound != 'blue3':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level2, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level2, guessing_mode)

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        answered_counter(answered_num, display.get_width() // 2, 60)
        correct_counter(correct_num, display.get_width() // 2, 100)

        if answered_num == 30:
            stats(answered_num, correct_num)

        surf = pygame.transform.scale(display, screen.get_size())
        screen.blit(surf, (0, 0))
        pygame.display.update()


def level3(answered_num_save, correct_num_save, guessing_md):
    run = True

    answered_num = answered_num_save
    correct_num = correct_num_save

    played_sound = ''

    guessing_mode = guessing_md

    listen_button = engine.Button(display.get_width() // 2 - 200 // 2, 170, 200, 35, font, white, 'Play Sound')
    red_button = engine.Button(155, 240, 50, 50, font, white)
    yellow_button = engine.Button(235, 240, 50, 50, font, white)
    blue_button = engine.Button(315, 240, 50, 50, font, white)
    white_button = engine.Button(395, 240, 50, 50, font, white)
    back_button = engine.Button(50, 50, 55, 40, font, white, '<--')

    while run:
        display.fill((0, 0, 0))

        w = screen.get_size()[0] / 600
        h = screen.get_size()[1] / 400

        mpos = list(pygame.mouse.get_pos())
        mpos[0] = mpos[0] / w
        mpos[1] = mpos[1] / h

        replay_sound_img = pygame.image.load('replay_sound.bmp')
        replay_sound_img = pygame.transform.scale(replay_sound_img, (40, 45))
        replay_sound_img_rect = replay_sound_img.get_rect()

        replay_sound_button = engine.Button(450, 160, replay_sound_img_rect.width, replay_sound_img_rect.height, font,
                                            white)

        if guessing_mode == 'active':
            display.blit(replay_sound_img, (450, 160))
            if replay_sound_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (replay_sound_button.x - i, replay_sound_button.y - i,
                                      replay_sound_button.width, replay_sound_button.height), 1)

        if back_button.is_over(mpos):
            back_button.draw(display, (50, 50, 50, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (back_button.x - i, back_button.y - i, back_button.width, back_button.height),
                                 1)
        else:
            back_button.draw(display, (50, 50, 50, 0))

        if listen_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (50, 50, 50, 0))

        if red_button.is_over(mpos):
            red_button.draw(display, (255, 0, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (red_button.x - i, red_button.y - i, red_button.width, red_button.height),
                                 1)
        else:
            red_button.draw(display, (255, 0, 0))

        if yellow_button.is_over(mpos):
            yellow_button.draw(display, (255, 255, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (yellow_button.x - i, yellow_button.y - i, yellow_button.width, yellow_button.height),
                                 1)
        else:
            yellow_button.draw(display, (255, 255, 0))

        if blue_button.is_over(mpos):
            blue_button.draw(display, (0, 0, 255))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (blue_button.x - i, blue_button.y - i, blue_button.width, blue_button.height),
                                 1)
        else:
            blue_button.draw(display, (0, 0, 255))

        if white_button.is_over(mpos):
            white_button.draw(display, (255, 255, 255))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (white_button.x - i, white_button.y - i, white_button.width, white_button.height),
                                 1)
        else:
            white_button.draw(display, (255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.is_over(mpos):
                    if not channel_check():
                        pygame.mixer.Channel(active_channel_check()).stop()
                        level_picker()
                    else:
                        level_picker()

                if listen_button.is_over(mpos):
                    randomsoundlvl1 = random.choice([red1, yellow2, blue3, white4])
                    if randomsoundlvl1 == red1 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(1).play(red1)
                        played_sound = 'red1'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == yellow2 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(2).play(yellow2)
                        played_sound = 'yellow2'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == blue3 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(3).play(blue3)
                        played_sound = 'blue3'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == white4 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(4).play(white4)
                        played_sound = 'white4'
                        guessing_mode = 'active'

                if replay_sound_button.is_over(mpos):
                    if played_sound == 'red1':
                        pygame.mixer.Channel(1).play(red1)
                    if played_sound == 'yellow2':
                        pygame.mixer.Channel(2).play(yellow2)
                    if played_sound == 'blue3':
                        pygame.mixer.Channel(3).play(blue3)
                    if played_sound == 'white4':
                        pygame.mixer.Channel(4).play(white4)

                if red_button.is_over(mpos) and played_sound == 'red1':
                    pygame.mixer.Channel(1).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level3, guessing_mode, played_sound)
                if red_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if red_button.is_over(mpos) and played_sound != 'red1':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level3, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level3, guessing_mode)

                if yellow_button.is_over(mpos) and played_sound == 'yellow2':
                    pygame.mixer.Channel(2).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level3, guessing_mode, played_sound)
                if yellow_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if yellow_button.is_over(mpos) and played_sound != 'yellow2':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level3, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level3, guessing_mode)

                if blue_button.is_over(mpos) and played_sound == 'blue3':
                    pygame.mixer.Channel(3).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level3, guessing_mode, played_sound)
                if blue_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if blue_button.is_over(mpos) and played_sound != 'blue3':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level3, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level3, guessing_mode)

                if white_button.is_over(mpos) and played_sound == 'white4':
                    pygame.mixer.Channel(4).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level3, guessing_mode, played_sound)
                if white_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if white_button.is_over(mpos) and played_sound != 'white4':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level3, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level3, guessing_mode)

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        answered_counter(answered_num, display.get_width() // 2, 60)
        correct_counter(correct_num, display.get_width() // 2, 100)

        if answered_num == 30:
            stats(answered_num, correct_num)

        surf = pygame.transform.scale(display, screen.get_size())
        screen.blit(surf, (0, 0))
        pygame.display.update()


def level4(answered_num_save, correct_num_save, guessing_md):
    run = True

    answered_num = answered_num_save
    correct_num = correct_num_save

    played_sound = ''

    guessing_mode = guessing_md

    listen_button = engine.Button(display.get_width() // 2 - 200 // 2, 170, 200, 35, font, white, 'Play Sound')
    red_button = engine.Button(115, 240, 50, 50, font, white)
    yellow_button = engine.Button(195, 240, 50, 50, font, white)
    blue_button = engine.Button(275, 240, 50, 50, font, white)
    white_button = engine.Button(355, 240, 50, 50, font, white)
    green_button = engine.Button(435, 240, 50, 50, font, white)
    back_button = engine.Button(50, 50, 55, 40, font, white, '<--')

    while run:
        display.fill((0, 0, 0))

        w = screen.get_size()[0] / 600
        h = screen.get_size()[1] / 400

        mpos = list(pygame.mouse.get_pos())
        mpos[0] = mpos[0] / w
        mpos[1] = mpos[1] / h

        replay_sound_img = pygame.image.load('replay_sound.bmp')
        replay_sound_img = pygame.transform.scale(replay_sound_img, (40, 45))
        replay_sound_img_rect = replay_sound_img.get_rect()

        replay_sound_button = engine.Button(450, 160, replay_sound_img_rect.width, replay_sound_img_rect.height, font,
                                            white)

        if guessing_mode == 'active':
            display.blit(replay_sound_img, (450, 160))
            if replay_sound_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (replay_sound_button.x - i, replay_sound_button.y - i,
                                      replay_sound_button.width, replay_sound_button.height), 1)

        if back_button.is_over(mpos):
            back_button.draw(display, (50, 50, 50, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (back_button.x - i, back_button.y - i, back_button.width, back_button.height),
                                 1)
        else:
            back_button.draw(display, (50, 50, 50, 0))

        if listen_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (50, 50, 50, 0))

        if red_button.is_over(mpos):
            red_button.draw(display, (255, 0, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (red_button.x - i, red_button.y - i, red_button.width, red_button.height),
                                 1)
        else:
            red_button.draw(display, (255, 0, 0))

        if yellow_button.is_over(mpos):
            yellow_button.draw(display, (255, 255, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (yellow_button.x - i, yellow_button.y - i, yellow_button.width, yellow_button.height),
                                 1)
        else:
            yellow_button.draw(display, (255, 255, 0))

        if blue_button.is_over(mpos):
            blue_button.draw(display, (0, 0, 255))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (blue_button.x - i, blue_button.y - i, blue_button.width, blue_button.height),
                                 1)
        else:
            blue_button.draw(display, (0, 0, 255))

        if white_button.is_over(mpos):
            white_button.draw(display, (255, 255, 255))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (white_button.x - i, white_button.y - i, white_button.width, white_button.height),
                                 1)
        else:
            white_button.draw(display, (255, 255, 255))

        if green_button.is_over(mpos):
            green_button.draw(display, (0, 255, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (green_button.x - i, green_button.y - i, green_button.width, green_button.height),
                                 1)
        else:
            green_button.draw(display, (0, 255, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.is_over(mpos):
                    if not channel_check():
                        pygame.mixer.Channel(active_channel_check()).stop()
                        level_picker()
                    else:
                        level_picker()

                if listen_button.is_over(mpos):
                    randomsoundlvl1 = random.choice([red1, yellow2, blue3, white4, green5])
                    if randomsoundlvl1 == red1 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(1).play(red1)
                        played_sound = 'red1'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == yellow2 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(2).play(yellow2)
                        played_sound = 'yellow2'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == blue3 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(3).play(blue3)
                        played_sound = 'blue3'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == white4 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(4).play(white4)
                        played_sound = 'white4'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == green5 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(5).play(green5)
                        played_sound = 'green5'
                        guessing_mode = 'active'

                if replay_sound_button.is_over(mpos):
                    if played_sound == 'red1':
                        pygame.mixer.Channel(1).play(red1)
                    if played_sound == 'yellow2':
                        pygame.mixer.Channel(2).play(yellow2)
                    if played_sound == 'blue3':
                        pygame.mixer.Channel(3).play(blue3)
                    if played_sound == 'white4':
                        pygame.mixer.Channel(4).play(white4)
                    if played_sound == 'green5':
                        pygame.mixer.Channel(5).play(green5)

                if red_button.is_over(mpos) and played_sound == 'red1':
                    pygame.mixer.Channel(1).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level4, guessing_mode, played_sound)
                if red_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if red_button.is_over(mpos) and played_sound != 'red1':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level4, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level4, guessing_mode)

                if yellow_button.is_over(mpos) and played_sound == 'yellow2':
                    pygame.mixer.Channel(2).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level4, guessing_mode, played_sound)
                if yellow_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if yellow_button.is_over(mpos) and played_sound != 'yellow2':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level4, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level4, guessing_mode)

                if blue_button.is_over(mpos) and played_sound == 'blue3':
                    pygame.mixer.Channel(3).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level4, guessing_mode, played_sound)
                if blue_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if blue_button.is_over(mpos) and played_sound != 'blue3':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level4, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level4, guessing_mode)

                if white_button.is_over(mpos) and played_sound == 'white4':
                    pygame.mixer.Channel(4).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level4, guessing_mode, played_sound)
                if white_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if white_button.is_over(mpos) and played_sound != 'white4':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level4, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level4, guessing_mode)

                if green_button.is_over(mpos) and played_sound == 'green5':
                    pygame.mixer.Channel(5).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level4, guessing_mode, played_sound)
                if green_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if green_button.is_over(mpos) and played_sound != 'green5':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level4, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level4, guessing_mode)

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        answered_counter(answered_num, display.get_width() // 2, 60)
        correct_counter(correct_num, display.get_width() // 2, 100)

        if answered_num == 30:
            stats(answered_num, correct_num)

        surf = pygame.transform.scale(display, screen.get_size())
        screen.blit(surf, (0, 0))
        pygame.display.update()


def level5(answered_num_save, correct_num_save, guessing_md):
    run = True

    answered_num = answered_num_save
    correct_num = correct_num_save

    played_sound = ''

    guessing_mode = guessing_md

    listen_button = engine.Button(display.get_width() // 2 - 200 // 2, 170, 200, 35, font, white, 'Play Sound')
    red_button = engine.Button(115, 240, 50, 50, font, white)
    yellow_button = engine.Button(195, 240, 50, 50, font, white)
    blue_button = engine.Button(275, 240, 50, 50, font, white)
    white_button = engine.Button(355, 240, 50, 50, font, white)
    green_button = engine.Button(435, 240, 50, 50, font, white)
    orange_button = engine.Button(115, 320, 50, 50, font, white)
    back_button = engine.Button(50, 50, 55, 40, font, white, '<--')

    while run:
        display.fill((0, 0, 0))

        w = screen.get_size()[0] / 600
        h = screen.get_size()[1] / 400

        mpos = list(pygame.mouse.get_pos())
        mpos[0] = mpos[0] / w
        mpos[1] = mpos[1] / h

        replay_sound_img = pygame.image.load('replay_sound.bmp')
        replay_sound_img = pygame.transform.scale(replay_sound_img, (40, 45))
        replay_sound_img_rect = replay_sound_img.get_rect()

        replay_sound_button = engine.Button(450, 160, replay_sound_img_rect.width, replay_sound_img_rect.height, font,
                                            white)

        if guessing_mode == 'active':
            display.blit(replay_sound_img, (450, 160))
            if replay_sound_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (replay_sound_button.x - i, replay_sound_button.y - i,
                                      replay_sound_button.width, replay_sound_button.height), 1)

        if back_button.is_over(mpos):
            back_button.draw(display, (50, 50, 50, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (back_button.x - i, back_button.y - i, back_button.width, back_button.height),
                                 1)
        else:
            back_button.draw(display, (50, 50, 50, 0))

        if listen_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (50, 50, 50, 0))

        if red_button.is_over(mpos):
            red_button.draw(display, (255, 0, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (red_button.x - i, red_button.y - i, red_button.width, red_button.height),
                                 1)
        else:
            red_button.draw(display, (255, 0, 0))

        if yellow_button.is_over(mpos):
            yellow_button.draw(display, (255, 255, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (yellow_button.x - i, yellow_button.y - i, yellow_button.width, yellow_button.height),
                                 1)
        else:
            yellow_button.draw(display, (255, 255, 0))

        if blue_button.is_over(mpos):
            blue_button.draw(display, (0, 0, 255))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (blue_button.x - i, blue_button.y - i, blue_button.width, blue_button.height),
                                 1)
        else:
            blue_button.draw(display, (0, 0, 255))

        if white_button.is_over(mpos):
            white_button.draw(display, (255, 255, 255))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (white_button.x - i, white_button.y - i, white_button.width, white_button.height),
                                 1)
        else:
            white_button.draw(display, (255, 255, 255))

        if green_button.is_over(mpos):
            green_button.draw(display, (0, 255, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (green_button.x - i, green_button.y - i, green_button.width, green_button.height),
                                 1)
        else:
            green_button.draw(display, (0, 255, 0))

        if orange_button.is_over(mpos):
            orange_button.draw(display, (255, 69, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (orange_button.x - i, orange_button.y - i, orange_button.width, orange_button.height),
                                 1)
        else:
            orange_button.draw(display, (255, 69, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.is_over(mpos):
                    if not channel_check():
                        pygame.mixer.Channel(active_channel_check()).stop()
                        level_picker()
                    else:
                        level_picker()

                if listen_button.is_over(mpos):
                    randomsoundlvl1 = random.choice([red1, yellow2, blue3, white4, green5, orange6])
                    if randomsoundlvl1 == red1 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(1).play(red1)
                        played_sound = 'red1'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == yellow2 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(2).play(yellow2)
                        played_sound = 'yellow2'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == blue3 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(3).play(blue3)
                        played_sound = 'blue3'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == white4 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(4).play(white4)
                        played_sound = 'white4'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == green5 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(5).play(green5)
                        played_sound = 'green5'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == orange6 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(6).play(orange6)
                        played_sound = 'orange6'
                        guessing_mode = 'active'

                if replay_sound_button.is_over(mpos):
                    if played_sound == 'red1':
                        pygame.mixer.Channel(1).play(red1)
                    if played_sound == 'yellow2':
                        pygame.mixer.Channel(2).play(yellow2)
                    if played_sound == 'blue3':
                        pygame.mixer.Channel(3).play(blue3)
                    if played_sound == 'white4':
                        pygame.mixer.Channel(4).play(white4)
                    if played_sound == 'green5':
                        pygame.mixer.Channel(5).play(green5)
                    if played_sound == 'orange6':
                        pygame.mixer.Channel(6).play(orange6)

                if red_button.is_over(mpos) and played_sound == 'red1':
                    pygame.mixer.Channel(1).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level5, guessing_mode, played_sound)
                if red_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if red_button.is_over(mpos) and played_sound != 'red1':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level5, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level5, guessing_mode)

                if yellow_button.is_over(mpos) and played_sound == 'yellow2':
                    pygame.mixer.Channel(2).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level5, guessing_mode, played_sound)
                if yellow_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if yellow_button.is_over(mpos) and played_sound != 'yellow2':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level5, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level5, guessing_mode)

                if blue_button.is_over(mpos) and played_sound == 'blue3':
                    pygame.mixer.Channel(3).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level5, guessing_mode, played_sound)
                if blue_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if blue_button.is_over(mpos) and played_sound != 'blue3':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level5, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level5, guessing_mode)

                if white_button.is_over(mpos) and played_sound == 'white4':
                    pygame.mixer.Channel(4).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level5, guessing_mode, played_sound)
                if white_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if white_button.is_over(mpos) and played_sound != 'white4':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level5, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level5, guessing_mode)

                if green_button.is_over(mpos) and played_sound == 'green5':
                    pygame.mixer.Channel(5).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level5, guessing_mode, played_sound)
                if green_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if green_button.is_over(mpos) and played_sound != 'green5':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level5, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level5, guessing_mode)

                if orange_button.is_over(mpos) and played_sound == 'orange6':
                    pygame.mixer.Channel(6).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level5, guessing_mode, played_sound)
                if orange_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if orange_button.is_over(mpos) and played_sound != 'orange6':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level5, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level5, guessing_mode)

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        answered_counter(answered_num, display.get_width() // 2, 60)
        correct_counter(correct_num, display.get_width() // 2, 100)

        if answered_num == 30:
            stats(answered_num, correct_num)

        surf = pygame.transform.scale(display, screen.get_size())
        screen.blit(surf, (0, 0))
        pygame.display.update()


def level6(answered_num_save, correct_num_save, guessing_md):
    run = True

    answered_num = answered_num_save
    correct_num = correct_num_save

    played_sound = ''

    guessing_mode = guessing_md

    listen_button = engine.Button(display.get_width() // 2 - 200 // 2, 170, 200, 35, font, white, 'Play Sound')
    red_button = engine.Button(115, 240, 50, 50, font, white)
    yellow_button = engine.Button(195, 240, 50, 50, font, white)
    blue_button = engine.Button(275, 240, 50, 50, font, white)
    white_button = engine.Button(355, 240, 50, 50, font, white)
    green_button = engine.Button(435, 240, 50, 50, font, white)
    orange_button = engine.Button(115, 320, 50, 50, font, white)
    purple_button = engine.Button(195, 320, 50, 50, font, white)
    back_button = engine.Button(50, 50, 55, 40, font, white, '<--')

    while run:
        display.fill((0, 0, 0))

        w = screen.get_size()[0] / 600
        h = screen.get_size()[1] / 400

        mpos = list(pygame.mouse.get_pos())
        mpos[0] = mpos[0] / w
        mpos[1] = mpos[1] / h

        replay_sound_img = pygame.image.load('replay_sound.bmp')
        replay_sound_img = pygame.transform.scale(replay_sound_img, (40, 45))
        replay_sound_img_rect = replay_sound_img.get_rect()

        replay_sound_button = engine.Button(450, 160, replay_sound_img_rect.width, replay_sound_img_rect.height, font,
                                            white)

        if guessing_mode == 'active':
            display.blit(replay_sound_img, (450, 160))
            if replay_sound_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (replay_sound_button.x - i, replay_sound_button.y - i,
                                      replay_sound_button.width, replay_sound_button.height), 1)

        if back_button.is_over(mpos):
            back_button.draw(display, (50, 50, 50, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (back_button.x - i, back_button.y - i, back_button.width, back_button.height),
                                 1)
        else:
            back_button.draw(display, (50, 50, 50, 0))

        if listen_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (50, 50, 50, 0))

        if red_button.is_over(mpos):
            red_button.draw(display, (255, 0, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (red_button.x - i, red_button.y - i, red_button.width, red_button.height),
                                 1)
        else:
            red_button.draw(display, (255, 0, 0))

        if yellow_button.is_over(mpos):
            yellow_button.draw(display, (255, 255, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (yellow_button.x - i, yellow_button.y - i, yellow_button.width, yellow_button.height),
                                 1)
        else:
            yellow_button.draw(display, (255, 255, 0))

        if blue_button.is_over(mpos):
            blue_button.draw(display, (0, 0, 255))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (blue_button.x - i, blue_button.y - i, blue_button.width, blue_button.height),
                                 1)
        else:
            blue_button.draw(display, (0, 0, 255))

        if white_button.is_over(mpos):
            white_button.draw(display, (255, 255, 255))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (white_button.x - i, white_button.y - i, white_button.width, white_button.height),
                                 1)
        else:
            white_button.draw(display, (255, 255, 255))

        if green_button.is_over(mpos):
            green_button.draw(display, (0, 255, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (green_button.x - i, green_button.y - i, green_button.width, green_button.height),
                                 1)
        else:
            green_button.draw(display, (0, 255, 0))

        if orange_button.is_over(mpos):
            orange_button.draw(display, (255, 69, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (orange_button.x - i, orange_button.y - i, orange_button.width, orange_button.height),
                                 1)
        else:
            orange_button.draw(display, (255, 69, 0))

        if purple_button.is_over(mpos):
            purple_button.draw(display, (119, 0, 200))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (purple_button.x - i, purple_button.y - i, purple_button.width, purple_button.height),
                                 1)
        else:
            purple_button.draw(display, (119, 0, 200))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.is_over(mpos):
                    if not channel_check():
                        pygame.mixer.Channel(active_channel_check()).stop()
                        level_picker()
                    else:
                        level_picker()

                if listen_button.is_over(mpos):
                    randomsoundlvl1 = random.choice([red1, yellow2, blue3, white4, green5, orange6, purple7])
                    if randomsoundlvl1 == red1 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(1).play(red1)
                        played_sound = 'red1'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == yellow2 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(2).play(yellow2)
                        played_sound = 'yellow2'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == blue3 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(3).play(blue3)
                        played_sound = 'blue3'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == white4 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(4).play(white4)
                        played_sound = 'white4'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == green5 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(5).play(green5)
                        played_sound = 'green5'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == orange6 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(6).play(orange6)
                        played_sound = 'orange6'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == purple7 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(7).play(purple7)
                        played_sound = 'purple7'
                        guessing_mode = 'active'

                if replay_sound_button.is_over(mpos):
                    if played_sound == 'red1':
                        pygame.mixer.Channel(1).play(red1)
                    if played_sound == 'yellow2':
                        pygame.mixer.Channel(2).play(yellow2)
                    if played_sound == 'blue3':
                        pygame.mixer.Channel(3).play(blue3)
                    if played_sound == 'white4':
                        pygame.mixer.Channel(4).play(white4)
                    if played_sound == 'green5':
                        pygame.mixer.Channel(5).play(green5)
                    if played_sound == 'orange6':
                        pygame.mixer.Channel(6).play(orange6)
                    if played_sound == 'purple7':
                        pygame.mixer.Channel(7).play(purple7)

                if red_button.is_over(mpos) and played_sound == 'red1':
                    pygame.mixer.Channel(1).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level6, guessing_mode, played_sound)
                if red_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if red_button.is_over(mpos) and played_sound != 'red1':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)

                if yellow_button.is_over(mpos) and played_sound == 'yellow2':
                    pygame.mixer.Channel(2).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level6, guessing_mode, played_sound)
                if yellow_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if yellow_button.is_over(mpos) and played_sound != 'yellow2':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)

                if blue_button.is_over(mpos) and played_sound == 'blue3':
                    pygame.mixer.Channel(3).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level6, guessing_mode, played_sound)
                if blue_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if blue_button.is_over(mpos) and played_sound != 'blue3':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)

                if white_button.is_over(mpos) and played_sound == 'white4':
                    pygame.mixer.Channel(4).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level6, guessing_mode, played_sound)
                if white_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if white_button.is_over(mpos) and played_sound != 'white4':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)

                if green_button.is_over(mpos) and played_sound == 'green5':
                    pygame.mixer.Channel(5).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level6, guessing_mode, played_sound)
                if green_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if green_button.is_over(mpos) and played_sound != 'green5':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)

                if orange_button.is_over(mpos) and played_sound == 'orange6':
                    pygame.mixer.Channel(6).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level6, guessing_mode, played_sound)
                if orange_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if orange_button.is_over(mpos) and played_sound != 'orange6':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)

                if purple_button.is_over(mpos) and played_sound == 'purple7':
                    pygame.mixer.Channel(7).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level6, guessing_mode, played_sound)
                if purple_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if purple_button.is_over(mpos) and played_sound != 'purple7':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level6, guessing_mode)

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        answered_counter(answered_num, display.get_width() // 2, 60)
        correct_counter(correct_num, display.get_width() // 2, 100)

        if answered_num == 30:
            stats(answered_num, correct_num)

        surf = pygame.transform.scale(display, screen.get_size())
        screen.blit(surf, (0, 0))
        pygame.display.update()


def level7(answered_num_save, correct_num_save, guessing_md):
    run = True

    answered_num = answered_num_save
    correct_num = correct_num_save

    played_sound = ''

    guessing_mode = guessing_md

    listen_button = engine.Button(display.get_width() // 2 - 200 // 2, 170, 200, 35, font, white, 'Play Sound')
    red_button = engine.Button(115, 240, 50, 50, font, white)
    yellow_button = engine.Button(195, 240, 50, 50, font, white)
    blue_button = engine.Button(275, 240, 50, 50, font, white)
    white_button = engine.Button(355, 240, 50, 50, font, white)
    green_button = engine.Button(435, 240, 50, 50, font, white)
    orange_button = engine.Button(115, 320, 50, 50, font, white)
    purple_button = engine.Button(195, 320, 50, 50, font, white)
    pink_button = engine.Button(275, 320, 50, 50, font, white)
    back_button = engine.Button(50, 50, 55, 40, font, white, '<--')

    while run:
        display.fill((0, 0, 0))

        w = screen.get_size()[0] / 600
        h = screen.get_size()[1] / 400

        mpos = list(pygame.mouse.get_pos())
        mpos[0] = mpos[0] / w
        mpos[1] = mpos[1] / h

        replay_sound_img = pygame.image.load('replay_sound.bmp')
        replay_sound_img = pygame.transform.scale(replay_sound_img, (40, 45))
        replay_sound_img_rect = replay_sound_img.get_rect()

        replay_sound_button = engine.Button(450, 160, replay_sound_img_rect.width, replay_sound_img_rect.height, font,
                                            white)

        if guessing_mode == 'active':
            display.blit(replay_sound_img, (450, 160))
            if replay_sound_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (replay_sound_button.x - i, replay_sound_button.y - i,
                                      replay_sound_button.width, replay_sound_button.height), 1)

        if back_button.is_over(mpos):
            back_button.draw(display, (50, 50, 50, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (back_button.x - i, back_button.y - i, back_button.width, back_button.height),
                                 1)
        else:
            back_button.draw(display, (50, 50, 50, 0))

        if listen_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (50, 50, 50, 0))

        if red_button.is_over(mpos):
            red_button.draw(display, (255, 0, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (red_button.x - i, red_button.y - i, red_button.width, red_button.height),
                                 1)
        else:
            red_button.draw(display, (255, 0, 0))

        if yellow_button.is_over(mpos):
            yellow_button.draw(display, (255, 255, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (yellow_button.x - i, yellow_button.y - i, yellow_button.width, yellow_button.height),
                                 1)
        else:
            yellow_button.draw(display, (255, 255, 0))

        if blue_button.is_over(mpos):
            blue_button.draw(display, (0, 0, 255))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (blue_button.x - i, blue_button.y - i, blue_button.width, blue_button.height),
                                 1)
        else:
            blue_button.draw(display, (0, 0, 255))

        if white_button.is_over(mpos):
            white_button.draw(display, (255, 255, 255))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (white_button.x - i, white_button.y - i, white_button.width, white_button.height),
                                 1)
        else:
            white_button.draw(display, (255, 255, 255))

        if green_button.is_over(mpos):
            green_button.draw(display, (0, 255, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (green_button.x - i, green_button.y - i, green_button.width, green_button.height),
                                 1)
        else:
            green_button.draw(display, (0, 255, 0))

        if orange_button.is_over(mpos):
            orange_button.draw(display, (255, 69, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (orange_button.x - i, orange_button.y - i, orange_button.width, orange_button.height),
                                 1)
        else:
            orange_button.draw(display, (255, 69, 0))

        if purple_button.is_over(mpos):
            purple_button.draw(display, (119, 0, 200))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (purple_button.x - i, purple_button.y - i, purple_button.width, purple_button.height),
                                 1)
        else:
            purple_button.draw(display, (119, 0, 200))

        if pink_button.is_over(mpos):
            pink_button.draw(display, (255, 105, 180))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (pink_button.x - i, pink_button.y - i, pink_button.width, pink_button.height),
                                 1)
        else:
            pink_button.draw(display, (255, 105, 180))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.is_over(mpos):
                    if not channel_check():
                        pygame.mixer.Channel(active_channel_check()).stop()
                        level_picker()
                    else:
                        level_picker()

                if listen_button.is_over(mpos):
                    randomsoundlvl1 = random.choice([red1, yellow2, blue3, white4, green5, orange6, purple7, pink8])
                    if randomsoundlvl1 == red1 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(1).play(red1)
                        played_sound = 'red1'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == yellow2 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(2).play(yellow2)
                        played_sound = 'yellow2'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == blue3 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(3).play(blue3)
                        played_sound = 'blue3'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == white4 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(4).play(white4)
                        played_sound = 'white4'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == green5 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(5).play(green5)
                        played_sound = 'green5'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == orange6 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(6).play(orange6)
                        played_sound = 'orange6'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == purple7 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(7).play(purple7)
                        played_sound = 'purple7'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == pink8 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(8).play(pink8)
                        played_sound = 'pink8'
                        guessing_mode = 'active'

                if replay_sound_button.is_over(mpos):
                    if played_sound == 'red1':
                        pygame.mixer.Channel(1).play(red1)
                    if played_sound == 'yellow2':
                        pygame.mixer.Channel(2).play(yellow2)
                    if played_sound == 'blue3':
                        pygame.mixer.Channel(3).play(blue3)
                    if played_sound == 'white4':
                        pygame.mixer.Channel(4).play(white4)
                    if played_sound == 'green5':
                        pygame.mixer.Channel(5).play(green5)
                    if played_sound == 'orange6':
                        pygame.mixer.Channel(6).play(orange6)
                    if played_sound == 'purple7':
                        pygame.mixer.Channel(7).play(purple7)
                    if played_sound == 'pink8':
                        pygame.mixer.Channel(8).play(pink8)

                if red_button.is_over(mpos) and played_sound == 'red1':
                    pygame.mixer.Channel(1).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level7, guessing_mode, played_sound)
                if red_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if red_button.is_over(mpos) and played_sound != 'red1':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)

                if yellow_button.is_over(mpos) and played_sound == 'yellow2':
                    pygame.mixer.Channel(2).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level7, guessing_mode, played_sound)
                if yellow_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if yellow_button.is_over(mpos) and played_sound != 'yellow2':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)

                if blue_button.is_over(mpos) and played_sound == 'blue3':
                    pygame.mixer.Channel(3).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level7, guessing_mode, played_sound)
                if blue_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if blue_button.is_over(mpos) and played_sound != 'blue3':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)

                if white_button.is_over(mpos) and played_sound == 'white4':
                    pygame.mixer.Channel(4).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level7, guessing_mode, played_sound)
                if white_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if white_button.is_over(mpos) and played_sound != 'white4':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)

                if green_button.is_over(mpos) and played_sound == 'green5':
                    pygame.mixer.Channel(5).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level7, guessing_mode, played_sound)
                if green_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if green_button.is_over(mpos) and played_sound != 'green5':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)

                if orange_button.is_over(mpos) and played_sound == 'orange6':
                    pygame.mixer.Channel(6).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level7, guessing_mode, played_sound)
                if orange_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if orange_button.is_over(mpos) and played_sound != 'orange6':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)

                if purple_button.is_over(mpos) and played_sound == 'purple7':
                    pygame.mixer.Channel(7).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level7, guessing_mode, played_sound)
                if purple_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if purple_button.is_over(mpos) and played_sound != 'purple7':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)

                if pink_button.is_over(mpos) and played_sound == 'pink8':
                    pygame.mixer.Channel(8).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level7, guessing_mode, played_sound)
                if pink_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if pink_button.is_over(mpos) and played_sound != 'pink8':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level7, guessing_mode)

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        answered_counter(answered_num, display.get_width() // 2, 60)
        correct_counter(correct_num, display.get_width() // 2, 100)

        if answered_num == 30:
            stats(answered_num, correct_num)

        surf = pygame.transform.scale(display, screen.get_size())
        screen.blit(surf, (0, 0))
        pygame.display.update()


def level8(answered_num_save, correct_num_save, guessing_md):
    run = True

    answered_num = answered_num_save
    correct_num = correct_num_save

    played_sound = ''

    guessing_mode = guessing_md

    listen_button = engine.Button(display.get_width() // 2 - 200 // 2, 170, 200, 35, font, white, 'Play Sound')
    red_button = engine.Button(115, 240, 50, 50, font, white)
    yellow_button = engine.Button(195, 240, 50, 50, font, white)
    blue_button = engine.Button(275, 240, 50, 50, font, white)
    white_button = engine.Button(355, 240, 50, 50, font, white)
    green_button = engine.Button(435, 240, 50, 50, font, white)
    orange_button = engine.Button(115, 320, 50, 50, font, white)
    purple_button = engine.Button(195, 320, 50, 50, font, white)
    pink_button = engine.Button(275, 320, 50, 50, font, white)
    brown_button = engine.Button(355, 320, 50, 50, font, white)
    back_button = engine.Button(50, 50, 55, 40, font, white, '<--')

    while run:
        display.fill((0, 0, 0))

        w = screen.get_size()[0] / 600
        h = screen.get_size()[1] / 400

        mpos = list(pygame.mouse.get_pos())
        mpos[0] = mpos[0] / w
        mpos[1] = mpos[1] / h

        replay_sound_img = pygame.image.load('replay_sound.bmp')
        replay_sound_img = pygame.transform.scale(replay_sound_img, (40, 45))
        replay_sound_img_rect = replay_sound_img.get_rect()

        replay_sound_button = engine.Button(450, 160, replay_sound_img_rect.width, replay_sound_img_rect.height, font,
                                            white)

        if guessing_mode == 'active':
            display.blit(replay_sound_img, (450, 160))
            if replay_sound_button.is_over(mpos):
                for i in range(4):
                    pygame.draw.rect(display, (255, 255, 255),
                                     (replay_sound_button.x - i, replay_sound_button.y - i,
                                      replay_sound_button.width, replay_sound_button.height), 1)

        if back_button.is_over(mpos):
            back_button.draw(display, (50, 50, 50, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (back_button.x - i, back_button.y - i, back_button.width, back_button.height),
                                 1)
        else:
            back_button.draw(display, (50, 50, 50, 0))

        if listen_button.is_over(mpos):
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (255, 255, 255, 100))
        else:
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (listen_button.x - i, listen_button.y - i, listen_button.width, listen_button.height),
                                 1)
            listen_button.draw(display, (50, 50, 50, 0))

        if red_button.is_over(mpos):
            red_button.draw(display, (255, 0, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (red_button.x - i, red_button.y - i, red_button.width, red_button.height),
                                 1)
        else:
            red_button.draw(display, (255, 0, 0))

        if yellow_button.is_over(mpos):
            yellow_button.draw(display, (255, 255, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (yellow_button.x - i, yellow_button.y - i, yellow_button.width, yellow_button.height),
                                 1)
        else:
            yellow_button.draw(display, (255, 255, 0))

        if blue_button.is_over(mpos):
            blue_button.draw(display, (0, 0, 255))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (blue_button.x - i, blue_button.y - i, blue_button.width, blue_button.height),
                                 1)
        else:
            blue_button.draw(display, (0, 0, 255))

        if white_button.is_over(mpos):
            white_button.draw(display, (255, 255, 255))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (white_button.x - i, white_button.y - i, white_button.width, white_button.height),
                                 1)
        else:
            white_button.draw(display, (255, 255, 255))

        if green_button.is_over(mpos):
            green_button.draw(display, (0, 255, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (green_button.x - i, green_button.y - i, green_button.width, green_button.height),
                                 1)
        else:
            green_button.draw(display, (0, 255, 0))

        if orange_button.is_over(mpos):
            orange_button.draw(display, (255, 69, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (orange_button.x - i, orange_button.y - i, orange_button.width, orange_button.height),
                                 1)
        else:
            orange_button.draw(display, (255, 69, 0))

        if purple_button.is_over(mpos):
            purple_button.draw(display, (119, 0, 200))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (purple_button.x - i, purple_button.y - i, purple_button.width, purple_button.height),
                                 1)
        else:
            purple_button.draw(display, (119, 0, 200))

        if pink_button.is_over(mpos):
            pink_button.draw(display, (255, 105, 180))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (pink_button.x - i, pink_button.y - i, pink_button.width, pink_button.height),
                                 1)
        else:
            pink_button.draw(display, (255, 105, 180))

        if brown_button.is_over(mpos):
            brown_button.draw(display, (150, 75, 0))
            for i in range(4):
                pygame.draw.rect(display, (255, 255, 255),
                                 (brown_button.x - i, brown_button.y - i, brown_button.width, brown_button.height),
                                 1)
        else:
            brown_button.draw(display, (150, 75, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.is_over(mpos):
                    if not channel_check():
                        pygame.mixer.Channel(active_channel_check()).stop()
                        level_picker()
                    else:
                        level_picker()

                if listen_button.is_over(mpos):
                    randomsoundlvl1 = random.choice(
                        [red1, yellow2, blue3, white4, green5, orange6, purple7, pink8, brown9])
                    if randomsoundlvl1 == red1 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(1).play(red1)
                        played_sound = 'red1'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == yellow2 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(2).play(yellow2)
                        played_sound = 'yellow2'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == blue3 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(3).play(blue3)
                        played_sound = 'blue3'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == white4 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(4).play(white4)
                        played_sound = 'white4'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == green5 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(5).play(green5)
                        played_sound = 'green5'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == orange6 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(6).play(orange6)
                        played_sound = 'orange6'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == purple7 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(7).play(purple7)
                        played_sound = 'purple7'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == pink8 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(8).play(pink8)
                        played_sound = 'pink8'
                        guessing_mode = 'active'
                    if randomsoundlvl1 == brown9 and guessing_mode == 'inactive':
                        pygame.mixer.Channel(9).play(brown9)
                        played_sound = 'brown9'
                        guessing_mode = 'active'

                if replay_sound_button.is_over(mpos):
                    if played_sound == 'red1':
                        pygame.mixer.Channel(1).play(red1)
                    if played_sound == 'yellow2':
                        pygame.mixer.Channel(2).play(yellow2)
                    if played_sound == 'blue3':
                        pygame.mixer.Channel(3).play(blue3)
                    if played_sound == 'white4':
                        pygame.mixer.Channel(4).play(white4)
                    if played_sound == 'green5':
                        pygame.mixer.Channel(5).play(green5)
                    if played_sound == 'orange6':
                        pygame.mixer.Channel(6).play(orange6)
                    if played_sound == 'purple7':
                        pygame.mixer.Channel(7).play(purple7)
                    if played_sound == 'pink8':
                        pygame.mixer.Channel(8).play(pink8)
                    if played_sound == 'brown9':
                        pygame.mixer.Channel(9).play(brown9)

                if red_button.is_over(mpos) and played_sound == 'red1':
                    pygame.mixer.Channel(1).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level8, guessing_mode, played_sound)
                if red_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if red_button.is_over(mpos) and played_sound != 'red1':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)

                if yellow_button.is_over(mpos) and played_sound == 'yellow2':
                    pygame.mixer.Channel(2).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level8, guessing_mode, played_sound)
                if yellow_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if yellow_button.is_over(mpos) and played_sound != 'yellow2':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)

                if blue_button.is_over(mpos) and played_sound == 'blue3':
                    pygame.mixer.Channel(3).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level8, guessing_mode, played_sound)
                if blue_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if blue_button.is_over(mpos) and played_sound != 'blue3':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)

                if white_button.is_over(mpos) and played_sound == 'white4':
                    pygame.mixer.Channel(4).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level8, guessing_mode, played_sound)
                if white_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if white_button.is_over(mpos) and played_sound != 'white4':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)

                if green_button.is_over(mpos) and played_sound == 'green5':
                    pygame.mixer.Channel(5).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level8, guessing_mode, played_sound)
                if green_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if green_button.is_over(mpos) and played_sound != 'green5':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)

                if orange_button.is_over(mpos) and played_sound == 'orange6':
                    pygame.mixer.Channel(6).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level8, guessing_mode, played_sound)
                if orange_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if orange_button.is_over(mpos) and played_sound != 'orange6':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)

                if purple_button.is_over(mpos) and played_sound == 'purple7':
                    pygame.mixer.Channel(7).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level8, guessing_mode, played_sound)
                if purple_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if purple_button.is_over(mpos) and played_sound != 'purple7':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)

                if pink_button.is_over(mpos) and played_sound == 'pink8':
                    pygame.mixer.Channel(8).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level8, guessing_mode, played_sound)
                if pink_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if pink_button.is_over(mpos) and played_sound != 'pink8':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)

                if brown_button.is_over(mpos) and played_sound == 'brown9':
                    pygame.mixer.Channel(9).stop()
                    answered_num += 1
                    correct_num += 1
                    guessing_mode = 'inactive'
                    correct_answ_screen(answered_num, correct_num, level8, guessing_mode, played_sound)
                if brown_button.is_over(mpos) and channel_check() == True and played_sound == '':
                    continue
                if brown_button.is_over(mpos) and played_sound != 'brown9':
                    if channel_check():
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)
                    else:
                        pygame.mixer.Channel(active_channel_check()).stop()
                        answered_num += 1
                        guessing_mode = 'inactive'
                        incorrect_func(played_sound, answered_num, correct_num, level8, guessing_mode)

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        answered_counter(answered_num, display.get_width() // 2, 60)
        correct_counter(correct_num, display.get_width() // 2, 100)

        if answered_num == 30:
            stats(answered_num, correct_num)

        surf = pygame.transform.scale(display, screen.get_size())
        screen.blit(surf, (0, 0))
        pygame.display.update()


# runs the game
menu()
