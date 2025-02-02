#Variables and values
# x = "Hello World!" #x is the variable while "Hello World!" is the value
# print(x)

#Assigning a unique value to multiple variables
# x = y = z = 1
# print(x) #This output 1
# print(y) #This output 1 too

#Assigning multiple values to multiple variables
# a, b, c = 1, 2, 3 #this means a = 1, b = 2, c = 3
# print(a)
# print(b)
# print(c)

# My_list = [23, "Hi", 100, "tomato"]
# print(My_list)
# subjects = ["PHE", "Maths", "Science"] #Declaring a list.
# print(subjects)
# print(subjects[0]) #Indexing. 0 is the first object in the list so this will print PHE.
# print(subjects[:2]) #This is range 0 to 2 with 2 excluding.
# print(subjects[1][:3]) #Accessing the 2nd object & printing range 0 to 3 with 3 excluding.

#Mutating an object from the list.
# subjects[2] = "English"  #Changing Science with English
# print(subjects) #This will output ['PHE', 'Maths', 'English']

#Using another method to change an object from the list
# ingredients = ["oil", "tomato", "ginger"]
# ingredients[1] = ingredients[1].replace("tomato","curry")
# print(ingredients)

#Nested list
# salad_dressing = ["salad", ["lemon_juice"], ["olive_oil"]]
# print(salad_dressing[2])
# print(salad_dressing[1][0][6:]) #Explaining this code below
# salad_dressing[1] accesses the second element, which is the sublist ["lemon_juice"].
# salad_dressing[1][0] accesses the first (and only) element inside that sublist, which is the string "lemon_juice".
# So the [0] is necessary because salad_dressing[1] gives you a list (["lemon_juice"]), and we need to grab the actual string ("lemon_juice") inside that list. If you didn’t add [0], you would be dealing with a list rather than a string, and you wouldn’t be able to slice it to get "juice".
#
# In summary:
# salad_dressing[1] gives ["lemon_juice"] (a list).
# salad_dressing[1][0] gives "lemon_juice" (the string).
# [6:] slices the string to get "juice".

# print(salad_dressing[2][0][0:5]) #This outputs olive.
# print(salad_dressing[0][2:]) #This outputs lad.
#Mutating from a nested list
# salad_dressing[1] = "Oregano"  #Changing lemon_juice to Oregano
# salad_dressing[2][0] = salad_dressing[2][0].replace("olive_oil","olive_wood")
# print(salad_dressing)

#Using .append() to add 1 object to the list
# salad_dressing.append("olive_oil")
# print(salad_dressing)

#Using .append() to add multiple objects to a list
# fridge = ["wine", "bottle_water"]
# fridge.append("ice-cream")
# fridge.append("parfait")
# fridge.append("yoghurt")
# fridge.append("parfait")
# print(fridge)

#Using .extend([]) to add multiple objects to a list.
# salad_dressing.extend(["olive_oil", "leccino"])
# print(salad_dressing)

#Using .insert to append at a specific position
# wardrobe = ["shirt", "shoes"]
# wardrobe.insert(0, "scarf")
# print(wardrobe)

#Deleting an object from a list
# del wardrobe[2]
# print(wardrobe)

#removing an object from the list
# fridge.remove("ice-cream")
# print(fridge)
#deleting deals with the index while removing deals with the value.

#Using .remove() in a loop to delete multiple items from a list.
# fridge.remove("bottle_water")
# fridge.remove("yoghurt")
# print(fridge)

#Using list comprehension to delete multiple items from a list.
# fridge =[item for item in fridge if item not in ["wine", "ice-cream", "parfait"]]
# print(fridge)

# fridge =[x for x in fridge if x != "wine" and x != "ice-cream" and x != "parfait"]
# print(fridge)

#Using pop() to delete the last item if index is not provided.
# fridge.pop()
# print(fridge)

# fridge.pop(2)
# print(fridge)

#Using pop() to return the last item in the list if index isn't provide
#print(fridge.pop())
#print(fridge.pop(3))

#.clear is used to clear the content of the list.
# fridge.clear()
# print(fridge)

#del can be used to delete the entire list
# del fridge

#Use .reverse or ::-1 to reverse the contents of a list.
# fridge.reverse()
# print(fridge)
#print(fridge[::-1])

#Sorting a list in ascending or descending order
#If the value true or false is not specified, ascending order remains the default.
# fridge.sort()
# print(fridge) #Items are printed in alphabetical order(Ascending).

# fridge.sort(reverse = True)
# print(fridge) #Items are printed in descending order.
# #Another example with numbers
# age = [10, 20, 30, 40, 50]
# age.sort()
# print(age)
# age.sort(reverse = True)
# print(age)

#Using .index() to know the position of a value in a list.
# print(fridge.index("ice-cream"))

#Using .count() to print the number of time an item is mentioned in the list.
#print(fridge.count("parfait")) #Answer should be 2 bcos parfait is mentioned twice

#Checking attendance in a list
# if "bottle_wr" in fridge:
#     print("Yes, it is")
# else:
#     print("No it's not")

#Use for loop to run your code a number of times without a condition attached.
# dollar = [5, 10, 20, 50, 100]
# for i in dollar:
#     print(i)
#
# #Use while loop to run your code multiple time with a condition attached.
#Basic while loop.
# i = 1
# while i <= 5:
#     print(i)
#     i += 1


#while loop with else
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# else:
#     print("The loop is over")

#Using break to exit while loop
# i = 1
# # while True:
# #     if i > 5:
# #         break
# #     print(i)
# #     i += 1
#
# #Using continue to skip iteration.
# i = 1
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)









