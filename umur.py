
umur = int(input("Masukan umur anda\t: "))

if umur >= 18 and umur <= 60:
    print("anda cukup umur")
elif umur < 18:
    print("anda belum cukup umur")
elif umur < 0:
    print("anda belum lahir")
else:
    print("banyakin ibadah, betar lagi mati")


