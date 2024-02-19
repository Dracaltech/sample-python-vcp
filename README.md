# sample-node-vcp
Dracal // SDK code sample for Node on VCP

## Assumptions

Running this repository requires you to have installed:
- Python (version >= `3.x`)

This also assumes you are able to run `pip` package manager, ideally a recent version (e.g. >= `23.x`)
```
pip --version
```

## Simple usage

Install dependencies _(configured in `requirements.txt`)_
```
pip install
```

Run script
```
python main.py <port> <interval>
```

e.g. if your device is running on `/dev/ttyACM0` _(refer to [VCP getting started](https://www.dracal.com/en/tutorials/getting-started-with-vcp-mode/))_ and you want to poll data every 1000ms:
```
python main.py /dev/ttyACM0 1000
```

## Sample output
<img src="https://github.com/Dracaltech/sample-python-vcp/assets/1357711/7f784aec-37b5-4c47-a447-a1c18885383f" width=400 />

```
Ξ dracal/sample-python-vcp git:(develop) ▶ python main.py /dev/ttyACM0 1000
I, Product ID, Serial Number, Message, MS5611 Pressure, Pa, SHT31 Temperature, C, SHT31 Relative Humidity, %
Poll interval set to 1000 ms
Printing 2 fractional digits

Mon Feb 19 12:55:11 2024, VCP-PTH450-CAL E24638
MS5611 Pressure          102989 Pa
SHT31 Temperature        30.5 C
SHT31 Relative Humidity  53.91 %

Mon Feb 19 12:55:12 2024, VCP-PTH450-CAL E24638
MS5611 Pressure          102989 Pa
SHT31 Temperature        30.46 C
SHT31 Relative Humidity  53.91 %

Mon Feb 19 12:55:13 2024, VCP-PTH450-CAL E24638
MS5611 Pressure          102991 Pa
SHT31 Temperature        30.52 C
SHT31 Relative Humidity  53.91 %

Mon Feb 19 12:55:14 2024, VCP-PTH450-CAL E24638
MS5611 Pressure          102991 Pa
SHT31 Temperature        30.48 C
SHT31 Relative Humidity  53.87 %
^CTraceback (most recent call last):
  File "/home/mathieu/dev/dracal/sample-python-vcp/main.py", line 41, in <module>
    line = ser.readline()
  File "/home/mathieu/.pyenv/versions/3.9.7/lib/python3.9/site-packages/serial/serialposix.py", line 565, in read
    ready, _, _ = select.select([self.fd, self.pipe_abort_read_r], [], [], timeout.time_left())
KeyboardInterrupt

↑130 dracal/sample-python-vcp git:(develop) ▶
```

