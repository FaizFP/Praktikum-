#Faiz Firdaus Priyanto
#064002300005
#Teknik Informatika
#Menghintung Dengan pandas


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


#Menghitung dan menampilkan standard deviasi 
standard_deviasi = pd.read_csv('negara.csv')
print("Berikut data Standard deviation nya ; ")
standard = standard_deviasi.groupby(["Benua"]).std(numeric_only=True)
print(standard)



