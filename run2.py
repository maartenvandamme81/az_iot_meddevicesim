import multiprocessing
import os
# Creating the tuple of all the processes

with open("devices.txt", "r") as file:
    lines = file.read().splitlines()
all_processes = tuple(lines)
count = len(all_processes)


# This block of code enables us to call the script from command line.
def execute(process):
    os.system(f'python3 {process}')


try:
    print(f"IoT - Simulating {count} medical monitoring devices")
    print("Press Ctrl-C to exit")
    process_pool = multiprocessing.Pool(processes=count)
    process_pool.map(execute, all_processes)

except KeyboardInterrupt:
    print("IoTHubClient sample stopped")
