# Used to simulate data being sent online,
# but really it's just a text file.

COMMS_FILE = 'Transmitted_Data'


def send(data):
    # Send data to the receiver.
    with open(COMMS_FILE, 'w') as f:
        f.write(data)


def read():
    # Read data from the sender.
    with open(COMMS_FILE, 'r') as f:
        return f.read()