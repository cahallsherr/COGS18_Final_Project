"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""
import mock
import builtins 
import string
import random
import nltk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from functions import is_question
from functions import remove_punctuation
from functions import prepare_text
from functions import respond_echo
from functions import selector
from functions import string_concatenator
from functions import list_to_string
from functions import end_chat
from functions import is_in_list
from functions import find_in_list
from functions import have_a_chat_sweet
from functions import have_a_chat_sassy
from functions import have_a_chat_bro
from functions import character_chat
from classes import MyCharacter
##
##

#testing introduction method
def test_introduction():
    testchar = MyCharacter('testchar','sweet','brown','none')
    testing = testchar.introduction()
    assert type(testing) == str
    assert testing == 'Hi! My name is testchar. I have a sweet personality!'

#testing show_character method
def test_show_character():
    testchar = MyCharacter('testchar','sweet','brown','none')   
    assert callable(testchar.show_character)
    assert type(testchar.personality) == str
    assert testchar.color == 'brown'
    assert testchar.name == 'testchar'
    assert testchar.pattern == 'none'
    
#testing character_chat function
def test_character_chat():
    from classes import MyCharacter
    testchar = MyCharacter('testchar','fake','brown','none') 
    assert callable(character_chat)
    character_chat(testchar)
    assert testchar.personality == ''

    
    
    





