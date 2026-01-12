a = 115         #int -> string
b = 3.14        #float -> string
c = "68"        #string -> int
d = "True"      #string -> boolean
e = True        #boolean -> string
f = False       #boolean -> string
g = '10110111'  #byte -> int
h = "2.54"      #string -> float
i = 100         #int -> float
j = 10.0        #float -> int
k = 254         #int -> byte
num=115
num_str=str(num)
print (num_str)

num_float=3.14
float_str=str(num_float)
print (float_str)

num_str="68"
num-int(num_str)
print (num)

bool_str="True"
bool_val=bool(bool_str)
print(bool_val)

bool_str="False"
bool_val= bool(bool_str)
print(bool_val)

binary_num='10110111'
num=int(binary_num, 2)
print (num)

float_str="2.54"
num=float(float_str)
print (num)

num=100
num_float=float(num)
print (num_float)

num_float=10.0
num=int(num_float)
print (num)

num=254
binary_num=bin(num)
print (binary_num)