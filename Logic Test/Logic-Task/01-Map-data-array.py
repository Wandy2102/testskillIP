def productArray(arr):
    n = len(arr)
    # Inisialisasi array yang akan menyimpan produk
    prod = [1] * n
    # Hitung total seluruh elemen dalam arr
    total = sum(arr)
    # Hitung produk untuk setiap elemen arr
    for i in range(n):
        # Hitung rata-rata seluruh elemen kecuali elemen i
        avg = (total - arr[i]) / (n - 1)
        # Hitung produk dengan menggunakan rumus rata-rata
        prod[i] = round(avg)
    return prod


print(productArray([12,20]))
print(productArray([12,9,6,3]))
print(productArray([2,4,6]))

