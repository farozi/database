import sqlite3
with sqlite3.connect("data.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS pegawai(
               ID INTEGER PRIMARY KEY NOT NULL,
               Nama TEXT NOT NULL,
               Umur INTEGER NOT NULL,
               Alamat CHAR(50),
               Gaji REAL);""")

def tambahData(array:list):
    cursor.executemany("INSERT INTO pegawai VALUES(?, ?, ?, ?, ?)", array)
    db.commit()

def inputId():
    cursor.execute("SELECT ID FROM pegawai")
    jml = 1
    for x in cursor.fetchall():
        jml +=1
    while True:
        nomor = int(input("  ~> Masukan ID Data : "))
        if nomor >= jml:
            print(" :::ID Data Tidak Ada:::")
        else:
            return nomor

def ubahData(Id, ubah):
    cursor.execute(f"UPDATE pegawai SET {ubah} WHERE ID= {Id}")
    db.commit()

def hapusData(Id):
    cursor.execute(f"DELETE FROM pegawai WHERE ID = {Id}")  #Hapus data di database
    db.commit()

def printData():
    cursor.execute("SELECT * FROM pegawai")
    for x in cursor.fetchall():         
        print(x)

def cari(kondisi):
    cursor.execute(f"SELECT * FROM pegawai WHERE {kondisi}")
    for x in cursor.fetchall():        
        print(x)

while True:
    print("\n====Menu Terminal====")
    print("1. Tambah Data Pegawai")
    print("2. Ubah Data Pegawai")
    print("3. Hapus Data Pegawai")
    print("4. Tampilkan Data Pegawai")
    print("5. Cari Data Pegawai")
    print("0. Keluar")
    pilih = input("Masukan Pilihan 0-5 : ")
    if pilih == "1":
        while True:
            banyak = int(input("Masukan banyaknya data (>10 data): "))
            if banyak >=10 :
                print("----------------------------------")
                x = []
                Id = 1
                cursor.execute(f"SELECT ID FROM pegawai ")
                for x in cursor.fetchall():        
                    if x == (Id, ):
                        Id += 1
                        continue
                    elif x != (Id, ):
                        break
                for data in  range(banyak):
                    nama = str(input("Masukan Nama : ")).upper()
                    umur = int(input("Masukan Umur : "))
                    alamat = str(input("Masukan Alamat : ")).upper()
                    gaji = float(input("Masukan Gaji : "))
                    print("----------------------------------")
                    x.append((Id, nama, umur, alamat, gaji))
                    Id+=1
                tambahData(array = x)
                break
            else:
                print("\nData kurang dari 10 !!!\n")
                continue
    elif pilih == "2":
        print("Pilih data yang akan diedit")
        printData()
        Id = inputId()
        while True:
            print("----------------------------------")
            print("Pilih kolom yang akan diedit")
            print("1. Nama")
            print("2. Umur")
            print("3. Alamat")
            print("4. Gaji")
            print("5. Semua")
            print("0. Selesai Edit")
            pilih = input("Masukan pilihan 0-5 : ")
            if pilih == "1":
                print("----------------------------------")
                nama = str(input("Masukan Nama Baru : ")).upper()
                ubah = f"Nama = '{nama}'"
                ubahData(Id, ubah)
            elif pilih == "2":
                print("----------------------------------")
                umur = int(input("Masukan Umur baru :"))
                ubah = f"Umur= {umur}"
                ubahData(Id, ubah)
            elif pilih == "3":
                print("----------------------------------")
                alamat = str(input("Masukan Kelas Baru : ")).upper()
                ubah = f"Alamat ='{alamat}'"
                ubahData(Id, ubah)
            elif pilih == "4":
                print("----------------------------------")
                gaji = float(input("Masukan Nilai Baru : "))
                ubah = f"Gaji = {gaji}"
                ubahData(Id, ubah)
            elif pilih == "5":
                print("----------------------------------")
                nama = str(input("Masukan Nama Baru : ")).upper()
                umur = int(input("Masukan Umur Baru : "))
                alamat = str(input("Masukan Alamat Baru : ")).upper()
                gaji = float(input("Masukan Gaji Baru : "))
                ubah = f"""Nama= '{nama}', 
                            Umur = {umur}, 
                            Alamat = '{alamat}', 
                            Gaji = {gaji}"""
                ubahData(Id, ubah)
            elif pilih == "0":
                break
            else:
                print(":::PILIHAN TIDAK ADA:::")
                continue
    elif pilih == "3":
        print("----------------------------------")
        print("Pilih data yang akan dihapus")
        printData()
        Id = inputId()
        hapusData(Id)
    elif pilih == "4":
        print("----------------------------------")
        printData()
    elif pilih =="5":
        while True:
            print("----------------------------------")
            print("Cari Lewat?")
            print("1. ID")
            print("2. NAMA")
            print("3. Umur")
            print("4. Alamat")
            print("0. Selesai")
            pilih = input("Masukan pilihan 0-4 : ")
            if pilih =="1":
                print("----------------------------------")
                Id = int(input("Masukan id : "))
                kondisi = f"ID = {Id}"
                cari(kondisi)
            elif pilih == "2":
                print("----------------------------------")
                nama = str(input("Masukan nama : ")).upper()
                kondisi = f"Nama = '{nama}'"
                cari(kondisi)
            elif pilih == "3":
                print("----------------------------------")
                umur = int(input("Masukan Umur : "))
                kondisi = f"Umur = {umur}"
                cari(kondisi)
            elif pilih == "4":
                print("----------------------------------")
                alamat = str(input("Masukan Alamat : ")).upper()
                kondisi = f"Alamat = '{alamat}'"
                cari(kondisi)
            elif pilih == "0":
                break
            else:
                print("\n     Pilihan tidak ada !!!\n")
    elif pilih == "0":
        break
    else:
        print("\n     Pilihan tidak ada !!!\n")
db.close()