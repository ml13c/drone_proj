from gpiozero import Servo
from time import sleep

# Continuous rotation servo on GPIO 18
servo = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

try:
    while True:
        cmd = input("Enter command (f=forward, b=back, s=stop, q=quit): ").strip().lower()

        if cmd == "f":
            servo.value = 1    # full forward
        elif cmd == "b":
            servo.value = -1   # full backward
        elif cmd == "s":
            servo.value = 0    # stop
        elif cmd == "q":
            servo.value = 0
            break
        else:
            print("Unknown command. Use f/b/s/q.")

except KeyboardInterrupt:
    pass

finally:
    servo.value = 0  # make sure it stops
