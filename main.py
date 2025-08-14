import subprocess
import json
import os

print("\n\n=====================")
print("\n\nWelcome to cool inventory")
# Ensure data.json exists
if not os.path.exists("data.json"):
    open("data.json", "w").close()  # Creates empty file

data = {}

ask = input("Is this your first time using cool? (Y/n) ")
if ask.lower() == "y":
    item = input("What is your first fridge item? ")
    amount = input(f"How much of {item} is there? ")
    data[item] = int(amount)
    with open("data.json", "w") as f:
        json.dump(data, f)
else:
    try:
        with open("data.json", "r") as f:
            raw = f.read().strip()
            if raw:
                data = json.loads(raw)
            else:
                data = {}
    except Exception as e:
        print(f"Error loading data: {e}")
        data = {}

def save_data():
    with open("data.json", "w") as f:
        json.dump(data, f)

def print_help():
    print("""
Commands:
    get [item]           - Show amount of item
    list                 - List all items and amounts
    set [item] [amount]  - Set the amount of an item
    add [item] [amount]  - Add amount to item
    subtract [item] [amount] - Subtract amount from item
    new [item] [amount]  - Add a new item (error if exists)
    help                 - Show this help
    exit                 - Exit program
    """)

run = True
while run:
    cmd = input("cool-inventory> ").strip()
    if not cmd:
        continue
    parts = cmd.split()
    if parts[0] == "get" and len(parts) == 2:
        item = parts[1]
        if item in data:
            print(f"{item}: {data[item]}")
        else:
            print(f"{item} not found.")
    elif parts[0] == "list":
        if data:
            for k, v in data.items():
                print(f"{k}: {v}")
        else:
            print("Inventory is empty.")
    elif parts[0] == "set" and len(parts) == 3:
        item, amount = parts[1], parts[2]
        try:
            data[item] = int(amount)
            save_data()
            print(f"{item} set to {amount}.")
        except:
            print("Invalid amount.")
    elif parts[0] == "add" and len(parts) == 3:
        item, amount = parts[1], parts[2]
        if item in data:
            try:
                data[item] += int(amount)
                save_data()
                print(f"Added {amount} to {item}. Now: {data[item]}")
            except:
                print("Invalid amount.")
        else:
            print(f"{item} not found.")
    elif parts[0] == "subtract" and len(parts) == 3:
        item, amount = parts[1], parts[2]
        if item in data:
            try:
                data[item] -= int(amount)
                if data[item] < 0:
                    data[item] = 0
                save_data()
                print(f"Subtracted {amount} from {item}. Now: {data[item]}")
            except:
                print("Invalid amount.")
        else:
            print(f"{item} not found.")
    elif parts[0] == "new" and len(parts) == 3:
        item, amount = parts[1], parts[2]
        if item in data:
            print(f"{item} already exists.")
        else:
            try:
                data[item] = int(amount)
                save_data()
                print(f"New item {item} added with amount {amount}.")
            except:
                print("Invalid amount.")
    elif parts[0] == "help":
        print_help()
    elif parts[0] == "exit":
        run = False
        print("Goodbye!")
    else:
        print("Unknown command. Type 'help' for commands.")
