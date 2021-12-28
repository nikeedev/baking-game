print("Loading all needed things, please be patient :)")
print("...")
import time, os, getpass
from about import *
running = True
use_username = True

def enter():
    input("press ENTER to continue...")


time.sleep(2)
print("Hello and welcome to Baking Game! v.0.1.0!")
input("press Enter to continue...")
while use_username:
    print("\n\nWhat is your name or in this case nickname?")
    username = input("My nickname is... ")
    agree = input(
        "\n\nDo you want to use this username(write 1), PC username(write 2), or change this username(write 3)? ")
    if agree == "1":
        use_username = False
    elif agree == "2":
        username = getpass.getuser()
        use_username = False
    elif agree == "3":
        continue
print(f"Hello {username}. Nice, now can we begin to bake!")
enter()
print("In this game, you are going to bake much, from cakes and muffins, to breads and various buns!")
enter()
print("This game is based on the same way as Cooking game, just this is baking version of it.")
print("")

while running:
    print("Hello, " + username + " ! What do you want to do now?")
    print("List of Commands:      ")
    print("                   Recipes")
    print("                   Inventory (Check your storage, your XP and you baked goods)")
    print("                   Bake ( Baking starts here! )")
    print("                   Market(Sell and Buy food)")
    print("                   Info")
    print("                   Update Log")
    print("                   Exit")
    command = input("                   ")

    if "recipe" in command:
        print("                   ")
