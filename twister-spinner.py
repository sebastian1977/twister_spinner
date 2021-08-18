'''
To choose random position from list use random.choice() or just import 'choice' from random module and then use choice(name_of_list)
'''
from os import system
from random import choice
system('cls')
colors_list = ['red', 'green', 'blue', 'yellow']
limb_list = ['left hand', 'right hand', 'left foot', 'right foot']
color_choice = choice(colors_list) # will choice a random pos. from colors_list and assign to color_choice variable
limb_choice = choice(limb_list)
print(f'Put your {limb_choice} on {color_choice} color.')