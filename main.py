import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def load_sound(name):
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)

    except pygame.error as message:
        print('Cannot load sound:', name)
        raise SystemExit(message)

    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл со звуком '{fullname}' не найден")
        sys.exit()
    sound = pygame.mixer.Sound(fullname)
    return sound


def load_music(name):
    fullname = os.path.join('data', name)
    try:
        music = pygame.mixer.music.load(fullname)

    except pygame.error as message:
        print('Cannot load sound:', name)
        raise SystemExit(message)

    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл со звуком '{fullname}' не найден")
        sys.exit()
    music = pygame.mixer.music.load(fullname)
    return music


FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Главная страница",
                  "Настройки",
                  "Продолжить"]
    size = WIDTH, HEIGHT = 700, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 125
    intro_rect_x = [65, 100, 90]
    for line in range(len(intro_text)):
        string_rendered = font.render(intro_text[line], 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = intro_rect_x[line]
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        mouse_click = load_sound("mouse_click.mp3")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    210 > event.pos[0] > 100 and 185 > event.pos[1] > 165:
                return  # натройки
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    215 > event.pos[0] > 90 and 215 > event.pos[1] > 195:
                return  # продолжить
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    410 > event.pos[0] > 390 and 205 > event.pos[1] > 175:
                return  # лампа
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click.play()
        pygame.display.flip()
        clock.tick(FPS)


pygame.init()
pygame.mixer.music.load("data/sonata.mp3")
pygame.mixer.music.play(loops=-1, start=6.5)
start_screen()
