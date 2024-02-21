import random
from random import sample
import tkinter as tk


grid = []

#Choose difficulty
difficulty_mode = ["easy","medium","hard"]

for idx ,difficulties in enumerate(difficulty_mode):
    print("{}) {}".format(idx + 1, difficulties))

difficulty_choosen = int(input("Choose difficulty: "))

def range_grid(difficulty_choosen):    
    if difficulty_choosen == 1:
        grid_num = 100
        bomb_num = 10
    elif difficulty_choosen == 2:
        grid_num = 225
        bomb_num = 22
    elif difficulty_choosen == 3:
        grid_num = 400
        bomb_num = 40
    return (grid_num, bomb_num)

[grid_num, bomb_num] = range_grid(difficulty_choosen)

#Define grid and set random bombs
for x in range(0,grid_num):
    grid.append(x)

random_bombs = sample(grid , k = bomb_num)


def criar_botao(idx):
    botao = tk.Button(root, text=str(idx), width=5, height=2, command=lambda i=idx: botao_clicado(i))
    botao.grid(row=idx // num_colls, column= idx % num_colls)

def botao_clicado(idx):
    print(f"Botão clicado: Index {idx}")


root = tk.Tk()
root.title("Minesweeper")

num_rows = int(grid_num ** (1/2))
num_colls = int(grid_num ** (1/2))
all_btn = num_rows * num_colls

for idx in range(all_btn):
    criar_botao(idx)

root.mainloop()





