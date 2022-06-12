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
#the grid above is the one the player will see
ai_grid_a1 = ["x","x","x","x","x","x"]
ai_grid_b2 = ["x","x","x","x","x","x"]
ai_grid_c3 = ["x","x","x","x","x","x"]
ai_grid_d4 = ["x","x","x","x","x","x"]
ai_grid_e5 = ["x","x","x","x","x","x"]
#this one is what the computer will work with a compare

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

#just random places for 0 which is the ship
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


#function so I dont have to call each list
def print_grid_ia():
    print(" ")
    print("---------IA Grid---------")
    print(ai_grid_a)
    print(ai_grid_b)
    print(ai_grid_c)
    print(ai_grid_d)
    print(ai_grid_e)

def print_grid_player():
    print(" ")
    print("---------Players Grid---------")
    print(player_grid_a)
    print(player_grid_b)
    print(player_grid_c)
    print(player_grid_d)
    print(player_grid_e)

print_grid_ia()

#checks the inputs takes to information the first int is the row and second is the column and multiple if statements to find the location to see if there is a ship, also asks until it misses
def players_turn():
    players_turns = True
    global ai_hit_check
    ai_hit_check = 0
    while players_turns is True:
        guess = input("Guess: ")
        if len(guess) != 2:
            print("Your Guess must be 2")
        if guess[0] == "A":
            if ai_grid_a1[int(guess[1])] == "x":
                print("Miss")
                ai_grid_a[int(guess[1])] = "x"
                players_turns = False
                print_grid_ia()
            else:
                print("Hit")
                ai_hit_check += 1
                ai_grid_a[int(guess[1])] = "o"
                print_grid_ia()
        if guess[0] == "B":
            if ai_grid_b2[int(guess[1])] == "x":
                print("Miss")
                ai_grid_b[int(guess[1])] = "x"
                players_turns = False
                print_grid_ia()
            else:
                print("Hit")
                ai_hit_check += 1
                ai_grid_b[int(guess[1])] = "o"
                print_grid_ia()
        if guess[0] == "C":
            if ai_grid_c3[int(guess[1])] == "x":
                print("Miss")
                ai_grid_c[int(guess[1])] = "x"
                players_turns = False
                print_grid_ia()
            else:
                print("Hit")
                ai_hit_check += 1
                ai_grid_c[int(guess[1])] = "o"
                print_grid_ia()
        if guess[0] == "D":
            if ai_grid_d4[int(guess[1])] == "x":
                print("Miss")
                ai_grid_d[int(guess[1])] = "x"
                players_turns = False
                print_grid_ia()
            else:
                print("Hit")
                ai_hit_check += 1
                ai_grid_d[int(guess[1])] = "o"
                print_grid_ia()
        if guess[0] == "E":
            if ai_grid_e5[int(guess[1])] == "x":
                print("Miss")
                ai_grid_e[int(guess[1])] = "x"
                players_turns = False
                print_grid_ia()
            else:
                print("Hit")
                ai_hit_check += 1
                ai_grid_e[int(guess[1])] = "o"
                print_grid_ia()
            
def ai_turn():
    ai_turn = True
    global player_hit_check
    player_hit_check = 0
    while ai_turn is True:
        row = random.randint(0,4)
        column = random.randint(0,4)
        if row == 0:
            if player_grid_a1[column] == "x":
                print("Miss")
                player_grid_a[column] = "x"
                ai_turn = False
                print_grid_player()
            else:
                print("Hit")
                player_hit_check += 1
                player_grid_a[column] = "o"
                print_grid_player()
        elif row == 1:
            if player_grid_b2[column] == "x":
                print("Miss")
                player_grid_b[column] = "x"
                ai_turn = False
                print_grid_player()
            else:
                print("Hit")
                player_hit_check += 1
                player_grid_b[column] = "o"
                print_grid_player()
        elif row == 0:
            if player_grid_c3[column] == "x":
                print("Miss")
                player_grid_c[column] = "x"
                ai_turn = False
                print_grid_player()
            else:
                print("Hit")
                player_hit_check += 1
                player_grid_c[column] = "o"
                print_grid_player()
        elif row == 0:
            if player_grid_d4[column] == "x":
                print("Miss")
                player_grid_d[column] = "x"
                ai_turn = False
                print_grid_player()
            else:
                print("Hit")
                player_hit_check += 1
                player_grid_d[column] = "o"
                print_grid_player()
        elif row == 0:
            if player_grid_e5[column] == "x":
                print("Miss")
                player_grid_e[column] = "x"
                ai_turn = False
                print_grid_player()
            else:
                print("Hit")
                player_hit_check += 1
                player_grid_e[column] = "o"
                print_grid_player()


#I did it like this so it would check for 5 ships that was hit the reason I have two turns first is so the hit function can be created
players_turn()        
ai_turn()
game = True
while game is True:
    if player_hit_check == 5:
        print("YOU WIN!, GOOD WORK")
        game = False
    else:
        players_turn()
    if ai_hit_check == 5:
        print("YOU LOSE, Beter luck next time")
        game = False
    else:
        ai_turn()
