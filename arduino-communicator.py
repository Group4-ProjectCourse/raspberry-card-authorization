import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)#sudo chmod a+rw /dev/ttyACM0
ser.flush()

def write_message(message):
    ser.write((str(message) + "\n").encode('ascii'))
    
def read_message():
    while True:
        line = ser.readline().decode('utf-8').rstrip()
        if line:
            return line