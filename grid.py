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

'''for i in range(4):
    ship_x = random.randint(1, 4)
    ship_y = random.randint(0, 5)
    player_ship_grid[ship_x][ship_y] = "o"
    player_ship_grid[ship_x+1][ship_y] = "o"
    player_ship_grid[ship_x][ship_y+1] = "o"
    
print(player_ship_grid)'''

import tkinter as tk
win = tk.Tk() #context

win.geometry("500x500")

tk.Label(win, text = "BattleShip").place(x = 210, y = 0)

ai_grid_a1 = tk.Button(win, text = " O ").place(x=175 , y = 50)
ai_grid_a2 = tk.Button(win, text = " O ").place(x=200 , y = 50)
ai_grid_a3 = tk.Button(win, text = " O ").place(x=225 , y = 50)
ai_grid_a4 = tk.Button(win, text = " O ").place(x=250 , y = 50)
ai_grid_a5 = tk.Button(win, text = " O ").place(x=275 , y = 50)
ai_grid_b1 = tk.Button(win, text = " O ").place(x=175 , y = 75)
ai_grid_b2 = tk.Button(win, text = " O ").place(x=200 , y = 75)
ai_grid_b3= tk.Button(win, text = " O ").place(x=225 , y = 75)
ai_grid_b4 = tk.Button(win, text = " O ").place(x=250 , y = 75)
ai_grid_b5 = tk.Button(win, text = " O ").place(x=275 , y = 75)
ai_grid_c1 = tk.Button(win, text = " O ").place(x=175 , y = 100)
ai_grid_c2 = tk.Button(win, text = " O ").place(x=200 , y = 100)
ai_grid_c3 = tk.Button(win, text = " O ").place(x=225 , y = 100)
ai_grid_c4 = tk.Button(win, text = " O ").place(x=250 , y = 100)
ai_grid_c5 = tk.Button(win, text = " O ").place(x=275 , y = 100)
ai_grid_d1 = tk.Button(win, text = " O ").place(x=175 , y = 125)
ai_grid_d2 = tk.Button(win, text = " O ").place(x=200 , y = 125)
ai_grid_d3 = tk.Button(win, text = " O ").place(x=225 , y = 125)
ai_grid_d4 = tk.Button(win, text = " O ").place(x=250 , y = 125)
ai_grid_d5 = tk.Button(win, text = " O ").place(x=275, y = 125)
ai_grid_e1 = tk.Button(win, text = " O ").place(x=175 , y = 150)
ai_grid_e2 = tk.Button(win, text = " O ").place(x=200 , y = 150)
ai_grid_e3 = tk.Button(win, text = " O ").place(x=225 , y = 150)
ai_grid_e4 = tk.Button(win, text = " O ").place(x=250 , y = 150)
ai_grid_e5 = tk.Button(win, text = " O ").place(x=275 , y = 150)


player_grid_a1 = tk.Button(win, text = " O ").place(x=175 , y = 250)
player_grid_a2 = tk.Button(win, text = " O ").place(x=200 , y = 250)
player_grid_a3 = tk.Button(win, text = " O ").place(x=225 , y = 250)
player_grid_a4 = tk.Button(win, text = " O ").place(x=250 , y = 250)
player_grid_a5 = tk.Button(win, text = " O ").place(x=275 , y = 250)
player_grid_b1 = tk.Button(win, text = " O ").place(x=175 , y = 275)
player_grid_b2 = tk.Button(win, text = " O ").place(x=200 , y = 275)
player_grid_b3 = tk.Button(win, text = " O ").place(x=225 , y = 275)
player_grid_b4 = tk.Button(win, text = " O ").place(x=250 , y = 275)
player_grid_b5 = tk.Button(win, text = " O ").place(x=275 , y = 275)
player_grid_c1 = tk.Button(win, text = " O ").place(x=175 , y = 300)
player_grid_c2 = tk.Button(win, text = " O ").place(x=200 , y = 300)
player_grid_c3 = tk.Button(win, text = " O ").place(x=225 , y = 300)
player_grid_c4 = tk.Button(win, text = " O ").place(x=250 , y = 300)
player_grid_c5 = tk.Button(win, text = " O ").place(x=275 , y = 300)
player_grid_d1 = tk.Button(win, text = " O ").place(x=175 , y = 325)
player_grid_d2 = tk.Button(win, text = " O ").place(x=200 , y = 325)
player_grid_d3 = tk.Button(win, text = " O ").place(x=225 , y = 325)
player_grid_d4 = tk.Button(win, text = " O ").place(x=250 , y = 325)
player_grid_d5 = tk.Button(win, text = " O ").place(x=275 , y = 325)
player_grid_e1 = tk.Button(win, text = " O ").place(x=175 , y = 350)
player_grid_e2 = tk.Button(win, text = " O ").place(x=200 , y = 350)
player_grid_e3 = tk.Button(win, text = " O ").place(x=225 , y = 350)
player_grid_e4 = tk.Button(win, text = " O ").place(x=250 , y = 350)
player_grid_e5 = tk.Button(win, text = " O ").place(x=275 , y = 350)

win.mainloop()

