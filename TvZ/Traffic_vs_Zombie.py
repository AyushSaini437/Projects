import pygame
from pygame.locals import *
import sys

pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Screen
screen = pygame.display.set_mode((1300, 650))
pygame.display.set_caption("Traffic vs Zombie")

# Lose sound
collision_sound = pygame.mixer.Sound("Sound/Mario Death - Sound Effect (HD).mp3")
collision_sound.set_volume(0.5)

collision_sound_played = False

# Lose screen
def game_over_screen():
    font = pygame.font.Font("Font/BloodLust.ttf", 100)
    screen.fill("Blue")
    text = font.render("GAME OVER", 1, (136, 8, 8))
    screen.blit(text, (450,275))
    pygame.display.flip()
    pygame.time.wait(3000)


# Background
background = pygame.image.load("Background/Backgnd.png")

# Player implementation
zombie = pygame.image.load("Player/zombie.png").convert_alpha()
x = 5
y = 25
pygame.key.set_repeat(1, 100)

# Vehicles on road
ambulance = pygame.image.load("Road_1/ambulance.png").convert_alpha()
buggy = pygame.image.load("Road_1/buggy.png").convert_alpha()
truck = pygame.image.load("Road_1/truckdelivery.png").convert_alpha()

school_bus = pygame.image.load("Road_2/bus_school.png").convert_alpha()
convertible = pygame.image.load("Road_2/convertible.png").convert_alpha()

transport = pygame.image.load("Road_3/transport.png").convert_alpha()
sedan = pygame.image.load("Road_3/sedan.png").convert_alpha()
police = pygame.image.load("Road_3/police.png").convert_alpha()

ambulance_x_pos = 100
buggy_x_pos = 600
truck_x_pos = 1000

school_bus_x_pos = 325
convertible_x_pos = 975

transport_x_pos = 100
sedan_x_pos = 600
police_x_pos = 1000

collision_status = {
    'ambulance': False,
    'buggy': False,
    'truck': False,
    'school_bus': False,
    'convertible': False,
    'police': False,
}


running = True
a, b = 0, 0
c = 7

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if event.key == pygame.K_ESCAPE:
                running = False
            pygame.quit()
            sys.exit()

    pygame.display.update()
    screen.blit(background, (a, b))


    # Player motion
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= c
            if event.key == pygame.K_s:
                y += c
            if event.key == pygame.K_a:
                x -= c
            if event.key == pygame.K_d:
                x += c

    zombie_rect = zombie.get_rect(midtop=(x, y))
    screen.blit(zombie, zombie_rect)

    # Motion of vehicles on road
    ambulance_x_pos += 4
    if ambulance_x_pos >= 1320:
        ambulance_x_pos = 0
    screen.blit(ambulance, (ambulance_x_pos, 125))

    buggy_x_pos += 4
    if buggy_x_pos >= 1320:
        buggy_x_pos = 0
    screen.blit(buggy, (buggy_x_pos, 125))

    truck_x_pos += 4
    if truck_x_pos >= 1320:
        truck_x_pos = 0
    screen.blit(truck, (truck_x_pos, 125))

    school_bus_x_pos -= 7
    if school_bus_x_pos <= -10:
        school_bus_x_pos = 1300
    screen.blit(school_bus, (school_bus_x_pos, 260))

    convertible_x_pos -= 7
    if convertible_x_pos <= -10:
        convertible_x_pos = 1300
    screen.blit(convertible, (convertible_x_pos, 260))

    police_x_pos += 10
    if police_x_pos > 1320:
        police_x_pos = 0
    screen.blit(police, (police_x_pos, 395))

    vehicle_rectangles = {
        'ambulance': ambulance.get_rect(topleft=(ambulance_x_pos, 125)),
        'buggy': buggy.get_rect(topleft=(buggy_x_pos, 125)),
        'truck': truck.get_rect(topleft=(truck_x_pos, 125)),
        'school_bus': school_bus.get_rect(topleft=(school_bus_x_pos, 260)),
        'convertible': convertible.get_rect(topleft=(convertible_x_pos, 260)),
        'police': police.get_rect(topleft=(police_x_pos, 395))
    }

    # Check for collisions
    for vehicle_name, vehicle_rect in vehicle_rectangles.items():
        if zombie_rect.colliderect(vehicle_rect) and not collision_status[vehicle_name]:
            collision_sound.play()
            collision_status[vehicle_name] = True
            print(f"Collision with {vehicle_name} detected!")
            game_over_screen()


    pygame.display.flip()
    clock.tick(60)
