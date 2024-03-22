sayi = input("enter the number : ")
cifttoplam = 0
tektoplam = 0

for i in range(1,int(sayi)+1):
    if(i%2==0):
        cifttoplam+=i

    else:
        tektoplam+=i
       
print("cift sayıların toplamı = " ,format(cifttoplam))
print("tek sayıların toplamı = " ,format(tektoplam))



