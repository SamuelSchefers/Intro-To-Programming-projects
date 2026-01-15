print("Please input 2 numbers and the calculator will add, subtract, multiply, and divide your input!")
x_input=input("Please enter X value:")
x_float=float(x_input)
y_input=input("Please enter Y value:")
y_float=float(y_input)
#this probably works
def Add(x,y):
    return (x+y)
#adds x and y
#doesnt work
def Subtract(x,y):
    return (x-y)
#subtracts y from x
def Multiply(x,y):
    return (x*y)
#multiplies x by y
def Divide(x,y):
    return (x/y)
#divides x by y
print ("Addition:")
print(Add(x_float,y_float))
#prints addition output
print("Subtract:")
print(Subtract(x_float,y_float))
#prints subtraction output
print("Multiply:")
print(Multiply(x_float,y_float))
#prints multiply output
print("Divide:")
print(Divide(x_float,y_float))
#prints divide output