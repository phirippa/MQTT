import paho.mqtt.publish as publish
import time

count = 0

while( count< 10 ):
    publish.single("MyOffice/Indoor/Temp", "23.4", hostname="localhost")
    publish.single("MyOffice/Indoor/Humi", "33", hostname="localhost")
    publish.single("MyOffice/Indoor/Lamp", "ON", hostname="localhost")

    publish.single("MyOffice/Outdoor/Temp", "33.4", hostname="localhost")
    publish.single("MyOffice/Outdoor/Humi", "23", hostname="localhost")
    publish.single("MyOffice/Outdoor/Lamp", "OFF", hostname="localhost")

    time.sleep(2)
    count+=1
