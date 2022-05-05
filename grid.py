# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:40:13 2022

@author: XLHS
"""
import random

print("---------BATTLESHIP--------")

#if a ship is hit the x will become an o
player_grid = [["x","x","x","x","x","x"],
               ["x","x","x","x","x","x"],
               ["x","x","x","x","x","x"],
               ["x","x","x","x","x","x"],
               ["x","x","x","x","x","x"],
               ["x","x","x","x","x","x"],]

player_ship_grid = [["x","x","x","x","x","x"],
                    ["x","x","x","x","x","x"],
                    ["x","x","x","x","x","x"],
                    ["x","x","x","x","x","x"],
                    ["x","x","x","x","x","x"],
                    ["x","x","x","x","x","x"],]

ai_grid = [["x","x","x","x","x","x"],
           ["x","x","x","x","x","x"],
           ["x","x","x","x","x","x"],
           ["x","x","x","x","x","x"],
           ["x","x","x","x","x","x"],
           ["x","x","x","x","x","x"],]

ai_ship_grid = [["x","x","x","x","x","x"],
               ["x","x","x","x","x","x"],
               ["x","x","x","x","x","x"],
               ["x","x","x","x","x","x"],
               ["x","x","x","x","x","x"],
               ["x","x","x","x","x","x"],]

ship = random.randint(0, 5)

for i in range(4):
    ship_x = random.randint(1, 4)
    ship_y = random.randint(0, 5)
    player_ship_grid[ship_x][ship_y] = "o"
    player_ship_grid[ship_x+1][ship_y] = "o"
    player_ship_grid[ship_x][ship_y+1] = "o"
    
print(player_ship_grid)