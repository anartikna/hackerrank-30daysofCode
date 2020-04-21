'''
Objective
In this challenge, we're going to learn about the difference between a class and an instance; because this is an Object Oriented concept, it's only enabled in certain languages. Check out the Tutorial tab for learning materials and an instructional video!

Task
Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter. The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as , the constructor should set  to  and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:

yearPasses() should increase the  instance variable by .
amIOld() should perform the following conditional actions:
If , print You are young..
If  and , print You are a teenager..
Otherwise, print You are old..
To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. The code that creates each instance of your Person class is in the main method. Don't worry if you don't understand it all quite yet!

Note: Do not remove or alter the stub code in the editor.

Input Format

Input is handled for you by the stub code in the editor.

The first line contains an integer,  (the number of test cases), and the  subsequent lines each contain an integer denoting the  of a Person instance.

Constraints

Output Format

Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print  or  lines (depending on whether or not a valid  was passed to the constructor).
# $######################################### $########################################
Study material:
# $######################################### $########################################

A blueprint defining the charactaristics and behaviors of an object of that class type. Class names should be written in CamelCase, starting with a capital letter.
class MyClass{
    ...
}
Class Constructor
class Dog{ // class name
    static String unnamed = "I need a name!"; // class variable
    int weight; // instance variable
    String name; // instance variable
    String coatColor; // instance variable
    
    Dog(){ // default constructor
        this.weight = 0;
        this.name = unnamed;
        this.coatColor = "none";
    }
    Dog(int weight, String color){ // parameterized constructor
        // initialize instance variables
        this.weight = weight; // assign parameter's value to instance variable
        this.name = unnamed; 
        this.coatColor = color; 
    }
    Dog(String dogName, String color){ // overloaded parameterized constructor
        // initialize instance variables
        this.weight = 0;
        this.name = dogName; 
        this.coatColor = color; 
    }
}
A sort of named procedure associated with a class that performs a predefined action. In the sample code below, returnType will either be a data type or  if no value need be returned. Like a constructor, a method can have  or more parameters.

returnType methodName(parameterOne, ..., parameterN){
    ...
    return variableOfReturnType; // no return statement if void
}
Most classes will have methods called getters and setters that get (return) or set the values of its instance variables. Standard getter/setter syntax:

class MyClass{
    dataType instanceVariable;
    ...
    void setInstanceVariable(int value){
        this.instanceVariable = value;
    }
    dataType getInstanceVariable(){
        return instanceVariable;
    }
}
'''
class Person:
    def __init__(self,initialAge):
        if initialAge >=0:
            self.age = initialAge
        elif initialAge<0:
            self.age=0
            print('Age is not valid, setting age to 0.')
        
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.age <13:
            print('You are young.')
        elif self.age>=13 and self.age<18:
            print('You are a teenager.')
        else:
            print('You are old.')
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.age += 1
        # Increment the age of the person in here

t = int(input())
