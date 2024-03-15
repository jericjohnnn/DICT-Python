# this is a comment
# this is a comment

x = 300
y = 6


def add_twonumbers():
    sumz = x + y
    print(sumz)


add_twonumbers()


def greetings(name):
    print("Have a nice day " + name)
    

greetings("jamal")

print(10 > 7)
print(str(73911))
print(tuple("thank god its friday"))
print(float(4302))
print(int(3299.35640))


class NewClass:
    pass


class Pets:
    looks = "Adorable!"


hamster = Pets()
print(hamster.looks)


class Guest:
    pass


g_1 = Guest()

g_1.first = "jamal"
g_1.last = "murray"
g_1.phone = 948

print(g_1.phone)


class Customers:
    greeting = "Welcome to the Coffee Palace"


c_1 = Customers()
c_1.name = "Samirah"
c_1.beverage = "iced caffe latte"
c_1.food = "cinnamon roll"
c_1.total = "225"

c_2 = Customers()
c_2.name = "Jerry"
c_2.beverage = "caramel macchiato"
c_2.food = "glazed doughnut"
c_2.total = "230"

print(Customers.greeting)

print(c_1.beverage)
print(c_2.food)


if x > 350:
    print("hooyah")

furniture = ["table", "chair", "cabinet", "desk", "couch"]

for x in furniture:
    if x == "cabinet":
        continue
    print(x)


i = 1

while i <= 15:
    print(i)
    i += 1
else:
    print("i is no longer less than 15")


class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def printall(self):
        print(self.goal, self.favorite_food, self.birthday, self.age, self.name)


class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, favorite_food, goal, position):
        self.Position = position
        ClubMembers.__init__(self, name, birthday, age, favorite_food, goal)

    def printagain(self):
        print(self.Position, self.goal, self.favorite_food, self.birthday, self.age, self.name)


m_1 = ClubMembers("tome", "january 3, 2021", "14", "ice cream", "to be happy")
o_4 = ClubOfficers("vera", "jan 3 2313", "16", "beef stroganoff", "to be chef", "treasurer")

m_1.printall()
o_4.printagain()
print(o_4.Position)

flavor = ["vanilla", "chocolate", "strawberry", "cookies n cream", "bubblegum"]
toppings = ["almonds", "banana slices", "choco syrup", "caramel syrup", "white choco chips"]

# toppings[1] = "blueberries"
ice_cream = dict(zip(flavor, toppings))
ice_cream["chocolate"] = "blueberries"
ice_cream.update({"matcha": "pistachios", "ube": "mango slices"})

print(ice_cream)

groceries = {"chicken": 8, "apples": 6, "cucumbers": 3, "milk": 2, "oranges": 4}

remove = groceries.pop("oranges")
keys = groceries.keys()
getpass = groceries.get("chicken")
print(groceries)

newFile = open("math", "w")
newFile.write("i like python")

x = 500
if x > 100:
    raise Exception("x should not be above 100")

# try:
#     print(variable1)
# except:
#     Exception("variable 1 is not yet defined")

# for i in range(6):
#     print("im so happy")

try:
    print(12*6)
except:
    print("this operation can be performed")
else:
    print("this operation can be performed")

best_burger = "burger king"
num2burger = "mcdo"

assert best_burger == "burger king"
assert best_burger == "mcdo"


