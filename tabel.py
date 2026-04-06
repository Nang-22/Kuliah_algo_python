
nama = input("\nmasukkan nama yang benar: ")

while nama != "nanang":
    print("nama anda salah, coba lagi")
    nama = input("masukkan nama yang benar: ")

nim = input("masukkan nim yang benar\t: ")

while nim != "25241018":
    print("nim anda salah, coba lagi")
    nim = input("masukkan nim yang benar\t: ")


angka1 = int(input("\nmasukkan angka\t\t: "))

for i in range(1, 11):
    print(f"{angka1} x {i} = {angka1 * i}\n")