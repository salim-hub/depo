import sys

sys.stderr.write("Bu bir hata mesajıdır\n")     #işlemin(process) çıktı vermesini sağlar

sys.stderr.flush()      #buffer'ı hemen yaz

sys.stdout.write("Bu normal bir yazıdır\n")     #hata mesajını çıktı olarak vermek için kullanılır

print(sys.argv) #bilgisayardaki konumu verir.