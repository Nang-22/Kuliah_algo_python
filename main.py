from datetime import date
import datetime
import random
print("\nISI DATA DIRI ANDA\n")

nama = input("masukkan nama anda\t\t: ")
tempat = input("dimana tempat anda lahir\t: ")
tanggal = int(input("tangggal berapa anda lahir\t: "))
bulan = int(input("bulan berapa anda lahir\t\t: "))
tahun = int(input("tahun berapa lahir\t\t: "))
jabatan = input("apa jabatan anda\t\t: ")
gaji_pokok = float(input("masukkan gaji pokok anda\t: "))
tunjangan = float(input("masukkan tunjangan anda\t\t: "))
gender = input("jenis kelamin anda (L/P)\t: ")
lama_kerja = int(input("lama bekerja (dalam tahun)\t: "))


inisial = "".join([i[0] for i in nama.split()])
user_id = inisial + str(tahun) + str(random.randint(100, 999))


lahir = date(tahun , bulan, tanggal)
hari_ini = date.today()
umur = hari_ini.year - lahir.year
if (hari_ini.month , hari_ini.day) < (lahir.month , lahir.day):
    umur -= 1

pajak = 0.5 * gaji_pokok
gaji_bersih = gaji_pokok + tunjangan - pajak



if umur <= 25 and gaji_pokok < 50000000:
    bonus = "dapat 🤲"
else:
    bonus = "sabar 🤝"

tanggal_sekarang = datetime.datetime.now().strftime("%d-%m-%Y")



print("\n\n==============DATA DIRI ANDA=============\n")
print("NAMA LENGKAP\t\t: ", nama) 
print("JABATAN\t\t\t: ", jabatan)
print("TEMPAT/TGL LAHIR\t: ", tempat ,",", tanggal , "/", bulan, "/", tahun    )
print(f"GAJI POKOK\t\t:  {gaji_pokok:.0f}")
print(f"TUNJANGAN\t\t:  {tunjangan:.0f}")
print("JENIS KELAMIN (L/P)\t: ", gender)
print("LAMA BEKERJA\t\t: ", lama_kerja, "Tahun")
print("\n==============TERIMA KASIH==============\n")


print("\n=========USER ID=========")
print("NAMA\t: ", nama)
print("TANGGAL\t: ", tanggal_sekarang)
print("USER ID\t: ", user_id)
print("USIA\t: ", umur , "Tahun")
print("=========================\n")

print("\n==========GAJI KARYAWAN==========")
print(f"Nama\t\t : {nama}")
print(f"Jabatan\t\t : {jabatan}")
print(f"Tanggal\t\t : {tanggal_sekarang}")
print(f"Gaji pokok\t : Rp {gaji_pokok:.0f}")
print(f"Tunjangan\t : Rp {tunjangan:.0f}")
print(f"Pajak (5%)\t : Rp {pajak:.0f}")
print("---------------------------------")
print(f"Gaji berseih\t : Rp {gaji_bersih:.0f}")
print(f"Bosnus\t\t : {bonus}")
print("=================================\n")

