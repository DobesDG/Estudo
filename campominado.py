import random

x = random.randrange(0,225)
grid = []

#Choose difficulty
difficulty_mode = ["easy","medium","hard"]

for idx ,difficulties in enumerate(difficulty_mode):
    print("{}) {}".format(idx + 1, difficulties))

difficulty_choosen = int(input("Choose difficulty: "))

def range_grid(difficulty_choosen):    
    if difficulty_choosen == 1:
        grid_num = 100
    elif difficulty_choosen == 2:
        grid_num = 625
    elif difficulty_choosen == 3:
        grid_num = 2500
    return grid_num

grid_num = range_grid(difficulty_choosen)


for x in range(0,grid_num):
    grid.append(x)

print(grid)


