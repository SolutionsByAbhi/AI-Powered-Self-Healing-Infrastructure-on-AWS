import time

from send_events import publish


def main():

    while True:

        publish()

        time.sleep(15)


if __name__ == "__main__":

    main()
