import os
import sys

import pygame
import pickle

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
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
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


def terminate():
    pygame.quit()
    sys.exit()


pygame.init()
FPS = 50
size = WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode(size)
sprite_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()

tile_images = {
    'wall': pygame.transform.scale(load_image('break.jpg'), (35, 20)),
    'empty': pygame.transform.scale(load_image('download.png'), (35, 20))
}
player_image = pygame.transform.scale(load_image('gg.jpg', -1), (35, 20))

tile_width, tile_height = 35, 20
current_level=1


class Sprite(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.rect = None

    def get_event(self, event):
        pass


class Player(Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(hero_group)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 5, tile_height * pos_y + 5)
        self.pos = (pos_x, pos_y)
        self.is_paused=False

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(tile_width * self.pos[0] + 5,
                                               tile_height * self.pos[1] + 1)
        pygame.time.set_timer(30, 500)
    def switch_pause(self):
        self.is_paused=not self.is_paused



class Tile(Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(sprite_group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.abs_pos = (self.rect.x, self.rect.y)


def start_screen():
    intro_text = ["Главная страница",
                  "Настройки",
                  "Продолжить",
                  "S - сохранить, P - пауза"]

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 125
    intro_rect_x = [65, 100, 90, 60]
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


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, ' ')), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == ' ':
                Tile('empty', x, y)
            elif level[y][x] == 'W':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
                level[y][x] = " "
    return new_player, x, y


def move(hero, movement):
    x, y = hero.pos
    if movement == "up":
        if y > 0 and level_map[y - 1][x] == " ":
            hero.move(x, y - 1)
    elif movement == "down":
        if y < max_y - 1 and level_map[y + 1][x] == " ":
            hero.move(x, y + 1)
    elif movement == "left":
        if x > 0 and level_map[y][x - 1] == " ":
            hero.move(x - 1, y)
    elif movement == "right":
        if x < max_x - 1 and level_map[y][x + 1] == " ":
            hero.move(x + 1, y)


level_map = load_level("map.map")
hero, max_x, max_y = generate_level(level_map)
pygame.mixer.music.load("data/sonata.mp3")
pygame.mixer.music.play(loops=-1, start=6.5)
start_screen()
running = True
clock = pygame.time.Clock()
move_right = False
move_left = False
move_down = False
move_up = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_DOWN:
                move_down = True
            elif event.key == pygame.K_UP:
                move_up = True
            if event.type==pygame.K_p:
                hero.switch_pause()
            # if event.type==pygame.K_s:
            #     with open(f"data/save.dat", "wb")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_DOWN:
                move_down = False
            elif event.key == pygame.K_UP:
                move_up = False
    if move_right:
        move(hero, "right")
    if move_left:
        move(hero, "left")
    if move_up:
        move(hero, "up")
    if move_down:
        move(hero, "down")
    screen.fill(pygame.Color("black"))
    sprite_group.draw(screen)
    hero_group.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()