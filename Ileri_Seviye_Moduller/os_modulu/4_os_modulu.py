import os
from datetime import datetime
print(os.getcwd())

# os.rename("test.txt", "test2.txt") #dosya adını değiştirir.


# print(os.stat("test2.txt")) #dosya hakkındaki tüm bilgileri verir.

# print(os.stat("test2.txt").st_mtime)  #dosyanın oluşturulma zamanını saniye cinsinden verir

print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime))