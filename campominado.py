import random
from random import sample
import tkinter as tk

# BACK-END

grid = []
buttons = []
removed_buttons = []

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

win_list = [ele for ele in grid if ele not in random_bombs]

# Define button actions in game
def clicked_button(idx, event):
    if event.num == 1:
        if idx in random_bombs:
            root.destroy()
            lose_game()
        else:
            remove_button(idx)
            win_condition()
    elif event.num == 3:          
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

def count_bombs_around(idx):
    bombs_around = sum(1 for i in range(max(0, idx % num_colls - 1), min(num_colls, idx % num_colls + 2))
                       for j in range(max(0, idx // num_colls - 1), min(num_rows, idx // num_colls + 2))
                       if i + j * num_colls in random_bombs)

    return bombs_around

def reveal_zeros(idx):
    global removed_buttons
    for i in range(max(0, idx % num_colls - 1), min(num_colls, idx % num_colls + 2)):
        for j in range(max(0, idx // num_colls - 1), min(num_rows, idx // num_colls + 2)):
            neighbor_idx = i + j * num_colls
            if neighbor_idx != idx and buttons[neighbor_idx]["state"] == "normal":
                bombs_around = count_bombs_around(neighbor_idx)
                buttons[neighbor_idx].grid_forget()
                label = tk.Label(root, text=str(bombs_around), width=5, height=2)
                label.grid(row=neighbor_idx // num_colls, column=neighbor_idx % num_colls)
                buttons[neighbor_idx] = label
                buttons[neighbor_idx].config(state="disabled")
                if bombs_around == 0:
                    reveal_zeros(neighbor_idx)
                removed_buttons.append(neighbor_idx)

def remove_button(idx):
    global removed_buttons
    bombs_around = count_bombs_around(idx)
    buttons[idx].grid_forget()
    label = tk.Label(root, text=str(bombs_around), width=5, height=2)
    label.grid(row=idx // num_colls, column=idx % num_colls)
    buttons[idx] = label
    buttons[idx].config(state="disabled")

    if bombs_around == 0:
        reveal_zeros(idx)
    removed_buttons.append(idx)

def win_condition ():
    global removed_buttons
    global win_list
    if sorted(removed_buttons) == sorted(win_list):
        win_game()
    else:
        pass

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

def win_game():
    root3 = tk.Tk()
    root3.title("")
    root3.geometry("225x200")
    win_lable = tk.Label(root3, text="Congratulation I've won the game!").place(x=20,y=70)
    quit_button = tk.Button(root3, text="   QUIT    ", command= lambda: root3.destroy() ).place(x=81,y=120)

    root3.mainloop()

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





