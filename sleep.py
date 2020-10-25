from time import sleep
from py_imessage import imessage
import time

phone ="7327998071"
message ="Hello Sender! I am currently asleep, so if it is something urgent, I'm not sure if I could help you right at this moment, but if you need something for tomorrow then just leave a message I'll see it when I wake up"

def sleepMessage():
    hour = time.localtime(time.time()).tm_hour
    while True:
        sleep(10)
        if hour > 21 and hour < 5:
            guid = imessage.send(phone, message)
        else:
            print(False)

sleepMessage()
