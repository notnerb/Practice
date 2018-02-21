

num = input("enter number check: ")
remainder = int(num) % 2
if remainder == 0:
    print("Your number is even squarer than you\n")
else:
    print("It's odd, goofball\n")


x = 'abc_%(hup)asdasdasd_'
x = x.replace('a', 'value')
#x %= {'hup':'value'}#
print(x)
#looks like I have to find and replace %(key)

#the cool thing about lists in Python is that you can have a list that contains objects of multiple types.
# Your list can mix between strings, integers, objects, other lists, what have you.

grade = int(input("Enter your grade:\n"))
if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 65:
  print("D")
else:
  print("F")

#In Python, lists are also iterables, which means you can loop through them with a for loop in a convenient way.
# (If you come from other languages like C++ or Java you are most likely used to using a counter to loop through indices of a list
# - in Python you can actually loop through the elements.)