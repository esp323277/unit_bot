from unit import motor
import pygame

# TODO 
# 1. Add logic for unit_motor steering

# Starting at 10% power
speed = 0.1


def adjust_speed(delta):
        global speed
        if -1 < speed < 1:
            speed += delta
            speed = max(min(speed, 1), -1)  # Ensure speed stays within bounds
            print(f"Speed adjusted to {speed}")
        else:
            print("Speed is already at its limit")


# Button mapping
buttons = {
    "exit": 10,
    "forward": 1,
    "backward": 0,
    "left_turn": 3,
    "right_turn": 2,
    "speed_up": 14,
    "speed_down": 15,
}

# Initialize Pygame
pygame.init()

# Initialize the joystick
pygame.joystick.init()

# Initialise Unit robot
bot = motor.Robot()

# Check for joysticks
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joysticks connected")
else:
    # Use the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    
    print(f"Joystick name: {joystick.get_name()}")
    print(f"Number of axes: {joystick.get_numaxes()}")
    print(f"Number of buttons: {joystick.get_numbuttons()}")

    
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Exit on joystick disconnection
            elif event.type == pygame.JOYDEVICEREMOVED:
                print("Joystick disconnected")
                running = False
            
            # Button pressed
            elif event.type == pygame.JOYBUTTONDOWN:
                button = event.button
                print(f"Button {button} pressed")
                
                # Bot movement
                if button == buttons["forward"]:
                    bot.forward(speed)
                elif button == buttons["backward"]:
                    bot.backward(speed)
                elif button == buttons["left_turn"]:
                    bot.left(speed)
                elif button == buttons["right_turn"]:
                    bot.right(speed)
                
                # Speed adjustment
                elif button == buttons["speed_up"]:
                    adjust_speed(0.1)
                elif button == buttons["speed_down"]:
                    adjust_speed(-0.1)
                
                # Exit
                elif button == buttons["exit"]:
                    running = False
            
            # Button released
            elif event.type == pygame.JOYBUTTONUP:
                button = event.button
                print(f"Button {button} released")

                # Stop bot movement
                if button in (buttons["forward"], buttons["backward"], \
                              buttons["left_turn"], buttons["right_turn"]):
                    bot.stop()
    
    # Quit Pygame
    pygame.quit()
