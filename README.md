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

Inheritances lets one object aquire the properties and methods of another class 

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


## Polymorphism 

--- 
This is when you would like create more functionalities 
You're not changing anything in the parent class, but inheriting more to put into parent class 

Phrases for classes: Super Class, Base Class, Parent Class, Child Class


- OOP Task 1
```python

# Created a simple calculator class first:

class Simple_calc:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def divide(self, value1, value2):
        return value1/value2

    def multiply(self, value1, value2):
        return value1 * value2

# create an object for this class

calc_object = Simple_calc()

# call the function

# print(calc_object.add(2,5))

```

```python
# Created a functional calculator class and then created an object to call and print from both simple calculator class and functional calculator class:

from oop_calc_task import Simple_calc

class Function_calc(Simple_calc):

    def __init__(self):
        super().__init__()

    def is_number_divisible(self, value1, value2):
        if value1 % value2 == 0:
            return True
        else:
            return False

    def area_of_triangle(self, height, base):
        return 1 / 2 * base * height * 2.54

fun_object = Function_calc()

# print statements for all the functions available in parents class as well as this(child) class
print(fun_object.is_number_divisible(20,5))
print(fun_object.is_number_divisible(7,2))
print(fun_object.area_of_triangle(5,2))
print(fun_object.add(5,2))
print(fun_object.subtract(10,3))
print(fun_object.divide(15,3))
print(fun_object.multiply(4,2))
```
