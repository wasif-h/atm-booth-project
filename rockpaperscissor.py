# Rock Paper Scissor Game - made by Wasif
import random


def rps():
    # this function will generate a random selection of r,p,s
    list1 = ['r', 'p', 's']
    rand_rps = random.randint(0, 2)
    return list1[rand_rps]


# dictionary for r,p,s
dict = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissor'
}

i = 1
# it will run until anyone enter 'x'
while True:
    print(f"\n< ------ Round {i} ------ >")
    i += 1

    print("Rock Paper Scissor Game\nEnter { r - rock | p - paper | s - scissor }")
    print("To Exit the Game - Enter x\n============================")

    # input and output section
    rps_in = input("---> ")
    rps_rand = rps()
    if rps_in == 'x':
        break
    elif rps_in in ['r', 'p', 's']:

        print(f"You have selected {dict[rps_in]}\nComputer has selected {dict[rps_rand]}\n")

        # deciding win or lose
        if rps_in == rps_rand:
            print("Draw")
        elif rps_in == 'r' and rps_rand == 'p':
            print("You Lose\nRock is wrapped by paper")
        elif rps_in == 'r' and rps_rand == 's':
            print("You Win\nRock destroyed Scissor")
        elif rps_in == 'p' and rps_rand == 'r':
            print("You Win\nRock is wrapped by paper")
        elif rps_in == 'p' and rps_rand == 's':
            print("You Lose\nScissor cut paper")
        elif rps_in == 's' and rps_rand == 'p':
            print("You Win\nScissor cut paper")
        elif rps_in == 's' and rps_rand == 'r':
            print("You Lose\nRock destroyed Scissor")
    else:
        print("x x x x x Invalid Entry, Try again x x x x ")

print()

# It will appear after pressing x
print("Thank you for playing the Game\nAuthor - Md. Wasif Hossain")
