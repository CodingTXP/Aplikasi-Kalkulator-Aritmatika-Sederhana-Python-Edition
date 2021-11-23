# Aplikasi Kalkulator Arimatika Sederhana - AKAS 1.0
print("Aplikasi Kalkulator Arimatika Sederhana - AKAS 1.0")
print("==================================================\r\n")

nilai_a = float(input("Input nilai a (boleh dalam desimal): "))
print("a = ", nilai_a)

nilai_b = float(input("Input nilai b (boleh dalam desimal): "))
print("b = ", nilai_b,"\r\n")

print("Menu pilihan operator:\r\n1. Penjumlahan\r\n2. Pengurangan\r\n3. Perkalian\r\n4. Pembagian (tidak dibulatkan)\r\n5. Pembagian (dibulatkan ke bawah)\r\n6. Modulus (sisa pembagian)\r\n7. Perpangkatan")
operator = input("Masukkan nomor menu sesuai dengan operator yang diinginkan: ")
if operator == "1":
    hasil = nilai_a + nilai_b
    print("\r\n", nilai_a, "+", nilai_b, "=", hasil)
elif operator == "2":
    hasil = nilai_a - nilai_b
    print("\r\n", nilai_a, "-", nilai_b, "=", hasil)
elif operator == "3":
    hasil = nilai_a * nilai_b
    print("\r\n", nilai_a, "×", nilai_b, "=", hasil)
elif operator == "4":
    if nilai_b == 0.0:
        print("Membagi suatu angka dengan nol (0) itu haram di matematika, kawan.")
    else:
        hasil = nilai_a / nilai_b
        print("\r\n", nilai_a, ":", nilai_b, "=", hasil)
elif  operator == "5":
    if nilai_b == 0.0:
        print("Membagi suatu angka dengan nol (0) itu haram di matematika, kawan.")
    else:
        hasil = nilai_a // nilai_b
        print("\r\n", nilai_a, ":", nilai_b, "=", hasil)
elif  operator == "6":
    hasil = nilai_a % nilai_b
    print("\r\nModulus dari ", nilai_a, ":", nilai_b, "=", hasil)
elif  operator == "7":
    hasil = nilai_a ** nilai_b
    print("\r\n", nilai_a, "pangkat", nilai_b, "=", hasil)
else: print("\r\nNomor menu yang anda pilih tidak sesuai/tidak dapat ditemukan.\r\nJalankan ulang program untuk mengulangi.")

print("\r\nAplikasi Kalkulator Arimatika Sederhana - AKAS 1.0 is Shutting Down...")