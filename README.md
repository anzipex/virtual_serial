# RS-485 Virtual Communication Scripts

The virtual ports are created with `socat`, enabling you to test sending, receiving of RS-485 data packets in a local environment.

## Requirements

To use these scripts, you need to install the following dependencies:

1. **socat** (for creating virtual serial ports)
    ```bash
    sudo apt install socat
    ```
2. **pyserial** (for interacting with the virtual ports)
    ```bash
    pip3 install pyserial
    ```

## Setting up virtual ports

To create virtual ports for RS-485 communication, use the following `socat` command:

```bash
socat -d -d pty,raw,echo=0 pty,raw,echo=0
```

This will generate two virtual ports (e.g., `/dev/pts/1` and `/dev/pts/2`). The output should look something like this:

```
2024/10/09 12:58:54 socat[22086] N PTY is /dev/pts/1
2024/10/09 12:58:54 socat[22086] N PTY is /dev/pts/2
2024/10/09 12:58:54 socat[22086] N starting data transfer loop with FDs [5,5] and [7,7]
```

You can use these ports with the scripts for sending and receiving data. Or change the ports used in the scripts to those that were opened through `socat`.

## How to Use

1. Run the **send** script on one port:
    ```bash
    python3 rs485_send.py
    ```

2. Run the **receive** script on the same or another virtual port:
    ```bash
    python3 rs485_receive.py
    ```

3. The sender will transmit data, and the receiver will output the received data in both raw and hexadecimal format.

---

The `rs485_decode.py` is for experimental purposes only.
