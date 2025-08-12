import subprocess # installs libraries to run commands
import json

print("\n\n=====================")
print("\n\nWelcome to cool inventory")
subprocess.run('echo "" >> index.cool', shell=True) # runs echo "" >> index.cool command in linux
subprocess.run('echo "" >> index.json', shell=True) # runs command in linux

data = {}

ask = input("Is this your first time using cool? (Y/n) ")
if ask == "y" or ask == "Y":
    item = input("What is your first fridge item? ")
    amount = input("How much of " + item + " is there? ")
    data[item] = int(amount)
    with open("data.json", "w") as f:
        json.dump(data, f)
else:
    with open("data.json", "r") as f:
        data = json.load(f)
    print("your current data is\n\n")
    print(data)
