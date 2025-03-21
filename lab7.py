#clock
import pygame 
import time
import math
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Mickey clock")
clock_img = pygame.image.load("clock.png")
minute_hand = pygame.image.load("rightarm.png")
second_hand = pygame.image.load("leftarm.png")
clock_img = pygame.transform.scale(clock_img, (WIDTH, HEIGHT))

done = False
while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    minute_angle = minute * 6    + (second / 60) * 6   
    second_angle = second * 6  
    screen.blit(clock_img, (0,0))
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(minute_hand, (800, 600)), -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(second_hand, (40.95, 682.5)), -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    pygame.display.flip()
    clock.tick(60) 
pygame.quit()
#music
import pygame
import os
pygame.init()
current_folder = os.path.dirname(__file__)
playlist = [os.path.join(current_folder, f) for f in os.listdir(current_folder) if f.endswith(".mp3")]
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()
background = pygame.image.load(os.path.join(current_folder, "background.png"))
playb = pygame.image.load(os.path.join(current_folder, "play.png"))
pausb = pygame.image.load(os.path.join(current_folder, "pause.png"))
nextb = pygame.image.load(os.path.join(current_folder, "next.png"))
prevb = pygame.image.load(os.path.join(current_folder, "back.png"))
font = pygame.font.SysFont(None, 40)
index = 0
aplay = False
pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play()
aplay = True
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: 
                if aplay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                aplay = not aplay

            if event.key == pygame.K_RIGHT:  
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                aplay = True

            if event.key == pygame.K_LEFT:  
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                aplay = True
    song_name = os.path.basename(playlist[index])
    text_surface = font.render(song_name, True, (255, 255, 255)) 
    text_rect = text_surface.get_rect(center=(400, 700))  
    screen.blit(background, (0, 0))
    screen.blit(text_surface, text_rect)
    playb = pygame.transform.scale(playb, (70, 70))
    pausb = pygame.transform.scale(pausb, (70, 70))
    nextb = pygame.transform.scale(nextb, (70, 70))
    prevb = pygame.transform.scale(prevb, (75, 75))
    if aplay:
        screen.blit(pausb, (370, 590))  
    else:
        screen.blit(playb, (370, 590)) 
    screen.blit(nextb, (460, 587))  
    screen.blit(prevb, (273, 585))  
    pygame.display.update()
    clock.tick(24)
  #ball
import pygame
pygame.init()
window_size = (800, 600) 
screen = pygame.display.set_mode(window_size) 
pygame.display.set_caption("Draw circle")
ball_color = pygame.Color('red')
bg_color = pygame.Color('white')
ball_pos = [400, 300] 
ball_radius = 25 
speed = 20 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_UP]: 
        ball_pos[1] = max(ball_pos[1] - speed, ball_radius)
    if keys[pygame.K_DOWN]:
        ball_pos[1] = min(ball_pos[1] + speed, window_size[1] - ball_radius)
    if keys[pygame.K_LEFT]:
        ball_pos[0] = max(ball_pos[0] - speed, ball_radius)
    if keys[pygame.K_RIGHT]:
        ball_pos[0] = min(ball_pos[0] + speed, window_size[0] - ball_radius)

    screen.fill(bg_color)
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    pygame.display.flip()
    pygame.time.Clock().tick(24)
