from azure.iot.device import IoTHubDeviceClient, Message
import sys


def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(sys.argv[2])
    return client
