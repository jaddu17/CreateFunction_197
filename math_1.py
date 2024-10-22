import math #library untuk operasi matematika

luas_lingkaran = lambda r: math.pi * r*r
#lambda adalah fungsi yang menerima satu argumen r

#contoh penggunaannya
jari_jari = 7
area = luas_lingkaran(jari_jari)
#area : menyimpan hasil fungsi dari luas lingkaran

#menampilkan luas lingkaran
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")