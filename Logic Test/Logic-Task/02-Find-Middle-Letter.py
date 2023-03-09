def cari_huruf_tengah(huruf_pertama, huruf_terakhir):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Temukan indeks huruf pertama dan terakhir dalam alfabet
    indeks_pertama = alfabet.index(huruf_pertama)
    indeks_terakhir = alfabet.index(huruf_terakhir)

    # Temukan indeks huruf tengah antara huruf pertama dan terakhir
    indeks_tengah = (indeks_pertama + indeks_terakhir) // 2

    # Jika jumlah huruf antara huruf pertama dan terakhir ganjil, maka ambil dua huruf tengah
    if (indeks_pertama + indeks_terakhir) % 2 == 1:
        indeks_tengah += 1

    # Ambil huruf tengah atau dua huruf tengah
    huruf_tengah = alfabet[indeks_tengah - 1:indeks_tengah + 1]

    return huruf_tengah



print(cari_huruf_tengah('Q', 'U'))
print(cari_huruf_tengah('R', 'U'))
print(cari_huruf_tengah('T', 'Z'))
print(cari_huruf_tengah('Q', 'Z'))

