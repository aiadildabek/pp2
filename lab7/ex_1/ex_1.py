# Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. 
# Use Mickey's right hand as minutes arrow and left - as seconds. 

# For moving Mickey's hands you can use: pygame.transform.rotate more explanation: https://stackoverflow.com/a/54714144
import pygame
import sys
import datetime


# Initialization of programm
pygame.init()


# My clock
clock = pygame.time.Clock()

# The display that we will see
W, H = 850, 850
display = pygame.display.set_mode([W, H])
pygame.display.set_caption("Aiashka sdelala chasi ura")

# My images are now in programm as sprites + zero pos for hands
clock_img = pygame.image.load("lab7//ex_1//sprites//clock.png") 
clock_rect = clock_img.get_rect(center=display.get_rect().center)

minutes_img = pygame.image.load("lab7//ex_1//sprites//minutes.png")
minutes_img = pygame.transform.rotate(minutes_img, -55.5)
minutes_rect = minutes_img.get_rect(center = display.get_rect().center)

seconds_img = pygame.image.load("lab7//ex_1//sprites//seconds.png")
seconds_img = pygame.transform.rotate(seconds_img, -4)
seconds_rect = seconds_img.get_rect(center = display.get_rect().center)


# Main code
run = True
while run:
    # Like just quit from programm
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if not run:
        break

    # Draw first the clock
    display.blit(clock_img, clock_rect)


    # Get Time
    cur_time = datetime.datetime.now()
    cur_seconds = cur_time.second
    cur_minutes = cur_time.minute

    # Computating the angle
    seconds_ang = 6 * cur_seconds
    minutes_ang = 0.1 * (cur_minutes * 60 + cur_seconds)

    # givinng the right angle to sprites
    seconds_img1 = pygame.transform.rotate(seconds_img, -seconds_ang)
    seconds_rect = seconds_img1.get_rect(center = clock_rect.center)

    minutes_img1 = pygame.transform.rotate(minutes_img, -minutes_ang)
    minutes_rect = minutes_img1.get_rect(center = clock_rect.center)

    # Display hands after the motion
    display.blit(seconds_img1, seconds_rect)
    display.blit(minutes_img1, minutes_rect)

    # Control the frame rate + Update the display
    pygame.display.flip()
    clock.tick(1)

pygame.quit()
sys.exit()