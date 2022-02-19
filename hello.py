import math

PI = math.pi

print("Hello World")
print("We have already finished")

z = "I am living in Adelaide"
print(z)

print("El valor de pi es:", PI)
seno = math.sin(PI/6)
coseno = math.cos(PI/3)
print("El seno es:", round(seno, 2))
print("El coseno es:", round(coseno, 2))

print("La tangente de 45 es:", round(math.tan(45*PI/180), 2))

def print_hello(name):
    print("Hello everybody, my name is", name)

print_hello("Alberto")

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[0])
print(thislist[0] + thislist[1] + thislist[2])
