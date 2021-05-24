# We will be creating an animal class

# We will then be creating a reptile class

# animal file to create Animal class

class Animal:

    # if you want to initilaise the class
    def __init__(self): # self refers to this class
         self.alive = True
         self.spine = True
         self.eyes = True
         self.lungs = True

    def breathe(self):
        return "Keep breathing to stay alive"

    def eat(self):
        return "nom nom nom nom"

    def move(self):
        return "moving all around the world! "

# if you want to use these functions within the class, we will need to create an object of our Animal class
# cat = Animal() # this is how we create an object of our Animal class called cat
# print(cat.breathe()) # breathing for cat is abstracted

# without creating an object (enstanciating) the class, you won't be able to call the method


