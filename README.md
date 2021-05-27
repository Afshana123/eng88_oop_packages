# Python OOP's 

---

OOP (Object oriented programming) is a way of programming that focuses on using objects and classes to design and build applications. There are 4 pillars of OOP:
 
- Inheritance 
- Abstraction
- Encapsulation
- Polymorphism

## Abstraction

---
To abstract something means to hide away the details inside something. For example, when we are calling a function

It is essentially like the saying 'what you see is what you get' - you do not need to know what's going on behind the scenes

## Inheritance 

---

Inheritance lets one object acquire the properties and methods of another class 

You can derive classes from a base class 

The benefit of inheritance is that it prevents code duplications meaning you do not have to repeat a code

For example, 

if we created a class called person and in the person's class, we created variables such as the name, DOB, address and gender. We basically have inherited all those things meaning we don't need to rewrite the information again.

When we want to create, you import person from person. Then you can create a separate class

You can inherit a child class from a parent class
  
## Encapsulation 

---

This is removing access of part of your code and making it private.

You can hide data from the user in situations where you would like to restrict information.

For example, in a bank where only the user can see their own information

You do this by putting an underscore to make it private e.g:
__dob = 01/01/1991

It is available but not accessible unless you are authorised to do so.



## Polymorphism 

---

Polymorphism means many forms. 

This is when you would like create more functionalities 
You're not changing anything in the parent class, but inheriting more to put into parent class 

Phrases for classes: 
- Super class, base Class, parent class all mean the same thing. 
- Child class is inheriting from the above.

Once you have inherited everything from the previous class, you can override particular attributes or behaviours without affecting the superclass.

## Animal Class Exercise 

```python
# We will be creating an animal class
# The behaviours are all the methods
# The attributes are variables
# We will then be creating a reptile class which will inherit from the animal class

# Animal > Reptile > Snake > Python
# Inheritance > Abstract > Encapsulate > Override

# animal file to create Animal class
# class name must start with a capital letter

# class Animal:
#     pass

# You can write the keyword pass if you don't want to create any functionalities at the time

class Animal:

    # if you want to initialise the class
    def __init__(self): # self refers to the current class
        # You create your variables
        # In a normal circumstance, you would create the variables as normal e.g alive = True but when you are dealing with classes, you need to add self.
         self.alive = True
         self.spine = True
         self.eyes = True
         self.lungs = True

    def breathe(self):
        return "Keep breathing to stay alive."

    def eat(self):
        return "nom nom nom nom"

    def move(self):
        return "Moving all around the world! "

# Nothing will be printed until you call the functions
# If you want to use these method functions within the class, we will need to create an object of our Animal class

cat = Animal() # This is how we create an object of our Animal class called cat

print(cat.breathe()) # breathing for cat is abstracted

# Without creating an object (instantiating) the class, you won't be able to call the methods
```


