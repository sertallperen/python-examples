print("hosgeldiniz : ")

bilet = input("Sinema için 's' , tiyatro için 't' tuşlayınız : ")
indirim = input("Öğrenciyseniz 'y', değilseniz 'n' tuşlayınız : ")
ücret = 0 

sinema = 15
tiyatro = 10

if ( bilet == 's' and indirim == 'y' ):
    sinema = sinema / 2 
    print("ödemeniz gereken tutar = " ,float(sinema) )

elif ( bilet == 's' and indirim == 'n' ):
    sinema = sinema 
    print("ödemeniz gereken tutar : " ,float(sinema) )

if ( bilet == 't' and indirim == 'y' ):
    tiyatro = tiyatro / 2 
    print("ödemeniz gereken tutar = " ,float(tiyatro) )

elif ( bilet == 't' and indirim == 'n' ):
    tiyatro = tiyatro 
    print("ödemeniz gereken tutar : " ,float(tiyatro) )
