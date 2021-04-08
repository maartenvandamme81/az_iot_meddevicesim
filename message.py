import random
import params
import time
from iothub_client_init import iothub_client_init
from azure.iot.device import IoTHubDeviceClient, Message


def iothub_message(condition):
    try:
        client = iothub_client_init()

        if condition == 'normal':
            starttime = 4
            while starttime > 0:
                starttime -= 1
                temperature = random.uniform(params.normal_temp_min, params.normal_temp_max)
                heartbeat = random.uniform(params.normal_heartbeat_min, params.normal_heartbeat_max)
                oxygen = random.uniform(params.normal_oxygen_min, params.normal_oxygen_max)

                msg_txt_formatted = params.MSG_TXT.format(temperature=temperature, heartbeat=heartbeat, oxygen=oxygen)
                message = Message(msg_txt_formatted)

                print(f"Sending {condition} message: {message}")
                client.send_message(message)
                time.sleep(10)

        elif condition == 'hightemp':
            starttime = 2
            while starttime > 0:
                starttime -= 1
                temperature = random.uniform(params.normal_temp_min, params.normal_temp_max)
                heartbeat = random.uniform(params.normal_heartbeat_min, params.normal_heartbeat_max)
                oxygen = random.uniform(params.normal_oxygen_min, params.normal_oxygen_max)

                msg_txt_formatted = params.MSG_TXT.format(temperature=temperature, heartbeat=heartbeat, oxygen=oxygen)
                message = Message(msg_txt_formatted)

                print(f"Sending {condition} message: {message}")
                client.send_message(message)
                time.sleep(10)

            firstevent = 2
            while firstevent > 0:
                firstevent -= 1
                temperature = random.uniform(params.high_temp_firstevent_min, params.high_temp_firstevent_max)
                heartbeat = random.uniform(params.high_heartbeat_firstevent_min, params.high_heartbeat_firstevent_max)
                oxygen = random.uniform(params.normal_oxygen_min, params.normal_oxygen_max)

                msg_txt_formatted = params.MSG_TXT.format(temperature=temperature, heartbeat=heartbeat, oxygen=oxygen)
                message = Message(msg_txt_formatted)

                print(f"Sending {condition} message: {message}")
                client.send_message(message)
                time.sleep(10)

            secondevent = 2
            while secondevent > 0:
                secondevent -= 1
                temperature = random.uniform(params.high_temp_secondevent_min, params.high_temp_secondevent_max)
                heartbeat = random.uniform(params.high_heartbeat_secondevent_min, params.high_heartbeat_secondevent_max)
                oxygen = random.uniform(params.normal_oxygen_min, params.normal_oxygen_max)

                msg_txt_formatted = params.MSG_TXT.format(temperature=temperature, heartbeat=heartbeat, oxygen=oxygen)
                message = Message(msg_txt_formatted)

                print(f"Sending {condition} message: {message}")
                client.send_message(message)
                time.sleep(10)

            thirdevent = 2
            while thirdevent > 0:
                thirdevent -= 1
                temperature = random.uniform(params.high_temp_thirdevent_min, params.high_temp_thirdevent_max)
                heartbeat = random.uniform(params.high_heartbeat_thirdevent_min, params.high_heartbeat_thirdevent_max)
                oxygen = random.uniform(params.normal_oxygen_min, params.normal_oxygen_max)

                msg_txt_formatted = params.MSG_TXT.format(temperature=temperature, heartbeat=heartbeat, oxygen=oxygen)
                message = Message(msg_txt_formatted)

                print(f"Sending {condition} message: {message}")
                client.send_message(message)
                time.sleep(10)

            finalevent = 2
            while finalevent > 0:
                finalevent -= 1
                temperature = random.uniform(0, 0)
                heartbeat = random.uniform(0, 0)
                oxygen = random.uniform(0, 0)

                msg_txt_formatted = params.MSG_TXT.format(temperature=temperature, heartbeat=heartbeat, oxygen=oxygen)
                message = Message(msg_txt_formatted)

                print(f"Sending {condition} message: {message}")
                client.send_message(message)
                time.sleep(10)

    except KeyboardInterrupt:
        pass
