def level_six():
    global running
    global move_left
    global move_right
    global move_down
    global move_up

    # if current_level == 6:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            elif event.key == pygame.K_d:
                move_right = True
            elif event.key == pygame.K_s:
                move_down = True
            elif event.key == pygame.K_w:
                move_up = True
            if event.type == pygame.K_p:
                hero.switch_pause()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            elif event.key == pygame.K_d:
                move_right = False
            elif event.key == pygame.K_s:
                move_down = False
            elif event.key == pygame.K_w:
                move_up = False
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")

def level_eleven():
    global  tile_images
    tile_images = {
        'wall': pygame.transform.scale(load_image('break_black.jpg'), (18, 10)),
        'empty': pygame.transform.scale(load_image('download.png'), (18, 10))
    }

def one_third_fifth_seventh_levels():
    global running, move_up, move_left, move_down, move_right, current_level
    FPS=0
    if current_level == 1 or current_level == 5:
        FPS = 20
    elif current_level == 3:
        FPS = 5
    elif current_level == 7:
        FPS = 20
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
                if event.type == pygame.K_p:
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
        if current_level == 1 or current_level == 3 or current_level == 5:
            if move_right:
                move(hero, "right")
            if move_left:
                move(hero, "left")
            if move_up:
                move(hero, "up")
            if move_down:
                move(hero, "down")
        elif current_level == 7:
            if move_right:
                move(hero, "down")
            if move_left:
                move(hero, "up")
            if move_up:
                move(hero, "right")
            if move_down:
                move(hero, "left")
        for finish in finishes:
            if hero.rect.colliderect(finish.rect):
                hero_group.remove(hero)
                current_level += 1
                map_change(0)
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


def second_level():
    global running, move_up, move_left, move_down, move_right, current_level
    FPS = 20
    level_map = load_level("map.map")
    hero, max_x, max_y, finishes, rutile = generate_level(level_map)
    r = False

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
                if event.type == pygame.K_p:
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
        if rutile and hero.rect.colliderect(rutile.rect):
            r = True
            map_change(1)
            x, y = hero.pos
            level_map = load_level("map.map")
            hero_group.remove(hero)
            hero, max_x, max_y, finishes, rutile = generate_level(level_map, x, y)
        for finish in finishes:
            if hero.rect.colliderect(finish.rect) and r:
                current_level += 1
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()

def fourth_level():
    global running, move_up, move_left, move_down, move_right, current_level
    level_map = load_level("map.map")
    hero, max_x, max_y, finishes, rutile = generate_level(level_map)
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
                if event.type == pygame.K_p:
                    hero.switch_pause()
                # if event.type==pygame.K_s:
                #     with open(f"data/save.dat", "wb")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    for i in range(10):
                        move(hero, 'left')
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    for i in range(10):
                        move(hero, 'left')
                    move_right = False
                elif event.key == pygame.K_DOWN:
                    for i in range(10):
                        move(hero, 'left')
                    move_down = False
                elif event.key == pygame.K_UP:
                    for i in range(10):
                        move(hero, 'left')
                    move_up = False
        if move_right:
            move(hero, "right")
        if move_left:
            move(hero, "left")
        if move_up:
            move(hero, "up")
        if move_down:
            move(hero, "down")
        for finish in finishes:
            if hero.rect.colliderect(finish.rect):
                hero_group.remove(hero)
                current_level += 1
                return
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()
