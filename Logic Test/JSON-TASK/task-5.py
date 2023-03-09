import json

with open('JSON-TASK/inventory.json', 'r') as f:
    inventory = json.load(f)

electronic_devices = []

for item in inventory:
    if item['type'] == 'electronic' or 'furniture':
        electronic_devices.append(item)

print(electronic_devices)