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
