import json

# load the inventory data from JSON
with open('JSON-TASK/inventory.json') as f:
    inventory_data = json.load(f)

# iterate through the inventory and find items with brown color
brown_items = []
for item in inventory_data:
    if "brown" in item["tags"]:
        brown_items.append(item)

# print the brown items
for item in brown_items:
    print(item["name"])
