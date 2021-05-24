# creating python class

from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = Flase

    def digest_large_prey(self):
        return "Yum yum yum..."

    def climb(self):
        return "up we go..."

    def shed_skin(self):
        return "Time to grow out of myself! "

python_object = Python()
dog_object = Python()
#print(" This climb function is from python class " + python_object.climb())
#print("This function is from snake class " + python_object.forked_tongue)