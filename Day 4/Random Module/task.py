import random
import my_module

random_integer = random.randint(1,10)
print(random_integer)
print(my_module.my_favourite_number)
random_number_0_to_1 = random.random() * 10
#0 inclusive 10 not clusive
# just as when we didnt multiply 10 --0 was inclusive but 1 wasnt
print(random_number_0_to_1)
#random.uniform(a,b) inclusive of a and b both
random_float = random.uniform(1,20)
#it is not sure whether it will give 20 or not
print(random_float)

#my heads and tails
coin = random.random()*20
if coin>10:
    print("Heads")
else:
    print("Tails")
#angela's head and tails program using randint
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails==0:
    print("Heads")
else:
    print("Tails")
