d1 = "makanan disini gurih dan enak"
d2 = "makanan disini biasa saja"
d3 = "makanan disini hambar dan tidak enak"

#d1 = "kelas unicorn adalah program kampus merdeka"
#d2 = "kelas unicorn merupakan kelas pertama di orbit"

d_string = f"{d1} {d2} {d3}"
d_semua = d1.split() + d2.split() + d3.split()
d_list = [d1, d2, d3]
print(d_semua)
print()



kamus_kata = {}
for data in d_semua:
    kamus_kata[data] = d_string.count(data)
print(kamus_kata)
print()



# TF
data_dict = {}
data_list = []
for kalimat in d_list:
    for kata in d_semua:
        data_dict[kata] = kalimat.count(kata)/len(kalimat.split())
    data_list.append(data_dict)
    data_dict = {}
print(data_list)
print()

print("Term Frequency")
for i in range(len(data_list)):
    print(f"Data{i+1} : {data_list[i]}")
print()



cek_ulang = []
for d in d_list:
    periksa = set(d.split())
    cek_ulang += list(periksa)
for cek in cek_ulang:
    kamus_kata[cek] = cek_ulang.count(cek)

# IDF
import math
data_idf = {}
for kata in kamus_kata:
    hitung = math.log(len(d_list)/kamus_kata[kata], 10)
    data_idf[kata] = hitung
print(data_idf)
print()




# TFIDF
hasil = []
data_sementara = {}
for index in range(len(data_list)):
    for i in data_list[index]:
        hitung = data_list[index][i] * data_idf[i]
        data_sementara[i] = round(hitung, 3)
    hasil.append(data_sementara)
    data_sementara = {}

for i in range(len(hasil)):
    print(f"Data {i} : {hasil[i]}")
    print()
