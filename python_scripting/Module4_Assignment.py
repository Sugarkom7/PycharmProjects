
#1. Write a Python function to find the Max of three numbers.
# x = [1874, 4567, 3901]
# print(max(x))


#2. Write a Python program to reverse a string.
# y = "God is good!"
# print(y[::-1])


#3. Write a Python function that takes a number as a parameter and check the number is prime or not.


# def prime_number(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#         return True
# number = int(input("The number is: "))
# print(prime_number(number))


# 4. What is the output of the below program ?
# x = 50
# def func(x):
#  print('x is', x)
#  x = 2
#  print('Changed local x to', x)
# func(x)
# print('x is now', x)
#Answer:
# x is 50
# change local variable to 2
# x is now 50. x being a global variable, it will remain unchanged.


#5. What is the output of the following code?
# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)
#Answer: The output will be 2 because of the finally block


# 6. What is the output of the following code?
# class test:
#     def __init__(self,a="Hello World"):
#             self.a = a
#     def display(self):
#         print(self.a)
# obj=test() Creating an instance for the class test.
# obj.display() Calling the display method.
#Answer: The output will be Hello World
# Module 4- Functions, OOPs and Exception Handling


# 7. What is the output of the following piece of code?
# class Stud:
#     def __init__(self, roll_no, grade):
#         self.roll_no = roll_no
#         self.grade = grade
#     def display (self):
#         print("Roll no : ", self.roll_no, ", Grade: ", self.grade)
# stud1 = Stud(34, 'S')
# stud1.age=7
# print(hasattr(stud1, 'age'))
#Answer: I don't remember being taught hasattr() function from the class.
#SO i have to check google. the above output would be true because
#that function checks if an object has aa specific attribute i.e age.



# 8. Suppose B is a subclass of A, to invoke the __init__ method in A from B, what is
# the line of code you should write?
# class A():
#     def __init__(self):
#         print("print something")
# class B(A):
#     def __init__(self):
#         print("print something here too")
#The above question is confusing to me. Thanks



# 9. What is the output of the following code?
class Demo:
    def __init__(self):
        self.a = 1
        self.__b = 1
    def display(self):
        return self.__b
obj = Demo()
print(obj.a)
#Answer: This code will output 1 which belongs to a.
#Normally there suppose to be a return of the value of b but it's impossible
#because __b it's private.

# 10. What is the output of the code shown below?
# lst = [1, 2, 3]
# lst[3]
# a) NameError
# b) ValueError
# c) IndexError
# d) TypeError
#Answer: c)
