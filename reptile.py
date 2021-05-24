# creating a reptile class to Inherit everything Animal class

from animal import Animal # Question about random
# in these brackets
class Reptile(Animal):

    def __init__(self): #What does init mean
        # we have a keyword called super which inherits everything from parent class at the time of initilaisation of this class
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None # because not all reptiles ae tetrapod # What do you mean by none
        self.heart_chabers = [3,4]

    def seek_heat(self):
        return "It's raining and windy, where is the sun?.... "

    def hunt(self):
        return "Keep hunting for food until you get it it"

    def use_venom(self):
        return "If I've got it I'm using it"

reptile_object = Reptile()

print("This function is from Reptile class: " + reptile_object.seek_heat())
print("This function is inherited from Animal class: " + reptile_object.cold_blooded()) # why does it not work for eat?
# This the amazing benefits of using OOP and

# what is the difference between a function and a method
