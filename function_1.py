#fonksiyon kullanarak dairenin alanını veren kod


def daireAlan(yaricap):
    alan = float(yaricap) * float(yaricap)*3.14
    print ("Alan :",alan)
    return alan
 
r = input("Yarıçapı Gir :")
 
daireAlan(r)  


