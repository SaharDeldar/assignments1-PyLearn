import math
while True:
    op = input("enter operator")
    if op == "exit":
        break
    if op =="sin" or op == "log" or op =="fact" or op =="tan" or op == "cot" or op =="fact":
        a = int(input("enter number"))
    else:
        a = int(input("enter number"))
        b = int(input("enter number"))

    if op == "+":
        result = a+b
    elif op == "-":
        result = a-b
    elif op == "*":
        result = a*b
    elif op == "/":
        result = a/b  
    elif op =="sin":
        result =math.sin(a)
    elif op =="tan":
        result =math.tan(a)
    elif op == "cot":
        result = 1/math.tan(a)
    elif op == "fact":
        result = math.factorial(a)
    

    print (result)