import time
import unit_motor

bot = unit_motor.Robot()

RUN_TIME = 1
SLEEP_TIME = 1
SPEED = 0.1

print("forward")
bot.forward(SPEED, RUN_TIME)
time.sleep(SLEEP_TIME)

print("backward")
bot.backward(SPEED, RUN_TIME)
time.sleep(SLEEP_TIME)

print("spin left")
bot.left(SPEED, RUN_TIME)
time.sleep(SLEEP_TIME)

print("spin right")
bot.right(SPEED, RUN_TIME)
time.sleep(SLEEP_TIME)

print("steer forward full left")
bot.steer(SPEED, -1, RUN_TIME)
time.sleep(SLEEP_TIME)

print("steer forward full right")
bot.steer(SPEED, 1, RUN_TIME)
time.sleep(SLEEP_TIME)

print("steer forward half left")
bot.steer(SPEED, -0.5, RUN_TIME)
time.sleep(SLEEP_TIME)

print("steer forward half right")
bot.steer(SPEED, 0.5, RUN_TIME)
time.sleep(SLEEP_TIME)

print("steer backward full left")
bot.steer(-SPEED, -1, RUN_TIME)
time.sleep(SLEEP_TIME)

print("steer backward full right")
bot.steer(-SPEED, 1, RUN_TIME)
time.sleep(SLEEP_TIME)

print("steer backward half left")
bot.steer(-SPEED, -0.5, RUN_TIME)
time.sleep(SLEEP_TIME)

print("steer backward half right")
bot.steer(-SPEED, 0.5, RUN_TIME)
time.sleep(SLEEP_TIME)

