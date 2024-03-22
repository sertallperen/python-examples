boy = float(input("boyunuzu giriniz : "))
kilo = int(input("kilonuzu giriniz : "))

vki = kilo / (boy*boy)  

if((vki) <= 18):
    print("cok zayif" .format(vki))

elif(  18 < (vki) <= 25  ):
    print("normalsiniz : " .format(vki))

elif(25 < (vki) <= 30):
    print("kilolusunuz : " .format(vki))

elif( 30 < (vki) <= 35 ):
    print("obezsin : " .format(vki))

elif( 35 < (vki) ):
    print("ölecen amk " .format(vki))
