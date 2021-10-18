from PIL import Image, ImageFilter

image = Image.open("atam.jpg")  

# image.show()  # fotoyu açmak için

# image.save("atam2.jpg") # resmi farklı isimle kaydetmek ve kopyalamak için

# image.rotate(180).save("atam3.jpg")   #resmi döndürmek için

# image.rotate(90).save("atam4.jpg")

# image.convert(mode = "L").save("atam5.jpg")  # siyah-beyaz halini almak için

# boyutlarını değiştirmek için:
# degistir = (960, 600)
# image.thumbnail(degistir)
# image.save("atam6.jpg")


# Resmi blurlamak için. Daha fazla blurlamak için değeri değiştir.
# image.filter(ImageFilter.GaussianBlur(5)).save("atam7.jpg")
# image.filter(ImageFilter.GaussianBlur(10)).save("atam8.jpg")


# FOTO KIRPMAK İÇİN:
kırpılacak_alan = (340, 0, 950, 600)


image.crop(kırpılacak_alan).save("atam9.jpg")



