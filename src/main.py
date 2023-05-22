import time


if __name__ == "__main__":
    for i in range(7200):
        try:
            raise RuntimeError
        except RuntimeError as e:
            print(e)
        time.sleep(1)
