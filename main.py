FPS = 30
dinosaur_y = 0
y_acceleration = 0.03
y_speed = 0
JUMP_FORCE = 40

def touching_ground():
    return dinosaur_y >= 4

def fall():
    global dinosaur_y, y_speed
    if touching_ground():
        # Stand on ground
        y_speed = 0
        dinosaur_y = 4
    else:
        # Falling in air
        y_speed += y_acceleration
        dinosaur_y += y_speed

def jump():
    global y_speed
    if touching_ground() and input.button_is_pressed(Button.A):
        # Only jump if on ground
        y_speed -= JUMP_FORCE

def draw():
    basic.clear_screen()
    led.plot(1, dinosaur_y)
    basic.pause(1000/FPS)

def on_forever():
    fall()
    jump()
    draw()
basic.forever(on_forever)
