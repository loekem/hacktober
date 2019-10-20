# nama = input()
# tanggal_pembelian = input()
# total_pembelian = int(input("jumlah total pembelian anda: "))
# if 1 < total_pembelian <=10:
#     hargaperkaleng = 25000
#     harga_total = total_pembelian*hargaperkaleng
#     print(harga_total)
# elif 11 < total_pembelian <=25:
#     hargaperkaleng = 24500
#     harga_total = total_pembelian*hargaperkaleng
#     print(harga_total)
# elif 26 < total_pembelian <=50:
#     hargaperkaleng = 23000
#     harga_total = total_pembelian*hargaperkaleng
#     print(harga_total)
# elif total_pembelian >50:
#     hargaperkaleng = 22000
#     harga_total = total_pembelian*hargaperkaleng
#     print(harga_total)
# else:
#     print("input salah")

#kasus ke-2
print("menghitung berat badan ideal")
print(50*"-")
tinggi_badan = float(input("tinggi badan anda: "))
berat_badan = float(input("berat badan anda: "))
print(50*"-")
BMI = berat_badan/(tinggi_badan*tinggi_badan)
print(BMI)
if BMI <18:
    print("Under Weight/Kurus – Sebaiknya mulai menambah berat badan dan mengkonsumsi makan berkarbohidrat di imbangi dengan olahraga")
elif 18 < BMI < 25:
    print("Normal Weight/Normal – Bagus, berat badan anda termasuk kategori ideal")
elif 25 < BMI <= 27:
    print("Over Weight/Kegemukan – anda sudah masuk kategori gemuk. sebaiknya hindari makanan berlemak dan mulailah menigkatkan olahraga seminggu minimal 2 kali ")
else:
    print("BMI > 27 Obesitas – Sebaiknya segera membuat program menurunkan berat badan karena anda termasuk kategori obesitas/terlalu gemuk dan tidak baik bagi kesehatan")
