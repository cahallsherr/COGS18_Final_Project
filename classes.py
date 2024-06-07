"""Classes used throughout project"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#each instance of an object of this class is a character.
class MyCharacter:
    """This class allows you to design a character using a single instance of the class
    Paramenters
    -----------
    self: self
    name: string
        User input string
    personality: string
        User input string
    color: string: string
        User input string
    pattern: string
        User input string
    Returns
    -------
    string
       This string is concatenated with predetermined text and user defined variables
    """
        
    def __init__(self, name, personality, color, pattern):
        self.name = name
        self.color = color
        self.pattern = pattern
        self.personality = personality
        
    #this will give you an image of your character with the correct specifications
    def show_character(self):
        if self.color == 'brown':
            if self.pattern == 'star': 
                self.character_image = mpimg.imread('images/brown_star.jpg')
            if self.pattern == 'heart': 
                self.character_image = mpimg.imread('images/brown_heart.jpg') 
            if self.pattern == 'none':
                self.character_image = mpimg.imread('images/brown_none.jpg')           
        elif self.color == 'polar':
            if self.pattern == 'star':
                self.character_image = mpimg.imread('images/polar_star.jpg')
            if self.pattern == 'heart':
                self.character_image = mpimg.imread('images/polar_heart.jpg')
            if self.pattern == 'none':
                self.character_image = mpimg.imread('images/polar_none.jpg')     
        elif self.color == 'black':
            if self.pattern == 'star':
                self.character_image = mpimg.imread('images/black_star.jpg')
            if self.pattern == 'heart':
                self.character_image = mpimg.imread('images/black_heart.jpg')
            if self.pattern == 'none':
                self.character_image = mpimg.imread('images/black_none.jpg') 
                
        image = plt.imshow(self.character_image)
        axis = plt.axis('off')
        plot = plt.show()
        text = 'This is your character!'
        return text, image, axis, plot
    
    #this allows the character to be introduced
    def introduction(self):
        output = 'Hi! My name is ' + self.name +'. I have a ' + self.personality + ' personality!'
        return output