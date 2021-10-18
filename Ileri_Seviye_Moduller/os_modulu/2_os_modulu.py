import os

print(os.getcwd())

#os modulünün altında bir klasör oluştuyrmak için:

# os.mkdir("Deneme1")          # yeni bir klasör oluşturmak için
# os.mkdir("Deneme2/Deneme3")  # deneme2 yoksa çalışmaz

os.makedirs("Deneme2/Deneme3") # iç içe iki klasör oluşturmak için.