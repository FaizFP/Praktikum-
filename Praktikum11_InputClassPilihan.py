#Faiz Firdaus Priyanto
#0640023000005
#Teknik Informatika 
#Fungsi Class 


class DataNama:    
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def pilihan():  #Tampilan menu program 
        print("====Program OOP====")
        print("1.Mendeklarasikan objek ")
        print("2.Menampilkan objek")
        print("3.Merubah Nilai objek")
        print("4.Menghapus objek")
        print("5.Keluar dari program ")

    def biodata(self):    #Hasil print biodata 
        print(f"Nama  : {self.nama}")
        print(f"Nilai : {self.nilai}")
        
a = None  


while True:
    DataNama.pilihan()    #Menampilkan pilihan menu 
    pilihan_user = int(input("Masukkan pilihan anda (1/2/3/4/5/) : "))  #pilihan user
    
            

    if pilihan_user == 1:    #mendeklarasikan objek 
         nama = input("Masukkan nama : ")
         nilai = input("Masukkan nilai : ")
         a = DataNama(nama,nilai) 
         
         
           

    elif pilihan_user == 2:  #menampilkan isi def biodata 
            if a :
                   a.biodata()
               

      
    elif pilihan_user == 3:  #Untuk mengubah nilai 
            if a is not None:
                 print("1. Ubah Nama")
                 print("2. Ubah Nilai")
                 pilihan_ubah = input("Pilih apa yang ingin diubah (Nama/Nilai): ")
                 if pilihan_ubah == "Nama":
                      a.nama = input("Masukkan nama baru: ")
                 elif pilihan_ubah == "Nilai":
                      a.nilai = input("Masukkan nilai baru: ")
                 else:
                      print("Masukkan pilihan yang benar")     

    elif pilihan_user == 4:   #pilihan 4 untuk menghapus objek
         a.nama  = None
         a.nilai = None 
         print("Data Berhasil dihapus")

    elif pilihan_user ==5:    #untuk menghentikan program 
         print("Terima kasih sudah menggunakan program saya :)")
         break     
    
    else:
         print("Masukkan pilihan yang benar ")


     


        

