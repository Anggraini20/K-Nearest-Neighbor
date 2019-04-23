import numpy as np
import math
train = np.genfromtxt('DataTrain_Tugas3_AI.csv', skip_header=1, dtype=None, delimiter=',')
test = np.genfromtxt('DataTest_Tugas3_AI.csv', skip_header=1, dtype=None, delimiter=',')
def euclidean(tr, te):
    return (te-tr)**2

def hsl_eucli(tr1, tr2, tr3, tr4, tr5, te1, te2, te3, te4, te5):
    hsl1 = euclidean(tr1, te1)
    hsl2 = euclidean(tr2, te2)
    hsl3 = euclidean(tr3, te3)
    hsl4 = euclidean(tr4, te4)
    hsl5 = euclidean(tr5, te5)
    hasil = hsl1 + hsl2 + hsl3 + hsl4 + hsl5
    return math.sqrt(hasil)

k = 5 #variable k merupakan nilai kuantum
A = [] #array A merupakan array yang berisi nilai jarak antara data training dan data testing dengan menggunakan rumus Euclidean
hasil = [] #array hasil merupakan array yang berisi nilai kelas data testing

#melakukan perulangan untuk setiap data testing ke data training
for item in test:
    nol = 0
    satu = 0
    dua = 0
    tiga = 0
    for i in train:
        nilai = hsl_eucli(i[1], i[2], i[3], i[4], i[5], item[1], item[2], item[3], item[4], item[5])
        A.append([nilai, i[6], i[0]])
    A.sort(key=lambda isi: isi[0]) #melakukan sorting
    for j in range(k):
        if A[j][1] == 0:
            nol = nol+1
        elif A[j][1] == 1:
            satu = satu+1
        elif A[j][1] == 2:
            dua = dua+1
        else:
            tiga = tiga+1
    maxx = max(nol, satu, dua, tiga)
    if maxx == nol:
        hasil.append(0)
    elif maxx == satu:
        hasil.append(1)
    elif maxx == dua:
        hasil.append(2)
    else:
        hasil.append(3)
    A.clear()

for item in hasil:
    print(item)

np.savetxt('TebakanTugas3.csv',hasil,fmt='%i')
