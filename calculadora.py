num1 = input("Enter number: ")
num2 = input("Enter another number: ")

def check_isfloat (num1,num2):
  if "." in num1 or "." in num2:
    return float(num1), float(num2)
  else:
    return int(num1), int(num2)

tipos = ["SUM","SUB","MUL","DIV"]
for idx, tipo in enumerate(tipos):
    print("{}) {}".format(idx + 1, tipo))

escolha = int(input("Choose option: "))
new_num1, new_num2 = check_isfloat(num1,num2)


if escolha == 1:
    print(new_num1+new_num2)

elif escolha == 2:
    print(new_num1-new_num2)

elif escolha == 3:
    print(round(new_num1*new_num2,2))

elif escolha == 4:
    print(round(new_num1/new_num2,2))

else:
    print("Invalid option")
    

 
