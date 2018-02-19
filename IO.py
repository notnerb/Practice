

num = input("enter number check: ")
remainder = int(num) % 2
if remainder == 0:
    print("Your number is even squarer than you")
else:
    print("It's odd, goofball")


x = 'abc_%(hup)asdasdasd_'
x = x.replace('a', 'value')
#x %= {'hup':'value'}#
print(x)
#looks like I have to find and replace %(key)

