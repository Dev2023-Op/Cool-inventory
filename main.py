import subprocess
import json
import os
# Ensure data.json exists
if not os.path.exists("data.json"):
    open("data.json", "w").close()  # Creates empty file

data = {}

ask = input("Is this your first time using this? (Y/n) ")
if ask.lower() == "y":
    teacher = input("What is your first late teacher? ")
    amount = input(f"How late {teacher} in minutes (exclude the m)? ")
    data[teacher] = int(amount)
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
    get [teacher]           - Show amount of item
    list                 - List all items and amounts
    set [teacher] [amount]  - Set the amount of an item
    add [teacher] [amount]  - Add amount to item
    subtract [teacher] [amount] - Subtract amount from item
    new [teacher] [amount]  - Add a new item (error if exists)
    help                 - Show this help
    exit                 - Exit program
    """)

run = True
while run:
    cmd = input("late-teachers> ").strip()
    if not cmd:
        continue
    parts = cmd.split()
    if parts[0] == "get" and len(parts) == 2:
        item = parts[1]
        if item in data:
            print(f"{teacher}: {data[teacher]}")
        else:
            print(f"{teacher} not found.")
    elif parts[0] == "list":
        if data:
            for k, v in data.items():
                print(f"{k}: {v}")
        else:
            print("Inventory is empty.")
    elif parts[0] == "set" and len(parts) == 3:
        teacher, amount = parts[1], parts[2]
        try:
            data[teacher] = int(amount)
            save_data()
            print(f"{teacher} set to {amount}.")
        except:
            print("Invalid amount.")
    elif parts[0] == "add" and len(parts) == 3:
        teacher, amount = parts[1], parts[2]
        if teacher in data:
            try:
                data[teacher] += int(amount)
                save_data()
                print(f"Added {amount} to {teacher}. Now: {data[teacher]}")
            except:
                print("Invalid amount.")
        else:
            print(f"{teacher} not found.")
    elif parts[0] == "subtract" and len(parts) == 3:
        teacher, amount = parts[1], parts[2]
        if teacher in data:
            try:
                data[teacher] -= int(amount)
                if data[teacher] < 0:
                    data[teacher] = 0
                save_data()
                print(f"Subtracted {amount} from {teacher}. Now: {data[teacher]}")
            except:
                print("Invalid amount.")
        else:
            print(f"{teacher} not found.")
    elif parts[0] == "new" and len(parts) == 3:
        item, amount = parts[1], parts[2]
        if teacher in data:
            print(f"{teacher} already exists.")
        else:
            try:
                data[teacher] = int(amount)
                save_data()
                print(f"New item {teacher} added with amount {amount}.")
            except:
                print("Invalid amount.")
    elif parts[0] == "help":
        print_help()
    elif parts[0] == "exit":
        run = False
        print("Goodbye!")
    else:
        print("Unknown command. Type 'help' for commands.")
