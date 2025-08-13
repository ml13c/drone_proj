import socket
from gpiozero import Servo

servo = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5005))

try:
    while True:
        data, addr = sock.recvfrom(1024)
        command = data.decode().strip()

        if command == "left":
            servo.value = -0.5
        elif command == "right":
            servo.value = 0.5
        else:
            servo.value = 0

except KeyboardInterrupt:
    pass
finally:
    servo.value = 0
