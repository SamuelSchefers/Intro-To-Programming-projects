item = input("Item name:")
price = input("Price of "+ item + " :$")
tax=1.06875
price_float = float(price)
def calculate_tax(p, t):
    return p*t
num_float = calculate_tax(price_float, tax)
float_str = str(num_float)
print ("Taxed price of " + item + ":$" + float_str)