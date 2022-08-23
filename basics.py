# Say words!
print("Hello World!")

# # Do Math!
print(5 + (10 * 5))

# # This assigns the value to the variable x
x: int = 5
print(x)

# # Give x a new value
x = "Hello World!"
print(x)

# # Exponent Notation
x = 5 ** 2
print(x)

# # Input takes data from the terminal user
# password = input("Enter your password!")

# if password == "CSH":
#     print("Correct!")
# else:
#     print("Incorrect!")

counter = 1

while counter <= 10:
    print(counter)
    counter += 1

for number in range(1,11):
    print(number)

names = ["Joe Abbate", "Wilson McDade", 69, 420, [], False, 69.420]


for name in names:
    print("Hi", name, end="\n\n")

print("Hi", "Shaun","and","Igor", end="\n", sep=" dammit ")

def get_name():
    name = input("What is your name?")
    hello_string = "Hello " + name
    hello_string = f"Hello {name}"
    # return hello_string

print(get_name())

def do_math():
    number = int(input("Give me a number! "), 16)
    # 0123456789ABCDEF
    print(number)

do_math()