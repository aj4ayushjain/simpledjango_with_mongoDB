import time


def send_notification(*args):
    """ dummy for sending sms notice """
    time.sleep(2)
    print(f"notification was sent with sms.{args}")
