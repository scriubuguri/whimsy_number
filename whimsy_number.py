#!/usr/bin/env python
#this is a guessing game

import random
import time 

def print_welcome_animation(message, delay=0.05):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def whimsy_number():
    scores = 0
    player_name = input("What is your name? ")
    print(f"Hello, {player_name}! Nice to see you!")
    player_input = input("Do you want to play the Whimsy Number Game? (y/n)")

    if player_input == "y":
        print("Great! Let's play!")
        print("I'm thinking of a number between 1 and 10. Can you guess it?")
    else:
        print("Ohh, okey.. See you next time XD")

    while player_input == "y":
        number = random.randint(1, 10)
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations, {player_name}! You guessed the whimsy number!")
            scores += 1
            player_input = input("Do you want to play again? (y/n)")
            print(f"Your score is {scores}")

        if scores > 2:
            print("Congratulations! You are now moving to the next level. Guess a number between 1 and 20.")
            new_number = random.randint(1, 20)
            new_guess = int(input("Enter your guess: "))
            if new_guess < new_number:
                print("Too low. Try again.")
            elif new_guess > new_number:
                print("Too high. Try again.")
            else:
                print(f"Congratulations, {player_name}! You guessed the whimsy number!")

while True:
    welcome_message = "Hello! Welcome to the Whimsy Number Game!"
    print_welcome_animation(welcome_message)
    whimsy_number() 
 
