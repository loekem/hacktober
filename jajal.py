def add (x, y):
    return x + y
def subtract (x, y):
    return x - y
def multiple(x, y):
    return x * y
def divide(x, y):
    return x / y

print("pilih operasi")
print('1.tambah')
print('2.kurang')
print('3.kali')
print('4.bagi')

pilihan = input('masukkan pilihan (1/2/3/4) : ')
angka1 = int(input('masukkan angka : '))
angka2 = int(input('masukkan angka : '))

if pilihan is '1' :
    print(angka1,"+",angka2,"=",add(angka1,angka2))
elif pilihan is '2' :
    print(angka1,"-",angka2,"=",subtract(angka1,angka2))
elif pilihan is '3' :
    print(angka1,"x",angka2,"=",multiple(angka1,angka2))
elif pilihan is '4' :
    print(angka1,":",angka2,"=",divide(angka1,angka2))
else:
    print('input salah')
