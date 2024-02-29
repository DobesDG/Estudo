import random
from random import sample
import tkinter as tk

# BACK-END Game Diffulty

grid = []
buttons = []
removed_buttons = []
difficulty_choosen = int()

# Set difficulty buttons action
def set_easy_difficulty():
    global difficulty_choosen
    difficulty_choosen = 1
    diff_root.destroy()

def set_medium_difficulty():
    global difficulty_choosen
    difficulty_choosen = 2
    diff_root.destroy()

def set_hard_difficulty():
    global difficulty_choosen
    difficulty_choosen = 3
    diff_root.destroy()

# FRONT-END Game Diffulty
    
# Create difficulty choose interface
diff_root = tk.Tk()
diff_root.title("Minesweeper")
diff_root.geometry = "400x400"
diff_root.config(bg="Lavenderblush4")
diff_root.iconbitmap("./mineicon.ico")
diff_label = tk.Label(diff_root,
                          text= "Choose Difficulty",
                          bg="Lavenderblush4",
                          fg="black",
                          font="Arial 15 bold").place(x=17,y=0)
easy_btn = tk.Button(diff_root,
                         text= "EASY",
                         command= set_easy_difficulty,
                         font="Segoe 10 bold",
                         fg="green",
                         bg="palegreen2",
                         borderwidth = 5,
                         width= 20,
                         height=2).place(x=13,y=35)
medium_btn = tk.Button(diff_root,
                         text= "MEDIUM",
                         command= set_medium_difficulty,
                         font="Segoe 10 bold",
                         fg="goldenrod3",
                         bg="#ffff4d" ,
                         borderwidth = 5,
                         width= 20, 
                         height=2).place(x=13,y=90)
hard_btn = tk.Button(diff_root,
                         text= "HARD",
                         command= set_hard_difficulty,
                         font="Segoe 10 bold",
                         fg="red4",
                         bg="firebrick1",
                         borderwidth = 5,
                         width= 20, 
                         height=2).place(x=13,y=145)
diff_root.mainloop()

# BACK-END Game 

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

# Define text as flag and create flag counter      
flag_count = 0
def flag(idx):
    current_text = buttons[idx]["text"]
    global flag_count
    if current_text == "🚩":
        buttons[idx].config(text="")  # Return text to original text
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

# Create and show all cells in grid with no bombs nearby the clicked button
def reveal_zeros(idx):
    global removed_buttons
    for i in range(max(0, idx % num_colls - 1), min(num_colls, idx % num_colls + 2)):
        for j in range(max(0, idx // num_colls - 1), min(num_rows, idx // num_colls + 2)):
            neighbor_idx = i + j * num_colls
            if neighbor_idx != idx and buttons[neighbor_idx]["state"] == "normal":
                bombs_around = count_bombs_around(neighbor_idx)
                buttons[neighbor_idx].grid_forget()
                label = tk.Label(root, 
                                 text=str(bombs_around),
                                 font="Segoe 9 bold", 
                                 width=5, 
                                 height=2)
                label.grid(row=neighbor_idx // num_colls, column=neighbor_idx % num_colls)
                buttons[neighbor_idx] = label
                buttons[neighbor_idx].config(state="disabled")
                if bombs_around == 0:
                    reveal_zeros(neighbor_idx)
                removed_buttons.append(neighbor_idx)

# Remove buttons e create labels with numbers of bombs nearby
def remove_button(idx):
    global removed_buttons
    bombs_around = count_bombs_around(idx)
    buttons[idx].grid_forget()
    label = tk.Label(root, 
                     text=str(bombs_around),
                     font="Segoe 9 bold", 
                     fg= "red",
                     width=5, 
                     height=2)
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

# FRONT-END Game

# Create buttons in grid
def create_button(idx):
    button = tk.Button(root, 
                       text="", 
                       width=5, 
                       height=2)
    button.grid(row=idx // num_colls, column= idx % num_colls)
    button.bind("<Button-1>", lambda event, i=idx: clicked_button(i, event))
    button.bind("<Button-3>", lambda event, i=idx: clicked_button(i, event))
    buttons.append(button)

# Create a lose game interface
def lose_game():
    root2 = tk.Tk()
    root2.title("You lose!")
    root2.geometry("225x200")
    root2.iconbitmap("./mineicon.ico")
    root2.config(bg="brown1",)
    lose_lable = tk.Label(root2, 
                          text="BOOM!\n💣💥💣💥💣",
                          font="HELVETICA 18 bold",
                          fg="red4",
                          bg="brown1",).place(x=45,y=30)
    quit_button = tk.Button(root2, 
                            text="   QUIT    ", 
                            font="Segoe 9 bold",
                            bg="red",
                            fg="white",
                            command= lambda: root2.destroy() ).place(x=81,y=120)

    root2.mainloop()

# Create a win game interface
def win_game():
    root3 = tk.Tk()
    root3.title("You won!")
    root3.geometry("225x200")
    root3.iconbitmap("./mineicon.ico")
    root3.config(bg="palegreen2")
    win_lable = tk.Label(root3, 
                         text="Congratulations,\nYou've won the game!",
                         font="HELVETICA 13 bold",
                         fg="green",
                         bg="palegreen2",).place(x=23,y=50)
    quit_button = tk.Button(root3, 
                            text="   QUIT    ",
                            font="Segoe 9 bold",
                            bg="red",
                            fg="white",
                            borderwidth=4,
                            command= lambda: root3.destroy() ).place(x=81,y=120)

    root3.mainloop()

# Set grid rows and collumns for game interface
num_rows = int(grid_num ** (1/2))
num_colls = int(grid_num ** (1/2))
all_btn = num_rows * num_colls

# Create game interface 
root = tk.Tk()
root.title("Minesweeper")
root.iconbitmap("./mineicon.ico")
for idx in range(all_btn):
    create_button(idx)

flags_label = tk.Label(root, 
                       text=f"Bombs Remaing: {bomb_num-flag_count}")
flags_label.grid(row=num_colls, columnspan=num_colls)

root.mainloop()





