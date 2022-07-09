Weight=float(input())
height=float(input())
bmi=(Weight/height**2)
print(bmi)

if bmi <18.5 :
    print("laghar")
elif 18.5 <= bmi    <24.9:
    print("normal")
elif 25 <= bmi    <29.9:
    print("ezafe vazn")   
elif 30 <= bmi    <34.9:
    print("chagh")
elif  bmi    >=35:
    print("khali chagh")    