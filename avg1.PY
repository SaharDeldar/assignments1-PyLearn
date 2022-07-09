name = input ("Enter Your name ")
family=input ("Enter Your family ")
a = int (input("Enter Your first score "))
b = int (input("Enter Your second score "))
c = int (input("Enter Your third score "))
av= (a+b+c)/3
if av >=17:
    print("avg great")
if 17>av>=12:
    print("avg normal")
if av<12:
    print("fail")
    

print ("Dear ",name,"your average is ",av)