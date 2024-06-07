"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
import string
import random
import nltk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from my_module.functions import is_question
from my_module.functions import remove_punctuation
from my_module.functions import prepare_text
from my_module.functions import respond_echo
from my_module.functions import selector
from my_module.functions import string_concatenator
from my_module.functions import list_to_string
from my_module.functions import end_chat
from my_module.functions import is_in_list
from my_module.functions import find_in_list
from my_module.functions import have_a_chat_sweet
from my_module.functions import have_a_chat_sassy
from my_module.functions import have_a_chat_bro
from my_module.functions import character_chat
from my_module.classes import MyCharacter
from my_module.functions import test_functions.py

#script for character examples

#Example of a character!
pooh = MyCharacter('pooh','sweet', 'brown', 'heart')
pooh.show_character()
pooh.introduction()

#Example of initializing a chat with your character!
character_chat(pooh)

pass
