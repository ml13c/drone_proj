import socket
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()
servo = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo.value = 0  # ensure stopped at start

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5005))

print("Waiting for commands from laptop...")

current_command = None  # keep track of last command

try:
    while True:
        # Non-blocking receive with small timeout
        sock.settimeout(0.1)
        try:
            data, addr = sock.recvfrom(1024)
            command = data.decode().strip()
        except socket.timeout:
            command = None

        if command and command != current_command:
            current_command = command

            if command == "left":
                servo.value = -1
                print("Turning LEFT")
            elif command == "right":
                servo.value = 1
                print("Turning RIGHT")
            elif command == "stop":
                servo.value = 0
                print("Stopping servo")
            else:
                servo.value = 0
                print("Unknown command, stopping servo")

        # Keep sending the last command to servo for stability
        sleep(0.05)

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    servo.value = 0
    print("Servo stopped.")
