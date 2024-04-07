my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1,15)

my_list.extend([50,60,70])

my_list.pop()

my_list.sort()
try:
    print("The index of 30 is: ",my_list.index(30))
except ValueError:
    print("30 is not in the list")