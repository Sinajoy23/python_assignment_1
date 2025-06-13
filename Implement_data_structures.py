# Step 1 - Create Inventory
inventory = {
    "orange": (10, 2.5),
    "grapes": (20, 1.2)
}
# Add item
inventory["mango"] = (15, 3.0)

# Remove 
del inventory["grapes"]  


inventory["orange"] = (12, 2.8)  # Updated quantity and price






# Display Inventory
print("Current inventory:")
for item, (quantity, price) in inventory.items():
    print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")

# Total Inventory Value
total_value = 0
for quantity, price in inventory.values():
    total_value += quantity * price

print(f"Total value of inventory: ${total_value}")

