# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:25:04 2023

@author: faiz
"""





angka_cari = int(input("Masukkan angka : "))
def mencari_angka(angka_cari,list_angka):   #Mencari angka ada atau tidaknya 
    if angka_cari in list_angka:
        lokasi = list_angka.index(angka_cari)             #lokasi angka 
        return f" {angka_cari} ditemukan , pada index {lokasi} " 
    

list_angka = [8, 17, 5, 14, 2, 20, 11, 3, 9, 12, 18, 7, 1, 16, 19, 6, 4, 10, 13, 15]  #list angka 
list_angka.sort() #pengurutan angka 
hasil_pencarian = mencari_angka(angka_cari, list_angka)
print(hasil_pencarian)
print(list_angka)
