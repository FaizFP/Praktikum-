#Faiz Firdaus Priyanto
#0640023000005
#Teknik Informatika 
#ouput pandas to excel 

import pandas as pd 

#Menampilkan data datanya 
df = pd.read_csv('negara.csv')
print("Berikut data framenya : ")
print(df)

#Menghitung serta menampilkan meanya
negara_mean = pd.read_csv('negara.csv')
print("Berikut data menannya : ")
mean = negara_mean.groupby(['Benua']).mean(numeric_only=True)
print(mean)
mean.to_csv("C:\\Users\\faiz\\Documents\\algo\\OutputPraktikum 12\\NegaraMean.csv", index=False)


#Menghitung dan menampilkan standard deviasi 
standard_deviasi = pd.read_csv('negara.csv')   
print("Berikut data Standard devisiasi nya : ")
standard = standard_deviasi.groupby(["Benua"]).std(numeric_only=True)
print(standard)
standard.to_csv("C:\\Users\\faiz\\Documents\\algo\\OutputPraktikum 12\\NegaraStandarDeviasi.csv", index=False)   #untuk merubah isi dari standard masuk ke NegaraStandarDeviasi.csv

