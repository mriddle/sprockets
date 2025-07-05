# listener.py (to be uploaded to the hub)
# responsible for receiving commands from the iOS app over Bluetooth

from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Standard MicroPython modules
from usys import stdin, stdout
from uselect import poll


# Optional: Register stdin for polling. This allows
# you to wait for incoming data without blocking.
keyboard = poll()
keyboard.register(stdin)

hub = PrimeHub()

while True:
    # Let the remote program know we are ready for a command.
    stdout.buffer.write(b"rdy")

    # Optional: Check available input.
    while not keyboard.poll(0):
        # Optional: Do something here.
        wait(10)

    # Read three bytes.
    cmd = stdin.buffer.read(3)

    # Decide what to do based on the command.
    if cmd == b"green":
        hub.light.on(Color.GREEN)
        wait(1000)

        hub.light.off()
        wait(500)
    elif cmd == b"red":
        hub.light.on(Color.RED)
        wait(1000)

        hub.light.off()
        wait(500)
    elif cmd == b"bye":
        break
