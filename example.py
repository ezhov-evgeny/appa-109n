from windmm.driver import AppaDriver

if __name__ == '__main__':
    driver = AppaDriver('/dev/tty.usbserial-14130')
    driver.is_open()
    n = 0
    while n < 1000:
        data = driver.read_data()
        if data:
            print(data.get_raw())
            print(data)
        n = n + 1
    driver.close()
