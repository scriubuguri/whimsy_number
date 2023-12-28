#!/usr/bin/env python
#this is a guessing game

import random

def whimsy_number():
    print("Hello there! Welcome to the Whimsy Number Game!")
    player_name = input("What is your name? ")
    print(f"Hello, {player_name}! Nice to see you!")
    player_input = input("Do you want to play the Whimsy Number Game? (y/n)")

    if player_input == "y":
        print("Great! Let's play!")
        print("I'm thinking of a number between 1 and 20. Can you guess it?")
    else:
        print("Ohh, okey! See you next time.")

    while player_input == "y":
        number = random.randint(1, 20)
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations, {player_name}! You guessed the whimsy number!")
            player_input = input("Do you want to play again? (y/n)")
    
    
whimsy_number() 
