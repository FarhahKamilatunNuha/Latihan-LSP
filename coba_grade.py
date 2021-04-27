while True :
    name_siswa = input("Masukkan Nama Anda : ")
    nilai_harian = int(input("Masukkan Nilai Harian : "))
    nilai_uts = int(input("Masukkan Nilai UTS : "))
    nilai_uas = int(input("Masukkan Nilai UAS : "))
    nilai_akhir = int(nilai_harian+nilai_uts+nilai_uas)/3

    if nilai_akhir >= 80:
        predikat_nilai = 'A'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)

    elif nilai_akhir >= 70:
        predikat_nilai = 'B'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)
    
    elif nilai_akhir >= 60:
        predikat_nilai = 'C'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)
    
    elif nilai_akhir >= 50:
        predikat_nilai = 'D'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)
    
    else :
        predikat_nilai = 'E'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)