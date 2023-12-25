# Author > wasif_71 | Problem >  find the ball
import random


def main():
    cup_list = ['X', 'X', 'O']

    intro()
    i = 0
    while i < 3:
        guessing_num = taking_input()
        shuffled_cup_list = shuffle_cup(cup_list)
        print(win_lose(shuffled_cup_list, guessing_num))
        i += 1

    print("\n---------------------------\nThank You for Playing the Game\nAuthor - Wasif Hossain")

# giving introduction
def intro():
    print("""Find the ball within 3 Cups
    
    Guess The Glass index >> 1, 2, 3 <<
    If matches - you win
    If doesn't - you lose
    Total Round - 3
    ----------------------------------
    """)


# make a shuffle
def shuffle_cup(cup_list):
    random.shuffle(cup_list)
    return cup_list


# take guessing input
def taking_input():
    num = 0

    while num not in ['1', '2', '3']:
        num = input("\nEnter 1,2,3 -> ")
    return int(num)


# win or lose decision
def win_lose(shuffled_cup_list, guessing_num):
    print(shuffled_cup_list)
    if shuffled_cup_list[guessing_num - 1] == 'O':
        return "Congo -- You Win"
    else:
        return "You Lose -- Try Next Time"


main()
