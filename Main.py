
# Sequential
print('Ibu berkata, "pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli 1 botol susu?"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan
Jumlah_botol_susu = 173
Jumlah_telur = 0
print(f"Jumlah botol susu {Jumlah_botol_susu} botol")
print(f"Jumlah telur {Jumlah_telur} butir")

if Jumlah_botol_susu > 1:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if Jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 butir telur dan 1 botol susu")

else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang kerumah")
print("Menyampaikan hasilnya kepada Ibu")