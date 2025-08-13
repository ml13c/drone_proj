from gpiozero import AngularServo
from time import sleep

servo = AngularServo(
    18,
    min_angle=0,
    max_angle=180,  # most hobby servos can't actually do 360°
    min_pulse_width=0.5/1000,
    max_pulse_width=2.5/1000
)

def set_angle(angle):
    servo.angle = angle
    sleep(1)

try:
    while True:
        angle_input = input("Enter angle (0-180) or 'q' to quit: ").strip()
        if angle_input.lower() == "q":
            break
        try:
            angle = int(angle_input)
            if 0 <= angle <= 180:
                set_angle(angle)
            else:
                print("Please enter a value between 0 and 180.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")
except KeyboardInterrupt:
    print("\nProgram stopped by user.")
