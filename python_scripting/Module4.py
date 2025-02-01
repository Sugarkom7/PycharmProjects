"""
def students_name(name, age):
    name = name
    age = age
    print("The pupil", name, "is present")
    return

pupil1 = "John", 12
pupil2 = "Paul", 9
pupil3 = "Claude", 10

students_name(pupil1,12)
students_name(pupil2, 9)
students_name(pupil3, 10)



def calculus(ttl):
    print("the total is", ttl)
    return
x = 5
y = 4
ttl = x + y
print(calculus(ttl))



age = 50
def staff(name, age):
    name = name
    age = age
    print("Welcome to Alis Aquilae", name)
    return
staff1 = "Miracle", 45
staff2 = "Peter", 57
staff3 = "Christus", age

print(staff(staff1, age))
print(staff(staff2, age))
print(staff(staff3, age))



def people(user, *users):
    print("users of python: ")
    print(user)
    for var in users:
        print(var)
        return

print(people("Anna"))
print(people("Peter", "Chloe", "Lucas"))



class Edureka():
    def message(self):
        print("Learning Python is fun")

ob1 = Edureka()
ob1.message()



class Parents:
    def parents_methods(self, name, age):
        self.name = name
        self.age = age
        if age > 18:
            print("Access granted")


class Children(Parents):
    def children_way(self, name, age):
        self.name = name
        self.age = age
        if age < 18:
            print("Access denied")
        else:
            print("Access granted")


p1 = Parents()
p2 = Parents()
c1 = Children()
c2 = Children()
p1.parents_methods("John", 45)
c1.children_way("Paul", 10)
c2.children_way("Ben", 19)


#the following code is called polymorphism
class Animal:
    def __init__(self, name):
        self.name = name
        def talk(self):
            pass

class Cat(Animal):
    def talk(self):
        print("The cat mews")

class Dog(Animal):
        def talk(self):
            print("The dog barks")


C1 = Cat("Millie")
D1 = Dog("Charlie")
C1.talk()
D1.talk()

the next code is called keyboard reading
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(a**b)

a = str(input("Enter your name: "))
print("You are a good guy")
"""
# this is an f-string
# number = 10
# formatted_string = f"The number is {number}"
# print(formatted_string)


