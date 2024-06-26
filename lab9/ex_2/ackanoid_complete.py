# 1) Instead of developing Snake upgrade Arkanoid;
# 2) Create unbreakable bricks;
# 3) Increase the speed of a ball with time;
# 4) Shrink the paddle with time;
# 5) Create bonus bricks, that give some perks when you destroy them.

import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)
time = 0 # to make ball faster

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


# Some parameters for options
volume = 1.0
is_Paused = False
only_once = True

# two buttons
vert1 = (635, 385)
vert2 = (635, 415)
vert3 = (645, 400)
triangle_vertices = (vert1, vert2, vert3)

overt1 = (570, 385)
overt2 = (570, 415)
overt3 = (560, 400)
otriangle_vertices = (overt1, overt2, overt3)

#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('lab9/ex_2/audio/catch.mp3')


def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# some perks
perk_list = []


#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 
un_block_list = [random.randrange(0, 10) for _ in range(len(block_list))] # if 0 then unbreakable

print(block_list)
#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Volume text
volfont = pygame.font.SysFont('comicsansms', 40)
voltext = volfont.render(f'{volume}', True, (255, 255, 255))
voltextRect = voltext.get_rect()
voltextRect.center = (W // 2, H // 2)

# This is a sound text
voltext2 = volfont.render('Sound:', True, (255, 255, 255))
voltextRect2 = voltext2.get_rect()
voltextRect2.center = (W // 2 - 110, H // 2)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_Paused = not is_Paused # change to the reverse
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_Paused:
                mx, my = pygame.mouse.get_pos()
                dv = 0.0

                if mx >= 635 and mx <= 645 and my >= 385 and my <= 415:
                    dv = 0.1
                
                if mx >= 560 and mx <= 570 and my >= 385 and my <= 415:
                   dv = -0.1

                volume = round(max(0.0, min(1.0, volume + dv)), 1)
                voltext = volfont.render(f'{volume}', True, (255, 255, 255))
                collision_sound.set_volume(volume)
                only_once = False
                


        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: # left click
                only_once = True

    screen.fill(bg)
    
    # print(pygame.mouse.get_pos())
    # Paused
    if is_Paused:
        screen.blit(voltext, voltextRect)
        screen.blit(voltext2, voltextRect2)

        pygame.draw.polygon(screen, (255, 255, 255), triangle_vertices)
        pygame.draw.polygon(screen, (255, 255, 255), otriangle_vertices)


        pygame.display.flip()
        clock.tick(FPS)
        continue
    
    # print(next(enumerate(block_list)))
    
    [pygame.draw.rect(screen, color_list[color], block) 
     for color, block in enumerate (block_list)] #drawing blocks
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    # print(next(enumerate (block_list)))

    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    #Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    #Collision blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list[hitIndex]
        hitColor = color_list[hitIndex]
        if un_block_list[hitIndex] != 0:
            block_list.pop(hitIndex)
            color_list.pop(hitIndex)
            un_block_list.pop(hitIndex)

            # if 0 then perk will appear
            if random.randrange(0, 2) == 0:
                perk_list.append(pygame.Rect(hitRect.centerx, hitRect.centery, 60, 60))
            
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()
    
    # make them move
    for rect in perk_list:
        rect.y += 10
    
    [pygame.draw.rect(screen, (255, 255, 255), rect) for rect in perk_list]

    # if they collide then perk will appear
    perkIndexes = paddle.collidelistall(perk_list)
    # print(perkIndex)
    for index in perkIndexes:
        perk_list.pop(index)
        
        # The only ability is to break a random breakable block
        for i in range(len(block_list)):
            if un_block_list[i] != 0:
                block_list.pop(i)
                color_list.pop(i)
                un_block_list.pop(i)
                break

        
    #Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list) - len([i for i in un_block_list if i == 0]):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
    # print(pygame.K_LEFT)
    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    # every 1000 frame +1 speed level and shrinking the paddle
    if time > 500:
        time -= 500
        ballSpeed += 1
        paddleW = max(100, paddleW - 20)
        paddle = pygame.Rect(paddle.x, paddle.y, paddleW, paddleH)


    pygame.display.flip()
    clock.tick(FPS)
    time += 1