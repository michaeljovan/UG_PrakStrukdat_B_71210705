def tambah(a1,a2):
    print("tambah=",a1+a2)

def kurang(a1,a2):
    print("kurang=",a1-a2)

def kali(a1,a2):
    print("kali=",a1*a2)

def bagi(a1,a2):
    print("bagi=",a1/a2)

while True:
    print("1.tambah")
    print("2.kurang")
    print("3.kali")
    print("4.bagi")    
   
    pilihan=str(input("masukkan pilihan perhitungan:"))
    if pilihan=="1":
        a1=int(input("masukkan angka yang ingin dihitung:"))
        a2=int(input("masukkan angka yang ingin dihitungkan :"))
        tambah(a1,a2)


    elif pilihan=="2":
        a1=int(input("masukkan angka yang ingin dihitung:"))
        a2=int(input("masukkan angka yang ingin dihitungkan:"))
        kurang(a1,a2)
    
    elif pilihan=="3":
        a1=int(input("masukkan angka yang ingin dihitung:"))
        a2=int(input("masukkan angka yang ingin dihitungkan:"))
        kali(a1,a2)
    
    elif pilihan=="4":
        a1=int(input("masukkan angka yang ingin dihitung:"))
        a2=int(input("masukkan angka yang ingin dihitungkan:"))
        if a2 == 0:
            print('')
        else:
            bagi(a1,a2)
                
    elif pilihan=="q": 
        print("program berhenti")
        break
    
   