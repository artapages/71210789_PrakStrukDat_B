import math
data = int(input("Masukan range data: "))
dict = dict()

for i in range(data):
    if i % 2 ==0:
        n = i
        faktorial = 1
        for case in range(1, n+1):
            faktorial = faktorial * case
        dict[i] = faktorial

print(dict)
output = int(input("Data ditampilkan: "))

if output in dict.keys()c:
    print(dict[output])
else:
    print("Data tidak ditemukan")