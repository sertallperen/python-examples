op = input("select the operator : ")
num1 = float(input("enter the first number : "))
num2 = float(input("enter the second number : "))


toplam = (num1) + (num2) 
cikarma = (num1) - (num2)
carpim = (num1) * (num2)
bolum = (num1) / (num2)

if(op == "+"):
    print("sonuc : {0}" .format(toplam))

elif(op == "-"):
    print("sonuc : {0}" .format(cikarma))

elif(op == "*"):
    print("sonuc : {0}" .format(carpim))

elif(op == "/"):  
    print("sonuc : {0}" .format(bolum))

else:
    print("hatali islem")