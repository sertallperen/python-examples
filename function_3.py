def indirim_yap(fiyat,yuzde):
    indirim_miktar = fiyat * (yuzde / 100)
    yeni_fiyat = fiyat - indirim_miktar

    print(f"indirimli fiyat : {yeni_fiyat}")

indirim_yap(100,10)