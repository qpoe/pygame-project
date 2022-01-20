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