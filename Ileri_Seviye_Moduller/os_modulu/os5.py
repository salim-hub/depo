import os

from datetime import datetime


# print(os.walk("C:/Users/salim/Desktop"))    # ÇIKTISI: <generator object walk at 0x00000279DAD12F90>   -- Bunu görmek için for döngüsü kullanabilirirz

# for i in os.walk("C:/Users/salim/OneDrive/Masaüstü"):
#     print(i)

for klasör_yolu, klasör_isimleri, dosya_isimler in os.walk("C:/Users/salim/OneDrive/Masaüstü"):
    # print("Klasör Yolu", klasör_yolu)
    # print("Klasör İsimler", klasör_isimleri)
    # print("Dosya İsimleri", dosya_isimler)
    # print("***************************************************************")
    for i in dosya_isimler:
        # print(i)
        if (i.endswith(".txt")):
            print(i)