import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#1st option
random_friend_to_play_bill = random.randint(0,4)
print(friends[random_friend_to_play_bill])
#2nd option
print(random.choice(friends))