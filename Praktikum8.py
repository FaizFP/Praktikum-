#Faiz Firdaus Priyanto
#064002300005
#Teknik Infomatika
#Penjumlahan Berurutan

def penjumlahan_berurutan(n, angka=[]):
    if n == 0:
        return sum(angka)
    else:
        angka.append(int(input(f"Masukkan angka ke-{len(angka)+1}: ")))
        return penjumlahan_berurutan(n-1, angka)

jumlah = int(input("Masukkan Jumlah Baris : "))
print(penjumlahan_berurutan(jumlah))




