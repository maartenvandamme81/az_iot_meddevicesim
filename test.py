
with open("devices.txt", "r") as file:
    lines = file.read().splitlines()
devices = tuple(lines)
print(devices)
print(type(devices))
