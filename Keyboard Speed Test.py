import time
import datetime

print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
time.sleep(0.5)

zaman = datetime.datetime.now()

metin =input("Metin Giriniz : ")
zaman2=datetime.datetime.now()

yazim_hizi=zaman2-zaman
saniye=round(yazim_hizi.total_seconds() ,2)
zaman3=round(len(metin)/saniye,1)

print("Toplam Zaman : {}".format(saniye))
print("{} Saniye Başına".format(zaman3))

