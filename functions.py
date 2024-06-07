"""A collection of functions for doing my project."""
import string
import random
import nltk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#is it a question from A3
def is_question(input_string):
    """This function determines if a text string is a question.
    
    Parameters
    ----------
    input_string: string
        String to check to see if there is a question mark within the string. 
        
    Returns
    -------
    output: boolean
        Boolean telling if there is a question mark or not.
    """ 
    if '?' in input_string:
        output = True
    else:
        output = False
    return output


#removing punctuation from A3
def remove_punctuation(input_string):
    """This function removes the punctuation from a text string.
    
    Parameters
    ----------
    input_string: string
        String to check to see if any punctuation is contained within.
        
    Returns
    -------
    out_string: string
        same string as input but without any punctuation characters. 
    """ 
    out_string = ''
    
    for char in input_string:
        if char not in string.punctuation:
            out_string = out_string + char
        else:
            continue
    return out_string


#preparing input for processing from A3
def prepare_text(input_string):
    """Combines the lower method with the remove punctuation function to edit a text string.
   
    Parameters
    ----------
    input_string: string
        This string is run with the lower method and then checked to remove punctuation
        
    Returns
    -------
    out_list: list
        The words in the string are split to be different elements in a list.
    
    """ 
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split(' ')
    return out_list


#respond with an echo from A3
def respond_echo(input_string, number_of_echoes, spacer):
    """This function repeats the input string n times with x as a spacer.
    
    Parameters
    ----------
    input_string: string
        A string which will be repeated in the output
    number_of_echoes: int
        The number of times the input string will be repeated in the output
    spacer: string
        What will appear between the repetitions of the input string. 
        
    Returns
    -------
    echo_output: string
        A string with input_string repeated number_of_echoes times separated by spacer. 
    """ 
    if input_string != None:
        echo_output = (input_string + spacer) * number_of_echoes
    if input_string == None:
        echo_output = None
    return echo_output


#choose a response based on input from A3
def selector(input_list, check_list, return_list):
    """This function repeats the input string n times with x as a spacer.
    
    Parameters
    ----------
    input_list: list
        list of words
    check_list: list
        list of words to check for trigger words
    return_list: list
        list of possible responses. 
        
    Returns
    -------
    output: string
        selected with the random.choice method from return list.
    """ 
    output = None
    for element in input_list:
        if element in check_list:
            output = random.choice(return_list)
            return output
            break
    return output


#string concatenator from A3
def string_concatenator(string1, string2, separator):
    """Adds two strings together with a specifed separator
    
    Parameters
    ----------
    string1:string
        First string to add
    string2:string
        Second string added
    separator:string
        Added between string1 and string2
    Returns
    -------
    output:string
        all three input strings added together. 
    
    """ 
    output = string1 + separator + string2
    return output


#list into a string from A3
def list_to_string(input_list, separator):
    """Takes a list and converts it to a string using a specified separator
    
    Parameters
    ----------
    input_list:list
        Items in this list will be combined using string_concatenator function
    separator:string
        This string will serve as the separator in the string_concatenator function.   
    Returns
    -------
    output: string
        This string will be compiled of the elements in the input_list.
    """ 
    output = input_list[0]
    for element in input_list[1:]:
        output = string_concatenator(output, element, separator)

    return output
    
    
#end chat from A3
def end_chat(input_list):
    """This checks to see if the word quit is in a list
    
    Parameters
    ----------
    input_list: list
        This is a list of strings    
    Returns
    -------
    output: boolean
        This boolean will return True if 'quit' is in the list and false if it is not. 
    """ 
    if 'quit' in input_list:
        output = True
    else:
        output = False

    return output


#provided within assignemt
def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two.
    
    Parameters
    ----------
    list_one: list
       List with elements to be crossed checked for appearance in list_two
    list_two: list
       List to be looped through to see if elements from list_one appear.     
    Returns
    -------
    boolean
       returns True if items from list_one are in list_two and returns False otherwise.
    """ 
    for element in list_one:
        if element in list_two:
            return True

    return False


#provided within assignemt
def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise.
    
    Parameters
    ----------
    list_one: list
       List with elements to be crossed checked for appearance in list_two
    list_two: list
       List to be looped through to see if elements from list_one appear.
    Returns
    -------
    element: string
        This is returned if elements from list_one appear in list_two
    None
    """ 
    
    for element in list_one:
        if element in list_two:
            return element
        
    return None

def have_a_chat_sassy():
    """This function allows you to chat with a sassy chat bot.
    
    Parameters
    ----------
    class_instance: class instance
        You need to input the name of a class instance that has already been defined. 
    Returns
    -------
    output: string
        This function will return the output of a specific function already defined based on user input.
        It will also print the character image associated with the class instance each conversational 
        turn. 
    """ 
    
    #what sassy says
    GREETINGS_IN_SASSY = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
    GREETINGS_OUT_SASSY = ["Ugh, ew!", 'Oh... hey...',  "Wow! That outfit is SO brave!", "Oh... have we\
    met?"]

    TOPIC_IN_SASSY = ['boring', 'mean', 'nice', 'eye', ]
    TOPIC_OUT_SASSY = ["Ugh. Everything is sooOOOooo boring.",
                "Honestly I think being mean is kinda fun. Someone has to keep things interesting",
                "being nice is for losers. its honestly sooooo overrated.",
                "I once won a contest for how good I am at glaring."]

    BEAR_IN_SASSY = ['bear', 'grizzly', 'brown', 'polar', 'brown', 'black', 'cub']
    BEAR_OUT_SASSY = ["Did you know that Ursus arctos, the grizzly bear, is the Rocky Mountains’ largest\
    predator?", "Did you know that an individual grizzly bear can have a home range as large as 1,500\
    square miles?", "Did you know that a polar bear's hair is not white? It has no color! The strands\
    are thick, hollow, and reflect light.", "Did you know the sun bear is only bear native to South and\
    Southeast Asia?"]

    JOKES_IN_SASSY = ['funny', 'hilarious', 'ha', 'haha', 'hahaha', 'lol']
    JOKES_OUT_SASSY = ["wow... that's soooooo funny...", 'ha.', 'lol'] 

    NONO_IN_SASSY = ['class', 'food', 'car', 'morning']
    NONO_OUT_SASSY = ["Ugh you're still here? At least talk about something else."]

    UNKNOWN_SASSY = ['um no.', 'whatever you say...', 'ugh really?', 'just stop already',
                     'have you ever thought about not talking?']

    QUESTION_SASSY = "Are you serious? I am rolling my eyes at you."  
    
    #chat functionality, from A3
    chat = True
    while chat:
        msg = input('INPUT :\t')
        out_msg = None
        question = is_question(msg)
        msg = prepare_text(msg)
        class_instance = class_instance
        
        draw_bear(msg, class_instance)
            
        if end_chat(msg):
            out_msg = 'Ugh, finally! Good riddance.'
            chat = False

        if not out_msg:
            outs = []
            outs.append(selector(msg, GREETINGS_IN_SASSY, GREETINGS_OUT_SASSY))
            outs.append(selector(msg, TOPIC_IN_SASSY, TOPIC_OUT_SASSY))
            outs.append(selector(msg, BEAR_IN_SASSY, BEAR_OUT_SASSY))
            outs.append(respond_echo(selector(msg, JOKES_IN_SASSY, JOKES_OUT_SASSY), 1, ''))
          
            if is_in_list(msg, NONO_IN_SASSY):
                outs.append(selector(msg, NONO_IN_SASSY, NONO_OUT_SASSY))
            options = list(filter(None, outs))

            if options:
                out_msg = random.choice(options)

        if not out_msg and question:
            out_msg = QUESTION_SASSY

        if not out_msg:
            out_msg = random.choice(UNKNOWN_SASSY)

        print('OUTPUT:', out_msg)
        image = plt.imshow(class_instance.character_image)
        axis = plt.axis('off')
        plot = plt.show()    
    return image, axis, plot
        
def have_a_chat_sweet(class_instance):
    """This function allows you to chat with a sweet chat bot.
    
    Parameters
    ----------
    class_instance: class instance
        You need to input the name of a class instance that has already been defined. 
    Returns
    -------
    output: string
        This function will return the output of a specific function already defined based on user input.
        It will also print the character image associated with the class instance each conversational
        turn. 
    """ 
    #what sweet says
    GREETINGS_IN_SWEET = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
    GREETINGS_OUT_SWEET = ["Hello, it's so nice to meet you!", 'Hi! OMG! This is so exciting!', 
                           "I love talking to you!"]

    TOPIC_IN_SWEET = ['baking', 'cookies', 'garden', 'sun','flower','nature' ]
    TOPIC_OUT_SWEET = ["Do you want to bake something together?", 
                "There's nothing like a freshly baked chocolate chip cookie!", 
                "I love gardening. I grow lots of yummy food!",
                "I love sitting in the sunshine!"]

    BEAR_IN_SWEET = ['bear', 'grizzly', 'brown', 'polar', 'brown', 'black', 'cub']
    BEAR_OUT_SWEET = ["Did you know that Ursus arctos, the grizzly bear, is the Rocky Mountains’ largest\
    predator?","Did you know that an individual grizzly bear can have a home range as large as 1,500\
    square miles?", "Did you know that a polar bear's hair is not white? It has no color! The strands\
    are thick, hollow, and reflect light.", "Did you know the sun bear is only bear native to South\
    and Southeast Asia?"]

    JOKES_IN_SWEET = ['funny', 'hilarious', 'ha', 'haha', 'hahaha', 'lol']
    JOKES_OUT_SWEET = ["Wow! You're really clever!", 'HAHAHA', "You're too funny!"] 

    NONO_IN_SWEET = ['bad', 'mean', 'not nice']
    NONO_OUT_SWEET = ["I'm sorry, I don't want to talk about negative things :/"]

    UNKNOWN_SWEET = ['Nice!', 'Alright!', 'Oh, I see!', 'Yeah!', "You're so cool!"]

    QUESTION_SWEET = "Oh, sorry! I don't know the answer to that. What else do you want to talk about?"
    
    #chat functionality, from A3
    chat = True
    while chat:
        msg = input('INPUT :\t')
        out_msg = None
        question = is_question(msg)
        msg = prepare_text(msg)
        class_instance = class_instance
        
        if end_chat(msg):
            out_msg = 'Bye! It was so nice talking to you!'
            chat = False

        if not out_msg:
            outs = []
            outs.append(selector(msg, GREETINGS_IN_SWEET, GREETINGS_OUT_SWEET))
            outs.append(selector(msg, TOPIC_IN_SWEET, TOPIC_OUT_SWEET))
            outs.append(selector(msg, BEAR_IN_SWEET, BEAR_OUT_SWEET))
            outs.append(respond_echo(selector(msg, JOKES_IN_SWEET, JOKES_OUT_SWEET), 1, ''))

            if is_in_list(msg, NONO_IN_SWEET):
                outs.append(selector(msg, NONO_IN_SWEET, NONO_OUT_SWEET))
            options = list(filter(None, outs))

            if options:
                out_msg = random.choice(options)

        if not out_msg and question:
            out_msg = QUESTION_SWEET

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN_SWEET)
            
        print('OUTPUT:', out_msg)
        image = plt.imshow(class_instance.character_image)
        axis = plt.axis('off')
        plot = plt.show()    
    return image, axis, plot
    
    
def have_a_chat_bro(class_instance):
    """This function allows you to chat with a bro chat bot.
    
    Parameters
    ----------
    class_instance: class instance
        You need to input the name of a class instance that has already been defined. 
    Returns
    -------
    output: string
        This function will return the output of a specific function already defined based on user input.
        It will also print the character image associated with the class instance each conversational
        turn.
    """
     #what bro says
    GREETINGS_IN_BRO = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
    GREETINGS_OUT_BRO = ['duuude', 'sup', 'hey', 'brooo', 'whats good', 'aha-ha',]

    TOPIC_IN_BRO = ['gym', 'lift', 'beer-pong', 'sports']
    TOPIC_OUT_BRO = ["Shiiiiiit my pump is craaazyy rn bro", 
                "Did you know I lift? Do you even lift bro?", 
                "I am the beer-pong champ. No one beats my game",
                "Did you catch the game last night?"]

    BEAR_IN_BRO = ['bear', 'grizzly', 'brown', 'polar', 'brown', 'black', 'cub']
    BEAR_OUT_BRO = ["Did you know that Ursus arctos, the grizzly bear, is the Rocky Mountains’ largest\
    predator?","Did you know that an individual grizzly bear can have a home range as large as\
    1,500 square miles?", "Did you know that a polar bear's hair is not white? It has no color! The\
    strands are thick, hollow, and reflect light.", "Did you know the sun bear is only bear native to\
    South and Southeast Asia?"]

    JOKES_IN_BRO = ['funny', 'hilarious', 'ha', 'haha', 'hahaha', 'lol']
    JOKES_OUT_BRO = ['Aha-ha', 'Aha-ha shiiiit', 'thats pretty funny bro'] 

    NONO_IN_BRO = ['women', 'school', 'politics']
    NONO_OUT_BRO = ["um nahhh dude. can't talk about that."]

    UNKNOWN_BRO = ['I dont know about that bro', 'Thats fire', 'Huh?', 'Sorry Dude I was not listening',
                   'Aha-ha, shiiit']

    QUESTION_BRO = "woah what's with the interrogation? dude you dont need to be so pressed" 
    
    #chat functionality, from A3
    chat = True
    while chat:
        msg = input('INPUT :\t')
        out_msg = None
        question = is_question(msg)
        msg = prepare_text(msg)
   
        if not out_msg:
            outs = []
            outs.append(selector(msg, GREETINGS_IN_BRO, GREETINGS_OUT_BRO))
            outs.append(selector(msg, TOPIC_IN_BRO, TOPIC_OUT_BRO))
            outs.append(selector(msg, BEAR_IN_BRO, BEAR_OUT_BRO))
            outs.append(respond_echo(selector(msg, JOKES_IN_BRO, JOKES_OUT_BRO), 1, ''))

            if is_in_list(msg, NONO_IN_BRO):
                outs.append(selector(msg, NONO_IN_BRO, NONO_OUT_BRO))
            options = list(filter(None, outs))

            if options:
                out_msg = random.choice(options)

        if not out_msg and question:
            out_msg = QUESTION_BRO

        if not out_msg:
            out_msg = random.choice(UNKNOWN_BRO)

        print('OUTPUT:', out_msg)
        image = plt.imshow(class_instance.character_image)
        axis = plt.axis('off')
        plot = plt.show()    
    return image, axis, plot


def character_chat(class_instance):
    """This function allows you to chat with your character.
    
    Parameters
    ----------
    class_instance: class instance
        You need to input the name of a class instance that has already been defined. 
    
    Returns
    -------
    output: string
        This function will return the output of a specific function already defined based on user input.
        It will also print the character image associated with the class instance each conversational 
        turn.
    """
    
    #specification for which chat bot to select
    if class_instance.personality == 'sassy':
        have_a_chat_sassy(class_instance)
    
    elif class_instance.personality == 'sweet':
        have_a_chat_sweet(class_instance)
        
    elif class_instance.personality == 'bro':
        have_a_chat_bro(class_instance)
        
    else:
        print('Please try again. This is not an option.')
        class_instance.personality = ''
        return
    
    
    end_message = 'You have ended your chat with ' + class_instance.name + '.'

    return end_message


        
