import time
import atexit
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())

class Robot:
    def __init__(self, left_front_trim=0, right_front_trim=0, left_back_trim=0, right_back_trim=0, stop_at_exit=True):
        """Create an instance of the robot.  Can specify the following optional
        parameters:
         - left_front_trim: Amount to offset the speed of the left front motor, can be positive
                      or negative and useful for matching the speed of both
                      motors. Default is 0.
         - right_front_trim: Amount to offset the speed of the right front motor (see above).
         - left_back_trim: Amount to offset the speed of the left back motor.
         - right_back_trim: Amount to offset the speed of the right back motor.
         - stop_at_exit: Boolean to indicate if the motors should stop on program
                         exit. Default is True (highly recommended to keep this
                         value to prevent damage to the bot on program crash!).
        """

        self._trims = {
            'front_left': left_front_trim,
            'front_right': right_front_trim,
            'back_left': left_back_trim,
            'back_right': right_back_trim,
        }

        if stop_at_exit:
            atexit.register(self.stop)
        
        # Define motors
        self._motors = {
            'front_left': kit.motor1,
            'front_right': kit.motor2,
            'back_left': kit.motor3,
            'back_right': kit.motor4,
        }

    def _set_motor_speed(self, speed, motor_name):
        """Set the speed of the motor, taking into account its trim offset."""
        assert -1 <= speed <= 1, "Speed must be a value between -1 to 1 inclusive!"
        trim = self._trims[motor_name]
        motor = self._motors[motor_name]
        speed += trim
        speed = max(-1, min(1, speed))  # Constrain speed to -1 to 1 after trimming.
        motor.throttle = speed

    def set_speed(self, speed, motor_position):
        """Set the speed of the specified motor position."""
        motor_name = {
            'f_left': 'front_left',
            'f_right': 'front_right',
            'b_left': 'back_left',
            'b_right': 'back_right'
        }.get(motor_position)
        
        if motor_name:
            self._set_motor_speed(speed, motor_name)
        else:
            raise ValueError(f"Invalid motor position: {motor_position}")

    def stop(self):
        """Stop all movement."""
        for motor in self._motors.values():
            motor.throttle = 0

    def move(self, left_speed, right_speed, seconds=None):
        """Move the robot by setting the speed of the left and right motors.
        If seconds is specified, move for that amount of time and then stop.
        """
        self.set_speed(left_speed, 'f_left')
        self.set_speed(left_speed, 'b_left')
        self.set_speed(right_speed, 'f_right')
        self.set_speed(right_speed, 'b_right')
        
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def forward(self, speed, seconds=None):
        """Move forward at the specified speed. Will start moving forward and return unless
        a seconds value is specified, in which case the robot will move forward for that amount
        of time and then stop.
        """
        self.move(speed, speed, seconds)

    def backward(self, speed, seconds=None):
        """Move backward at the specified speed. Will start moving backward and return unless
        a seconds value is specified, in which case the robot will move backward for that amount
        of time and then stop.
        """
        self.move(-speed, -speed, seconds)

    def right(self, speed, seconds=None):
        """Spin to the right at the specified speed. Will start spinning and return unless
        a seconds value is specified, in which case the robot will spin for that amount of time
        and then stop.
        """
        self.move(speed, -speed, seconds)

    def left(self, speed, seconds=None):
        """Spin to the left at the specified speed. Will start spinning and return unless
        a seconds value is specified, in which case the robot will spin for that amount of time
        and then stop.
        """
        self.move(-speed, speed, seconds)

    def steer(self, speed, direction, seconds=None):
        """Move at the specified speed (0 to 1). Direction is +-1.
        Full left is -1, full right is +1.
        """
        left_speed = speed + direction / 2
        right_speed = speed - direction / 2
        self.move(left_speed, right_speed, seconds)