def solusi(n):
    # Inisialisasi variabel untuk menyimpan hasil
    total = 0
    
    # Loop dari 1 hingga n-1
    for i in range(1, n):
        # Jika i adalah kelipatan 3 atau 5, tambahkan ke total
        if i % 3 == 0 or i % 5 == 0:
            total += i
    
    return total
print(solusi(10))
print(solusi(20))