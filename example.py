from windmm.driver import WinDmmDriver

if __name__ == '__main__':
    # Initialize WinDMM driver with specified RS-232 port name as string.
    # For Windows it can be 'COM1' or 'COM4'
    # For Unix or MacOS it can be '/dev/tty.xx'
    driver = WinDmmDriver('/dev/tty.usbserial-14130')

    # Check is serial port opened
    if not driver.is_open():
        print("Port is not opened")
        exit(-1)

    # Reading data 1000 times
    n = 0
    while n < 1000:
        data = driver.read_data()
        if data:
            print(data.get_raw())
            print(data)
        n = n + 1

    # Close serial port
    driver.close()
