#!/usr/bin/env python3
import click
import time
from trilobot import *
from trilobot import controller_mappings

left = '\x1b\x5b\x44'
right = '\x1b\x5b\x43'
up = '\x1b\x5b\x41'
down = '\x1b\x5b\x42'

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

tbot = Trilobot()

for led in range(NUM_UNDERLIGHTS):
    tbot.clear_underlighting(show=False)
    tbot.set_underlight(led, RED)
    time.sleep(0.1)
    tbot.clear_underlighting(show=False)
    tbot.set_underlight(led, GREEN)
    time.sleep(0.1)
    tbot.clear_underlighting(show=False)
    tbot.set_underlight(led, BLUE)
    time.sleep(0.1)

tbot.clear_underlighting()

h = 0
v = 0
spacing = 1.0 / NUM_UNDERLIGHTS

speed = 0.5

while True:
    # Read the controller bumpers to see if the tank steer mode has been enabled or disabled
    c = click.getchar()
    #click.echo(''.join([ '\\'+hex(ord(i))[1:] for i in c ]))
    if c == left:
        tbot.set_left_speed(-speed)
        tbot.set_right_speed(speed)
    elif c == right:
        tbot.set_left_speed(speed)
        tbot.set_right_speed(-speed)
    elif c == down:
        tbot.set_left_speed(-speed)
        tbot.set_right_speed(-speed)
    elif c == up:
        tbot.set_left_speed(speed)
        tbot.set_right_speed(speed)

    # Run a rotating rainbow effect on the RGB underlights
    for led in range(NUM_UNDERLIGHTS):
        led_h = h + (led * spacing)
        if led_h >= 1.0:
            led_h -= 1.0
        if c == ' ':
            tbot.set_underlight_hsv(led, 0.0, 0.0, 0.7, show=False)
        else:
            tbot.set_underlight_hsv(led, led_h, show=False)

    tbot.show_underlighting()

    # Advance the rotating rainbow effect
    h += 0.5 / 360
    if h >= 1.0:
        h -= 1.0

    time.sleep(0.01)
