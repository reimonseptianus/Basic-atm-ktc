saldo = 5000
pin_atm = 1234
sisa_saldo =[]
def cek_pin(pin):
    return pin == pin_atm
def tarik_tunai(nominal):
    global saldo
    if saldo >= nominal:
        saldo -= nominal
        sisa_saldo.append(f"Anda Telah Tarik Tunai Sebesar {nominal}")
        return True
    else:
        sisa_saldo.append("Saldo Tidak Mencukupi Untuk Tarik Tunai")
        return False
def input_pin():
    pin = int(input("Masukkan PIN: "))
    if pin == pin_atm:
        return True
    else:
        return False
while True:
    pin_benar = input_pin()
    if pin_benar:
        break
    else:
        print("PIN Salah.Silakan Coba Lagi.")
while True:
    print("\nMenu ATM:")
    print("1. Tarik Tunai")
    print("2. Setor Tunai")
    print("3. Cek Saldo")
    print("4. cek pin")
    print("5. EXIT")
    pilihan = int(input("masukkan pilihan: "))
    if pilihan == 1:
        nominal = int(input("Masukkan Nominal Yang Ingin Di Tarik: "))
        if tarik_tunai(nominal):
            print(f"Saldo Anda Saat Ini: {saldo} ")
        else:
            print("Tidak dapat Melakukan Tarik Tunai.")
    elif pilihan == 2:
        setor = int(input("masukkan nominal setor \nRp "))
        saldo += setor
    elif pilihan == 3:
        print(f"Saldo Rekening Anda Saat Ini: {saldo}")
    elif pilihan == 4:
        print (f"Pin ATM anda adalah : {pin_atm}")
    elif pilihan == 5:
        print("Terimah Kasih Telah Menggunakan ATM Kami.")
        break
    else:
        print("Pilihan Tidak Valid.Silakan Coba Lagi.")



