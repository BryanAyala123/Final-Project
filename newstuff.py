# -*- coding: utf-8 -*-
"""
Created on Mon May 30 23:03:19 2022

@author: XLHS
"""
import random
print("---------BATTLESHIP--------")

ai_grid_a = ["?","?","?","?","?","?"]
ai_grid_b = ["?","?","?","?","?","?"]
ai_grid_c = ["?","?","?","?","?","?"]
ai_grid_d = ["?","?","?","?","?","?"]
ai_grid_e = ["?","?","?","?","?","?"]

ai_grid_a1 = ["x","x","x","x","x","x"]
ai_grid_b2 = ["x","x","x","x","x","x"]
ai_grid_c3 = ["x","x","x","x","x","x"]
ai_grid_d4 = ["x","x","x","x","x","x"]
ai_grid_e5 = ["x","x","x","x","x","x"]

player_grid_a = ["?","?","?","?","?","?"]
player_grid_b = ["?","?","?","?","?","?"]
player_grid_c = ["?","?","?","?","?","?"]
player_grid_d = ["?","?","?","?","?","?"]
player_grid_e = ["?","?","?","?","?","?"]

player_grid_a1 = ["x","x","x","x","x","x"]
player_grid_b2 = ["x","x","x","x","x","x"]
player_grid_c3 = ["x","x","x","x","x","x"]
player_grid_d4 = ["x","x","x","x","x","x"]
player_grid_e5 = ["x","x","x","x","x","x"]


for x in range(2):
     ai_grid_a1[random.randint(0, 4)] = "O"   
for x in range(2):
     ai_grid_b2[random.randint(0, 4)] = "O"
for x in range(2):
     ai_grid_c3[random.randint(0, 4)] = "O"     
for x in range(2):
     ai_grid_d4[random.randint(0, 4)] = "O"
for x in range(2): 
     ai_grid_e5[random.randint(0, 4)] = "O"

for x in range(2):
     player_grid_a1[random.randint(0, 4)] = "O"   
for x in range(2):
     player_grid_b2[random.randint(0, 4)] = "O"
for x in range(2):
     player_grid_c3[random.randint(0, 4)] = "O"     
for x in range(2):
     player_grid_d4[random.randint(0, 4)] = "O"
for x in range(2): 
     player_grid_e5[random.randint(0, 4)] = "O"

print(ai_grid_a1)
print(ai_grid_b2)
print(ai_grid_c3)
print(ai_grid_d4)
print(ai_grid_e5)

def print_grid():
    print(" ")
    print("---------Players Grid---------")
    print(ai_grid_a)
    print(ai_grid_b)
    print(ai_grid_c)
    print(ai_grid_d)
    print(ai_grid_e)

print_grid()

def players_turn():
    players_turns = True
    while players_turns is True:
        guess = input("Guess: ")
        if len(guess) != 2:
            print("Your Guess must be 2")
        if guess[0] == "A":
            if ai_grid_a1[int(guess[1])] == "x":
                print("Miss")
                ai_grid_a[int(guess[1])] = "x"
                players_turns = False
                print_grid()
            else:
                print("Hit")
                ai_grid_a[int(guess[1])] = "o"
                print_grid()
        if guess[0] == "B":
            if ai_grid_b2[int(guess[1])] == "x":
                print("Miss")
                ai_grid_b[int(guess[1])] = "x"
                players_turns = False
                print_grid()
            else:
                print("Hit")
                ai_grid_b[int(guess[1])] = "o"
                print_grid()
        if guess[0] == "C":
            if ai_grid_c3[int(guess[1])] == "x":
                print("Miss")
                ai_grid_c[int(guess[1])] = "x"
                players_turns = False
                print_grid()
            else:
                print("Hit")
                ai_grid_c[int(guess[1])] = "o"
                print_grid()
        if guess[0] == "D":
            if ai_grid_d4[int(guess[1])] == "x":
                print("Miss")
                ai_grid_d[int(guess[1])] = "x"
                players_turns = False
                print_grid()
            else:
                print("Hit")
                ai_grid_d[int(guess[1])] = "o"
                print_grid()
        if guess[0] == "E":
            if ai_grid_e5[int(guess[1])] == "x":
                print("Miss")
                ai_grid_e[int(guess[1])] = "x"
                players_turns = False
                print_grid()
            else:
                print("Hit")
                ai_grid_e[int(guess[1])] = "o"
                print_grid()
            
players_turn()

def ai_turn
