import pygame,sys,random

def animate_player():
    player.x += player_speed

    if player.right >= screen_widht:
        player.right = screen_widht

    if player.left <= 0:
        player.left = 0

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

bullet_speed = -6
bullets = []

enemies = []


for i in range(5):
    enemy  = pygame.Rect(random.randint(0,screen_widht),1*screen_height/6,40,40)
    enemies.append(enemy)

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
                # CORREZIONE: usa = invece di ==
                new_bullet = pygame.Rect(0,0,30,30)
                new_bullet.center = (player.centerx, player.top)
                bullets.append(new_bullet)

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

    # CORREZIONE: gestisci il movimento e le collisioni per tutti i proiettili
    for bullet in bullets[:]:  # Usa una copia della lista per iterare
        bullet.y += bullet_speed
        
        # Rimuovi i proiettili usciti dallo schermo
        if bullet.bottom < 0:
            bullets.remove(bullet)
            continue
        
        # Controlla collisione con i nemici
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                if bullet in bullets:
                    bullets.remove(bullet)
                break

    # Disegna tutti i proiettili
    for bullet in bullets:
        pygame.draw.ellipse(screen, 'white', bullet)

    # Disegna tutti i nemici
    for enemy in enemies:
        pygame.draw.rect(screen, 'red', enemy)

    # Mostra messaggio di vittoria
    if is_empty(enemies):
        enemy_count = score_font.render("hai vinto", True, "white")
        screen.blit(enemy_count, (4*screen_widht/10, 20))

    pygame.display.update()
    clock.tick(60)