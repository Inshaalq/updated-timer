"""This program contains the Nerve of Steel game
# Pseudocode below:
#1. Display the message "Players stand."
#2. Sleep for a random time between 5 to 25 seconds.
#3. During this time, players can choose to sit down.
#4. Once the sleep time is over, display the message "Times Up. Last to sit down wins."
#5. The players who remain standing are eliminated.
#6. The last player to sit down is declared the winner.
"""


import time # The time library has a sleep function that will pause the script for a specifized amount of time
# from PIL import Image # the pillow library makes it easy to display images 
import random

# Line 17 to be included if want to include the image as well
# im = Image.open("times-up.jpeg")

def nerve_of_steel_game():

# Display the message "Players stand."
    print("Players stand")

    # Sleep for a random time between 5 to 25 seconds.
    sleep_time = random.randint(5, 25)
    time.sleep(sleep_time)

    # Once the sleep time is over, display the message "Times Up. Last to sit down wins."
    print("Times Up. Last to sit down wins.")
    
# Line 32 to be included if want to include the image as well
   # im.show()

# Run the game
nerve_of_steel_game()
