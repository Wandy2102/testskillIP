def find_closest_fibonacci(arr):
    # menjumlahkan semua elemen dalam array
    total = sum(arr)
    
    # inisialisasi bilangan fibonacci awal
    fib1 = 0
    fib2 = 1
    
    # cari bilangan fibonacci terdekat yang lebih besar dari atau sama dengan total
    while fib2 < total:
        temp = fib1 + fib2
        fib1 = fib2
        fib2 = temp
    
    # periksa apakah total sama dengan salah satu bilangan fibonacci yang telah dicari
    if total == fib2:
        return 0
    elif total < fib2 - total:
        return fib1 - total
    else:
        return fib2 - total
print(find_closest_fibonacci([15,1,3]))