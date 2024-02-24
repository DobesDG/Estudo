import random
from random import sample
import tkinter as tk

# BACK-END

grid = []
buttons = []

# Choose difficulty
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

# Define grid and set random bombs
[grid_num, bomb_num] = range_grid(difficulty_choosen)

for x in range(0,grid_num):
    grid.append(x)

random_bombs = sample(grid , k = bomb_num)
print(random_bombs)

# Define button actions in game
def clicked_button(idx, event):
    if event.num == 1:
        if idx in random_bombs:
            root.destroy()
            lose_game()
            
        else:
            print(f"Botão esquerdo clicado: Index {idx}")
            remove_button(idx)
    elif event.num == 3:
        print(f"Botão Direito clicado: Index {idx}")          
        flag(idx)

# Define text as flag and Create flag counter      
flag_count = 0
def flag(idx):
    current_text = buttons[idx]["text"]
    global flag_count
    if current_text == "🚩":
        buttons[idx].config(text=str(idx))  # Return text to original text
        flag_count -= 1
    else:
        buttons[idx].config(text="🚩")  # Define text as flag
        flag_count += 1 
    update_flags_label()

def update_flags_label():
    flags_label.config(text=f"Bombs Remaing: {bomb_num-flag_count}")

def remove_button(idx):
    buttons[idx].grid_forget()
    label = tk.Label(root, text="", width=5, height=2)
    label.grid(row=idx // num_colls, column=idx % num_colls)
    buttons[idx] = label

# FRONT-END

# Create buttons in grid

def create_button(idx):
    button = tk.Button(root, text=str(idx), width=5, height=2)
    button.grid(row=idx // num_colls, column= idx % num_colls)
    button.bind("<Button-1>", lambda event, i=idx: clicked_button(i, event))
    button.bind("<Button-3>", lambda event, i=idx: clicked_button(i, event))
    buttons.append(button)

# Create a lose game interface
def lose_game():
    root2 = tk.Tk()
    root2.title("")
    lose_lable = tk.Label(root2, text="BOOM!").place(x=77,y=70)
    quit_button = tk.Button(root2, text="   QUIT    ", command= lambda: root2.destroy() ).place(x=70,y=120)

    root2.mainloop()

num_rows = int(grid_num ** (1/2))
num_colls = int(grid_num ** (1/2))
all_btn = num_rows * num_colls

# Create game interface 
root = tk.Tk()
root.title("Minesweeper")

for idx in range(all_btn):
    create_button(idx)

flags_label = tk.Label(root, text=f"Bombs Remaing: {bomb_num-flag_count}")
flags_label.grid(row=num_colls, columnspan=num_colls)

root.mainloop()





