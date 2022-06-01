# pong game with pygame
# By: slime3000fly and angater1

import pygame, sys, time, random

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


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(
        'AI: ' + str(ai_score) + '  Player: ' + str(score) + '  Highest Score : ' + str(highest_score), True, color)
    score_rect = score_surface.get_rect()

    screen.blit(score_surface, score_rect)


# variable declartaion
x = [200]
y = [200]
checker = [0]
number_of_apple = 0
size = 1  # variable which define how long is snake
t = 0.5
z1 = 0
z2 = 0
move = 20  # variable which define how big is single step for snake
x_apple = 0
y_apple = 0

x_pong = 1060
y_pong = 320
velocity = 15

x_ball = 530
y_ball = 355

wall_left = pygame.Rect(0, 0, 10, 740)
wall_right = pygame.Rect(1070, 0, 10, 740)

# function declaration
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
    # print(size)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    # adding new element to list x and y
    for i in range(0, size):
        if (i >= len(x)):
            x.append(i)
            y.append(i)

    # key to control
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if y_pong > 0: y_pong -= velocity
        if event.key == pygame.K_DOWN:
            if y_pong < 640: y_pong += velocity
        if event.key == pygame.K_LEFT:
            x_ball -= velocity
        if event.key == pygame.K_RIGHT:
            x_ball += velocity
        if event.key == pygame.K_ESCAPE:
            done = True

    pygame.draw.rect(screen, black, wall_right)
    pygame.draw.rect(screen, black, wall_left)
    pygame.draw.rect(screen, white, pygame.Rect(5, 320, 15, 80))
    pygame.draw.rect(screen, white, pygame.Rect(x_pong, y_pong, 15, 80))


    # drawing score
    show_score(1, white, 'times new roman', 20)
    pygame.display.flip()
    screen.fill(black)

    # draw ball
    ball = pygame.draw.rect(screen, red, pygame.Rect(x_ball, y_ball, 10, 10))
    # collisions
    collide = pygame.Rect.colliderect(ball, wall_left)

    if pygame.Rect.colliderect(ball, wall_right):
        ai_score += 1
    if pygame.Rect.colliderect(ball, wall_left):
        score += 1
        if score > highest_score:
            highest_score = score

    # saving highest score to highest_score.txt
    f = open('highest_score.txt', 'w')
    f.write(str(highest_score))
    f.close()

    # FPS !!!!!
    fps_controller.tick(60)
