#Faiz Firdaus Priyanto
#0640023000005
#Teknik Informatika
#Perpangkatan dan angka

def perpangkatan(angka, pangkat):   #Fungsi angka dan pangkat 
    if pangkat == 0:
        return 1
    else:
        return angka * perpangkatan(angka, pangkat -1 )  #Untuk menghitung angka dan pangkatnya 

while True:
    print("Ini merupakan program pemangkatan negatif dan positif , tekan enter untuk berhenti ")
    number = input("Masukkan Angka : ")  # Meminta pengguna untuk memasukkan angka

    # Periksa apakah pengguna menekan Enter untuk keluar
    if number == '':
        
        break

    try:
        number = float(number)
        pangkat = int(input("Masukkan Pangkatnya: "))   #User menginput pangkat 
        

        hasil = perpangkatan(number, pangkat) # Menghitung dan menampilkan hasil perpangkatan
        print(f"Hasilnya adalah: {hasil}")
    except ValueError:    
        print("Masukkan angka yang valid untuk angka.")