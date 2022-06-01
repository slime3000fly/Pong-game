# pong game with pygame
# By: slime3000fly and angater1

import pygame, sys, time, random
from pygame import mixer

pygame.init()
pygame.display.init()
fps_controller = pygame.time.Clock()

screen = pygame.display.set_mode((1080, 720))

# score
score = 0
ai_score = 0

# reading highest score from txt
f = open('highest_score.txt', 'r')
highest_score = int(f.read())
f.close()

# color
black = (0, 0, 0)

initial_x_pong = 1060
initial_y_pong = 360
initial_x_pong_2 = 5
initial_y_pong_2 = 360

x_pong = 1060
y_pong = 360

x_pong_2 = 5
y_pong_2 = 360

velocity = 5
ball_velocity = 5

initial_x_ball = 530
initial_y_ball = 355

x_ball = 530
y_ball = 355
ball_direction = 'RIGHT'
change_to = ball_direction

wall_left = pygame.Rect(0, 0, 5, 740)
wall_right = pygame.Rect(1075, 0, 10, 740)
wall_up = pygame.Rect(0, 0, 1080, 10)
wall_down = pygame.Rect(0, 710, 1080, 10)
line = pygame.Rect(535, 0, 5, 740)

#sound
mixer.music.load('Simplicity(by damn so deep).mp3')
mixer.music.play(-1)
bang_sound = mixer.Sound('bang.wav')
score_sound = mixer.Sound('score.wav')
ai_score_sound = mixer.Sound('ai_score.wav')

# function declaration
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(
        'AI: ' + str(ai_score) + '  Player: ' + str(score) + '  Highest Score : ' + str(highest_score), True, color)
    score_rect = score_surface.get_rect()

    screen.blit(score_surface, score_rect)


def lose():
    # function which play after lose game
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.QUIT: sys.exit()
        # drawing writing 'you lose'
        font = pygame.font.Font('freesansbold.ttf', 52)
        text = font.render('YOU LOSE', True, red, white)
        # text surface object
        textRect = text.get_rect()
        # set the center of the rectangular object.
        textRect.center = (540, 360)
        screen.blit(text, textRect)
        pygame.display.update()


# color
red = pygame.Color(139, 0, 0)
blue = pygame.Color(51, 255, 255)
white = pygame.Color(255, 255, 255)
orange = (255, 100, 0)
yellow = (255, 50, 170)

done = False

while not done:
    for event in pygame.event.get():

        # key to control
        if event.type == pygame.KEYDOWN:
            pygame.key.set_repeat(10)
            if event.key == pygame.K_UP:
                if y_pong > 50:
                    y_pong -= velocity
            if event.key == pygame.K_DOWN:
                if y_pong < 670:
                    y_pong += velocity
            if event.key == pygame.K_w:
                if y_pong_2 > 50:
                    y_pong_2 -= velocity
            if event.key == pygame.K_s:
                if y_pong_2 < 670:
                    y_pong_2 += velocity
            if event.key == pygame.K_ESCAPE:
                done = True
        if event.type == pygame.QUIT: sys.exit()


    #drawing elements
    pygame.draw.rect(screen, black, wall_right)
    pygame.draw.rect(screen, black, wall_left)
    pygame.draw.rect(screen, white, line)
    pygame.draw.rect(screen, red, wall_up)
    pygame.draw.rect(screen, red, wall_down)
    ball = pygame.draw.rect(screen, red, pygame.Rect(x_ball, y_ball, 10, 10))
    ai_rect = pygame.Rect(x_pong_2, y_pong_2, 15, 80)
    #ai_rect = pygame.Rect(x_pong_2, y_ball, 15, 80)
    #ai_rect.center = (15, y_ball)
    ai_rect.center = (15, y_pong_2)
    player_rect = pygame.Rect(x_pong, y_pong, 15, 80)
    player_rect.center = (x_pong, y_pong)
    pygame.draw.rect(screen, white, player_rect)
    pygame.draw.rect(screen, white, ai_rect)

    # drawing score
    show_score(1, white, 'times new roman', 20)
    pygame.display.flip()
    screen.fill(black)
    # collisions
    i = random.randint(0, 100)
    j = random.randint(0, 120)

    if pygame.Rect.colliderect(ball, player_rect):
        bang_sound.play()
        if ball_direction == 'RIGHT':
            if i < 50:
                ball_direction = 'UP_LEFT'
            if i > 50:
                ball_direction = 'DOWN_LEFT'
        if ball_direction == 'UP_RIGHT':
            ball_direction = 'UP_LEFT'
        if ball_direction == 'DOWN_RIGHT':
            ball_direction = 'DOWN_LEFT'

    if pygame.Rect.colliderect(ball, ai_rect):
        bang_sound.play()
        if ball_direction == 'LEFT':
            if i < 50:
                ball_direction = 'UP_RIGHT'
            if i >= 50:
                ball_direction = 'DOWN_RIGHT'
        if ball_direction == 'UP_LEFT':
            ball_direction = 'UP_RIGHT'
        if ball_direction == 'DOWN_LEFT':
            ball_direction = 'DOWN_RIGHT'

    if pygame.Rect.colliderect(ball, wall_up):
        bang_sound.play()
        if ball_direction == 'UP_RIGHT':
            ball_direction = 'DOWN_RIGHT'
        if ball_direction == 'UP_LEFT':
            ball_direction = 'DOWN_LEFT'

    if pygame.Rect.colliderect(ball, wall_down):
        bang_sound.play()
        if ball_direction == 'DOWN_LEFT':
            ball_direction = 'UP_LEFT'
        if ball_direction == 'DOWN_RIGHT':
            ball_direction = 'UP_RIGHT'

    if pygame.Rect.colliderect(ball, wall_right):
        ai_score_sound.play()
        ai_score += 1
        x_ball = initial_x_ball
        y_ball = initial_y_ball
        x_pong = initial_x_pong
        y_pong = initial_y_pong
        x_pong_2 = initial_x_pong_2
        y_pong_2 = initial_y_pong_2
        if i <= 20:
            ball_direction = 'RIGHT'
        if 20 < i <= 40:
            ball_direction = 'LEFT'
        if 40 < i <= 60:
            ball_direction = 'UP_RIGHT'
        if 60 < i <= 80:
            ball_direction = 'UP_LEFT'
        if 80 < i <= 100:
            ball_direction = 'DOWN_RIGHT'
        if 100 < i <= 120:
            ball_direction = 'DOWN_LEFT'
    if pygame.Rect.colliderect(ball, wall_left):
        score_sound.play()
        score += 1
        x_ball = initial_x_ball
        y_ball = initial_y_ball
        x_pong = initial_x_pong
        y_pong = initial_y_pong
        x_pong_2 = initial_x_pong_2
        y_pong_2 = initial_y_pong_2
        if i <= 20:
            ball_direction = 'RIGHT'
        if 20 < i <= 40:
            ball_direction = 'LEFT'
        if 40 < i <= 60:
            ball_direction = 'UP_RIGHT'
        if 60 < i <= 80:
            ball_direction = 'UP_LEFT'
        if 80 < i <= 100:
            ball_direction = 'DOWN_RIGHT'
        if 100 < i <= 120:
            ball_direction = 'DOWN_LEFT'
    # Moving the ball
    if ball_direction == 'UP':
        y_ball -= ball_velocity
    if ball_direction == 'DOWN':
        y_ball += ball_velocity
    if ball_direction == 'LEFT':
        x_ball -= ball_velocity
    if ball_direction == 'RIGHT':
        x_ball += ball_velocity

    if ball_direction == 'UP_RIGHT':
        x_ball += ball_velocity
        y_ball -= ball_velocity
    if ball_direction == 'UP_LEFT':
        x_ball -= ball_velocity
        y_ball -= ball_velocity
    if ball_direction == 'DOWN_RIGHT':
        x_ball += ball_velocity
        y_ball += ball_velocity
    if ball_direction == 'DOWN_LEFT':
        x_ball -= ball_velocity
        y_ball += ball_velocity

    if ai_score > score + 10:
        lose()

    # saving highest score to highest_score.txt
    f = open('highest_score.txt', 'w')
    f.write(str(highest_score))
    f.close()

    # FPS !!!!!
    fps_controller.tick(60)
