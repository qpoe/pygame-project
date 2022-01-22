def first_level():
    global running, move_up, move_left, move_down, move_right
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
        screen.fill(pygame.Color("black"))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()
