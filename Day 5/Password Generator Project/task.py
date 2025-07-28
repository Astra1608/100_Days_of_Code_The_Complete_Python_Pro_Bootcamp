import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#method 1
#newList = []
#for n1 in range(1,nr_letters+1):
#    n1 = random.choice(letters)
#    newList.append(n1)
#for n2 in range(1,nr_symbols+1):
#    n2 = random.choice(symbols)
#    newList.append(n2)
#for n3 in range(1,nr_numbers+1):
#    n3 = random.choice(numbers)
#    newList.append(n3)

#print("".join(newList))
#'''password = ""
#for char in range(0,nr_letters+1):
#    password+=random.choice(letters)
#for char in range(0,nr_symbols+1):
 #   password+=random.choice(symbols)
#for char in range(0,nr_numbers+1):
 #   password+=random.choice(numbers)

#print(password)'''

newList=[]
for char in range(0,nr_letters+1):
    newList.append(random.choice(letters))
for char in range(0,nr_symbols+1):
    newList.append(random.choice(symbols))
for char in range(0,nr_numbers+1):
    newList.append(random.choice(numbers))

print(newList)
random.shuffle(newList)
print(newList)

password=""
for char in newList:
    password+=char

print(f"Your password is : {password}")


#another step without using 46 to 48 line to print list as string
print(f"Your Password is : " + "".join(newList))








