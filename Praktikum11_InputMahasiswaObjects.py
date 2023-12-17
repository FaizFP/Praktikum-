# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:30:06 2023

@author: faiz
"""

class Mahasiswa:
    mhswCount= 0 
    
    
    def __init__(self, nama, nim, angkatan):     #fungsi untuk memanggil objek mahasiswa
        self.nama = nama   #variabel untuk setiap objek mahasiswa
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.mhswCount += 1

    def cetakNama(self):           #fungsi nama dll dari Mahasiswa
        print(f"Nama : {self.nama}")  
    def CetakNim(self):
        print(f"Nim : {self.nim}")
    def CetakAngkatan(self):
        print(f"Angkatan : {self.angkatan}")
    def jumlah_siswa(self):
        print("Jumlah mahasiswa %d" % Mahasiswa.mhswCount)    

    # Contoh penggunaan:

nama = input("Masukkan nama Anda: ")   #input user 
nim = input("Masukkan NIM Anda: ")    
angkatan = int(input("Masukkan angkatan Anda: "))
k1 = Mahasiswa(nama, nim, angkatan)    
k1.cetakNama()  #fungsi cetak nama
k1.CetakNim()   #fungsi cetak nim
k1.CetakAngkatan()  #fungsi cetak angkatan 
k1.jumlah_siswa()  #fungsi jumlah siswa


