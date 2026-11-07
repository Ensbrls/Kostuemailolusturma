def tekrar():
    global kad,soyad,dyil,sifre,kadson,soyadson,dyilson,sonemail
    print("\n"+("-" * 50)+"\n")

    kad = input("Adınızı Giriniz: ")
    soyad = input("Soyadınızı Giriniz: ")
    dyil = input("Doğum Yılınızı Giriniz: ")
    sifre = input("\n"+"Şifrenizi Giriniz: ")

    kadson = kad[:2].lower() + kad[2:]
    soyadson = soyad[:-3] + soyad[-3:].upper()
    dyilson = dyil[-2:]

    sonemail = kadson + soyadson + dyilson + "@kocaelisaglik.edu.tr"

    def sifretekrar():
        global sifre
        if (len(sifre) >= 8) and " " not in sifre:
            print("Şifreniz Geçerlidir.")
        else:
            sifre = input("Şifrenizi Tekrar Giriniz: ")
            sifretekrar()

    sifretekrar()
    print()

    print("Oluşturulan Mail:", sonemail)
    print()
    sorutekrar = input("Tekrardan E-mail Oluşturmak İstermisiniz? (E/H): ")
    if sorutekrar == "E" or sorutekrar == "e":
        tekrar()
    else:
        print("Görüşmek Üzere!")
        print("\n"+("-" * 50)+"\n")
    
tekrar()