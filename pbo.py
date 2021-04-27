nama = input("Masukan nama    : ")
nharian = int(input("Masukan nilai harian    : "))
nuts = int(input("Masukan Nilai UTS         : "))
nuas = int(input("Masukan Nilai UAS         : "))

harian = nharian * 20 / 100
uts = nuts * 40 / 100
uas = nuas * 40 / 100


nilai_akhir = harian + uts + uas

print("\nNama       : %s" %nama)
print("Nilai Harian : %d" %nharian)
print("Nilai UTS    : %d" %nuts)
print("Nilai UAS    : %d" %nuas)
print("Nilai Akhir  : " ,float(nilai_akhir))

if nilai_akhir >=80 :
    print ("\n Predikat Nilai: A")
elif nilai_akhir >=70 :
    print("\n Predikat Nilai: B")
elif nilai_akhir >=55 :
    print("\n Predikat Nilai: C")
elif nilai_akhir >=40 :
    print("\n Predikat Nilai: D")
elif nilai_akhir <=39 :
    print("\n Predikat Nilai: E")