def urutasc(mylist):
    for i in range(len(mylist)-1, 0, -1):
        for j in range(i):
            if mylist[j] > mylist[j+1]:
                simpan = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = simpan
    print(mylist)

def urutdsc(mylist):
    for i in range(len(mylist)-1, 0, -1):
        for j in range(i):
            if mylist[j] < mylist[j+1]:
                simpan = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = simpan
    print(mylist)

print('Program mengurutkan data dengan metode bubble sort')

angka1 = int(input('Masukkan bilangan ke 1 : '))
angka2 = int(input('Masukkan bilangan ke 2 : '))
angka3 = int(input('Masukkan bilangan ke 3 : '))
angka4 = int(input('Masukkan bilangan ke 4 : '))
angka5 = int(input('Masukkan bilangan ke 5 : '))
angka6 = int(input('Masukkan bilangan ke 6 : '))
angka7 = int(input('Masukkan bilangan ke 7 : '))
angka8 = int(input('Masukkan bilangan ke 8 : '))
angka9 = int(input('Masukkan bilangan ke 9 : '))
angka10 = int(input('Masukkan bilangan ke 10 : '))

angka = [angka1, angka2, angka3, angka4, angka5,
         angka6, angka7, angka8, angka9, angka10]

print('===========================')
print('pilih metode pengurutan : ')
print('1. Sorting Ascending \n2.Sorting Deccending')
pilih = input('metode yang dipilih : ')

print('===========================')
print('data sebelum diurutkan : ')
print(angka)
print('data sebelum diurutkan : ')

if pilih == ('1'):
    urutasc(angka)
elif pilih == ('2'):
    urutdsc(angka)
else:
    print("Angka yang anda masukkan salah")

home = input("kembali ke menu utama (Y/N)? ")
text = print('Program mengurutkan data dengan metode bubble sort')
back = ('')
garis = ('===========================')
if home == ('Y'):
    garis
    text
    angka1 = int(input('Masukkan bilangan ke 1 : '))
    angka2 = int(input('Masukkan bilangan ke 2 : '))
    angka3 = int(input('Masukkan bilangan ke 3 : '))
    angka4 = int(input('Masukkan bilangan ke 4 : '))
    angka5 = int(input('Masukkan bilangan ke 5 : '))
    angka6 = int(input('Masukkan bilangan ke 6 : '))
    angka7 = int(input('Masukkan bilangan ke 7 : '))
    angka8 = int(input('Masukkan bilangan ke 8 : '))
    angka9 = int(input('Masukkan bilangan ke 9 : '))
    angka10 = int(input('Masukkan bilangan ke 10 : '))
    angka = [angka1, angka2, angka3, angka4, angka5,
            angka6, angka7, angka8, angka9, angka10]
    garis
    print('pilih metode pengurutan : ')
    print('1. Sorting Ascending \n2. Sorting Deccending')
    pilih = input('metode yang dipilih : ')
    print('===========================')
    print('data sebelum diurutkan : ')
    print(angka)
    print('data setelah diurutkan : ')
    if pilih == ('1'):
        urutasc(angka)
    else :
        urutdsc(angka)
    home = input("kembali ke menu utama (Y/N)? ")
else:
    back