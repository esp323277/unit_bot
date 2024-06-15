import time
import unit_motor

# Constants
RUN_TIME = 1
SLEEP_TIME = 1
SPEED = 0.1

# Initialize robot
bot = unit_motor.Robot()

def perform_action(action, speed, run_time, sleep_time):
    """Perform a bot action and sleep for a specified time."""
    action(speed, run_time)
    time.sleep(sleep_time)

def main():
    """Main function to control the bot."""
    actions = [
        ("forward", bot.forward, SPEED),
        ("backward", bot.backward, SPEED),
        ("spin left", bot.left, SPEED),
        ("spin right", bot.right, SPEED),
        ("steer forward full left", bot.steer, SPEED, -1),
        ("steer forward full right", bot.steer, SPEED, 1),
        ("steer forward half left", bot.steer, SPEED, -0.5),
        ("steer forward half right", bot.steer, SPEED, 0.5),
        ("steer backward full left", bot.steer, -SPEED, -1),
        ("steer backward full right", bot.steer, -SPEED, 1),
        ("steer backward half left", bot.steer, -SPEED, -0.5),
        ("steer backward half right", bot.steer, -SPEED, 0.5),
    ]

    for description, action, *params in actions:
        print(description)
        perform_action(lambda speed, run_time: action(*params), SPEED, RUN_TIME, SLEEP_TIME)

if __name__ == "__main__":
    main()

