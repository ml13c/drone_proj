import socket
from gpiozero import Servo
from time import sleep

# Continuous rotation servo on PWM-capable pin (GPIO18)
servo = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
servo.value = 0  # stop initially

# UDP socket listening
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5005))  # listen on all interfaces

print("Waiting for commands from laptop...")

try:
    while True:
        data, addr = sock.recvfrom(1024)
        command = data.decode().strip()
        print(f"Received command: '{command}' from {addr}")

        if command == "left":
            servo.value = -0.5
            print("Turning LEFT")
        elif command == "right":
            servo.value = 0.5
            print("Turning RIGHT")
        elif command == "stop":
            servo.value = 0
            print("Stopping servo")
        else:
            servo.value = 0
            print("Unknown command. Stopping servo for safety.")

        sleep(0.05)  # small delay for stability

except KeyboardInterrupt:
    print("\nStopping program...")

finally:
    servo.value = 0
    print("Servo stopped.")
