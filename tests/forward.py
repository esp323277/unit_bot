import unit_motor

bot = unit_motor.Robot()

RUN_TIME = 1
SPEED = 1

print("forward")
bot.forward(SPEED, RUN_TIME)
