from random import randint
from time import sleep
bank = int(input("How many money you have: "))
games_no = bank//3
change = bank % 3
print("You can play " + str(games_no) + " games, " + "take a change " + str(change) + " nis")
sleep(3)
total_prize = 0
for x in range(games_no):
    print("Game " + str(x+1) + " started ...")
    sleep(5)
    first_no = randint(1,6)
    second_no = randint(1,6)
    if first_no == second_no:
        if first_no < 6:
            print("Result: " + str(first_no) + " -:- " + str(second_no) + " ---> " + "You win 100 nis\n")
            total_prize = total_prize + 100
        elif first_no == 6:
            print("Result: " + str(first_no) + " -:- " + str(second_no) + " ---> " + "You win 1000 nis\n")
            total_prize = total_prize + 1000
    elif second_no == 2:
        print("Result: " + str(first_no) + " -:- " + str(second_no) + " ---> " + "You win 40 nis\n")
        total_prize = total_prize + 40
    elif first_no == 1:
        print("Result: " + str(first_no) + " -:- " + str(second_no) + " ---> " + "You win 20 nis\n")
        total_prize = total_prize + 20
    else:
        print("Result: " + str(first_no) + " -:- " + str(second_no) + " ---> " + "You loose\n")
print("Your total prize is: " + str(total_prize) + " nis")
