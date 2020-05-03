import paho.mqtt.client as mqtt
import time
import os
import json

#this script was tested using an MQTT broker
#using paho-mqtt library and Python3.5

if __name__ == "__main__":

    topic = ['i3dataseller/i3sellerhub/parking']
    port = 1883
    host = 'localhost'

try:

        client = mqtt.Client(protocol=mqtt.MQTTv311)
        #client.username_pw_set(account, pw)
        client.connect(host, port)
        print("Connected to broker") 
        #parsing JSON (uncomment the appropriate line below
        #for your experimentation)
        #with open("JSON_with_1_area.json", 'r') as jsonfile:
        #with open("JSON_with_1_area_1_lot.json", 'r') as jsonfile:
        #with open("JSON_with_1_area_1_lot_1_section.json", 'r') as jsonfile:
        #with open("JSON_with_1_area_1_lot_1_section_1_spot.json", 'r') as jsonfile:
        #with open("DowntownWithSpots.json", 'r') as jsonfile:
        #with open("LAXwithLots.json", 'r') as jsonfile:
        #with open("LAX_current_standard.json", 'r') as jsonfile:  
        #with open("Downtown_current_standard.json", 'r') as jsonfile:
        with open("Downtown_inventory_for_current_standard.json", 'r') as jsonfile:  
            reader=json.load(jsonfile)
            print(reader)
            client.publish(topic[0], json.dumps(reader))
        print("Published")

except Exception as e:
    print ("Exception" + str(e))
    exit(-1)
