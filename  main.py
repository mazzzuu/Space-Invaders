import pygame,sys

def animate_player():
    player.x += player_speed

    if player.right >= screen_widht:
        player.right = screen_widht

    if player.left <= 0:
        player.left = 0

def killing():
    if bullet.center == enemy.center:
        print("killato")

def is_empty(sequence):
    if not sequence:
        return True
    else:
        return False
    
pygame.init()

screen_widht = 1280
screen_height = 800

screen = pygame.display.set_mode((screen_widht,screen_height))
pygame.display.set_caption("Screen")

clock = pygame.time.Clock()

bullet = pygame.Rect((0,0,30,30))
bullet.center = (screen_widht/2,5*screen_height/6)
bullet_speed = -6
bullet_moving = False

enemies = []

distribuzion = 20
for i in range(1):
    enemy  = pygame.Rect(distribuzion,1*screen_height/6,40,40)
    enemies.append(enemy)
    distribuzion += 300

bullets = []


player = pygame.Rect(0,0,40,40)
player.center = (screen_widht/2,5*screen_height/6)
player_speed = 0


score_font = pygame.font.Font(None, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_speed = 6
            if event.key == pygame.K_LEFT:
                player_speed = -6
            if event.key == pygame.K_SPACE:
                bullet.centerx = player.centerx
                bullet_moving= True
                bullets.append(bullets)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_speed = 0
            if event.key == pygame.K_LEFT:
                player_speed = 0
            if event.key == pygame.K_SPACE:
                None

    animate_player()



    screen.fill('black')

    pygame.draw.rect(screen,'white',player)

    for enemy in enemies:
        pygame.draw.rect(screen, 'red', enemy)

    # for bullet in bullets:
    #     pygame.draw.ellipse(screen,'white',bullet)


    pygame.draw.ellipse(screen,'white',bullet)

    pygame.draw.rect(screen,'red', enemy)

    killing()

    enemy_count = score_font.render("hai ucciso un nemico",True,"white")

    if bullet_moving:
        bullet.y += bullet_speed
        # Disattiva il movimento se esce dallo schermo
        if bullet.bottom < 0:
            bullet_moving = False
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullet_moving =False
                enemies.remove(enemy)

    if is_empty(enemies):
        screen.blit(enemy_count,(screen_widht/4,20))


    if bullet_moving:
        pygame.draw.ellipse(screen,'white',bullet)

    pygame.display.update()
    clock.tick(60)


            
    # screen.blit(cpu_score_surface,(screen_widht/4,20))
    # screen.blit(player_score_surface,(3*screen_widht/4,20))