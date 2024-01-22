#!/usr/bin/python
import sys
import time

import serial  # https://pypi.org/project/pyserial/
import crccheck  # https://pypi.org/project/crccheck/


# Parse command-line arguments
if len(sys.argv) not in (2, 3):
    print("Syntax: %s  [poll_interval_ms]" % sys.argv[0])
    print("Example (Windows)  %s COM1 1000" % sys.argv[0])
    print("Example (Linux/MacOS)    %s /dev/ttyACM0 1000" % sys.argv[0])
    sys.exit(1)

port = sys.argv[1]

if len(sys.argv) >= 3:
    interval = int(sys.argv[2])
else:
    interval = 1000  # default


crc_checker = crccheck.crc.CrcXmodem()

# Open serial port

with serial.Serial(port) as ser:
    ser.readlines(2)  # Discard the first two lines as they may be partial

    ser.write(b"INFO\n")  # Get the info line

    time.sleep(0.3)  # Allow 100 ms for request to complete
    ser.write(b"POLL %d\n" % interval)  # Set poll interval

    time.sleep(0.3)
    ser.write(b"FRAC 2\n")  # Return data with two digits past the decimal

    # Process all lines in a loop
    while True:
        line = ser.readline()
        t = time.ctime()

        if not line:
            break

        # Check data integrity using CRC-16-CCITT (XMODEM)
        try:
            data, crc = line.split(b"*")
            crc = int(crc, 16)  # parse hexadecimal string into an integer variable
            crc_checker.process(data)
            computed_crc = crc_checker.final()
            crc_checker.reset()
            crc_success = computed_crc == crc
        except ValueError:
            # We will get here if there isn't exactly one '*' character in the line.
            # If that's the case, data is most certainly corrupt!
            crc_success = False

        if not crc_success:
            print("Data integrity error")
            break

        # Decode bytes into a list of strings
        data = data.decode("ASCII").strip(",").split(",")

        if data[0] == "I":
            if data[1] == "Product ID":  # For the INFO command response
                info_line = data
                padlen = max(len(s) for s in info_line[4::2])
                print(", ".join(info_line))
            else:  # Other info lines only need the message to be echoed
                print(data[3])
        else:
            # Create an ID for the device
            device = f"{data[1]} {data[2]}"

            # Convert number strings to the appropriate numerical format
            for i in range(4, len(data), 2):
                try:
                    data[i] = int(data[i])
                except ValueError:
                    data[i] = float(data[i])

            # Convert data to a tuple of (sensor, value, unit) triads
            data = zip(info_line[4::2], data[4::2], data[5::2])

            # Display the current time, product id and serial number before every point
            print(f"\n{t}, {device}")
            for d in data:
                print(("{:" + str(padlen + 2) + "}{} {}").format(*d))
