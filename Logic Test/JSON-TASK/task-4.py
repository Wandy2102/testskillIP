import json

# load the inventory data from JSON
with open('JSON-TASK/inventory.json', 'r') as f:
    inventory = json.load(f)

# find items in meeting room
meeting_room_items = []
for item in inventory:
    if item['placement']['name'] == 'Meeting Room':
        meeting_room_items.append(item)

# print the meeting room items
print(meeting_room_items)
