import time
import os
import keyboard
from colorama import * # type: ignore
grasstouch = 0
with open('funnything.txt', 'r') as f:
    print(f.read())

time.sleep(3)
clear = lambda: os.system('clear')
clear()
with open('./textfiles/gts.txt', 'r') as f:
    print(Fore.GREEN + Style.BRIGHT + f.read())
    
print(Fore.GREEN + Style.BRIGHT + "Grass " + Fore.CYAN + Style.BRIGHT + "Touching " + Fore.WHITE + Style.BRIGHT + "Simulator")
usernam = input("What is your name: ")
with open('./textfiles/menu.txt', 'r') as f:
    print(f.read())

choice = input("Choose what you want to do: ")
with open('./textfiles/grass.txt', 'r') as a:
    print(Fore.GREEN + a.read())
print(Fore.RESET + "This is grass \n Grass is good. \n It is important to touch it.")
print("Press spacebar to touch it!")
keyboard.wait('space')
print("good. now press it again.")
keyboard.wait('space')
print("good.")
print("press p at any time to view your progress")
time.sleep(0.5)
clear()
with open('./textfiles/grass.txt', 'r') as a:
    print(Fore.GREEN + a.read())

while True:
    
    if keyboard.read_key() == "space":
        print(Fore.RESET + "\ntouched grass! +1")
        grasstouch = grasstouch + 1
    
    if keyboard.read_key() == "p":
        print(" - you have touched grass " + str(grasstouch) + " times!")
    if grasstouch == 100:
        
        print("YOU HAVE TOUCHED GRASS 100 TIMES!!!!!!!!\n\n")
        print("now please go outside and do the same.")
        print("there are many benefits to being outside, like you get a life.")
        time.sleep(10)
        exit()



