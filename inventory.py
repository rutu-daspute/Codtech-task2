from tkinter import *

# Initialize the main window
root = Tk()
root.title("Inventory Management System")
root.geometry("400x400")

# Function to add items to the inventory
def add_item():
    item_name = item_name_entry.get()
    quantity = int(quantity_entry.get())
    
    inventory[item_name] = inventory.get(item_name, 0) + quantity
    
    result_label.config(text=f"Added {quantity} {item_name}(s). Current stock: {inventory[item_name]}")

# Function to remove items from the inventory
def remove_item():
    item_name = item_name_entry.get()
    quantity = int(quantity_entry.get())
    
    if item_name in inventory and inventory[item_name] >= quantity:
        inventory[item_name] -= quantity
        result_label.config(text=f"Removed {quantity} {item_name}(s). Current stock: {inventory[item_name]}")
    else:
        result_label.config(text=f"Not enough {item_name} in stock or item not found.")

# Inventory dictionary to store item names and their quantities
inventory = {}

# Labels for item name and quantity
Label(root, text="Item Name:", font="arial 10").place(x=50, y=20)
Label(root, text="Quantity:", font="arial 10").place(x=50, y=70)

# Entries for item name and quantity
item_name_value = StringVar()
quantity_value = StringVar()

item_name_entry = Entry(root, textvariable=item_name_value, font="arial 15", width=15)
quantity_entry = Entry(root, textvariable=quantity_value, font="arial 15", width=15)

item_name_entry.place(x=150, y=20)
quantity_entry.place(x=150, y=70)

# Label to display results
result_label = Label(root, text="", font="arial 10")
result_label.place(x=50, y=170)

# Buttons to add and remove items
Button(root, text="Add Item", font="arial 15", bg="white", bd=10, width=8, command=add_item).place(x=50, y=300)
Button(root, text="Remove Item", font="arial 15", bg="white", bd=10, width=10, command=remove_item).place(x=200, y=300)

# Exit button
Button(root, text="Exit", font="arial 15", bg="white", bd=10, width=8, command=root.quit).place(x=150, y=350)

root.mainloop()