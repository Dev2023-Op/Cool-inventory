import subprocess # instals libarys to run commands
import subprocess
import json

print("\n\n=====================")
print("\n\nWelcome to cool inventory")
subprocess.run('echo "" >> index.cool', shell=True) # runns echo "" >> index.cool command in linux
subprocess.run('echo "" >> index.json', shell=True) # runns command in linux

data = {}

ask = input("Is this your first time using cool? (Y/n) ")
if ask == "y" or "Y":
	item = input("What is your first fridge item? ")
	amount = input("How much of " + item + " is there? ")
	data[item] = int(amount)
	with open("data.json", "w") as f:
    		json.dump(data, f)

else:
	with open("data.json", "w") as f:
		json.load(data, f)

	print("your current data is\n\n")
	print(data)
