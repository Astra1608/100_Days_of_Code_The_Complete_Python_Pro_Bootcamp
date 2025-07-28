print(r'''
               |
               |
              / \
             /___\       ~ You found the Treasure! ~
             \o o/
             ( ^ )        _____
             |||||       /     \
           __|||||__    / $$$$$ \
         .'  |||||  `.  | $$$$$ |
       _/    |||||    \ | $$$$$ |
      / \____|||||____/ \______/  
     /      /     \     \
    /      /       \     \
   |      /         \     |
   |     /           \    |
   |    /             \   |
   |___/               \__|

     ☀️  Sand, 🪙 Gold, 🌴 Tree… All Yours!
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
start = input("Type 'start' to begin the game")
step1 = str(input("You reach a fork in the jungle path: Type 'left' or 'right' "))
if step1== "left":
    print("You walk into the jungle and reach a river")
    step2 = str(input("Do you want to wait for a boat or swim?: Type 'wait' or 'swim'"))
    if step2== "wait":
        print("You build a raft and cross safely → reach island 🛶")
        step3 = str(input("a temple with 3 doors —Type 'red', 'blue' or 'gold' "))
        if step3== "gold":
            print("The treasure room! 🎉 You Win!")
        elif step3== "blue":
            print("Ice room. You freeze! Game Over ❄️")
        else:
            print("Fire trap! Game Over 🔥")
    else:
        print("Crocodile attack! Game Over 🐊")
else:
    print("You fall into quicksand → Game Over 🕳️")


