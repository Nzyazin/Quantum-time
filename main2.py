from _datetime import datetime
import time
import pygame

RES = WIDTH, HEIGHT = 1200, 800
pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Verdana', 200)


time_now = datetime.now()
secs = time.localtime()
print(time_now, " время сейчас")
print(time.mktime(secs), " секунд сейчас")
print((time.mktime(secs)) / 60, " минут сейчас")
print((time.mktime(secs) + 10800) / 3600 % 24, " часов сейчас")

old_secs = time.mktime(secs) + 10800

all_new_secs = old_secs * 100 / 75
all_new_mins = all_new_secs / 60
all_new_hours = all_new_mins / 60

today_new_secs = all_new_secs % 60
print(all_new_secs, " новых секунд сейчас")
print(all_new_mins, " новых минут сейчас")
print(all_new_hours, " новых часов сейчас")
today_new_mins = all_new_mins % 60
today_new_hours = all_new_hours % 32


print(today_new_secs, " новых секунд в сутках")
print(today_new_mins, " новых минут в сутках")
print(today_new_hours, " новых часов в сутках")

start_time = time.time()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    surface.fill(pygame.Color('black'))

    time_now = datetime.now()
    secs = time.localtime()

    old_secs = time.mktime(secs) + 10800

    all_new_secs = old_secs * 100 / 75
    all_new_mins = all_new_secs / 60
    all_new_hours = all_new_mins / 60

    today_new_secs = all_new_secs % 60
    today_new_mins = all_new_mins % 60
    today_new_hours = all_new_hours % 32

    current_time = '%s:%s:%s' % (int(today_new_hours), int(today_new_mins), int(today_new_secs))

    time_render = font.render(current_time, True, pygame.Color('forestgreen'), pygame.Color('orange'))
    surface.blit(time_render, (120, 150))

    pygame.display.flip()
    clock.tick(20)




