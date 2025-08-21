class Çalışan():

    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgileri_goster(self):
        print("Calısan sınfının bilgileri")

        print("İsim : {}\nMaaş: {}\nDepartman: {} \n ".format(self.isim,self.maaş,self.departman))

    def departman_degistir(self,yeni_departman):
        self.departman = yeni_departman

class Yönetici(Çalışan):
    pass

yönetici = Yönetici("Esra",3000,"Bilisim")

yönetici.bilgileri_goster()

yönetici.departman_degistir("İnsan Kaynakları")

yönetici.bilgileri_goster()

class Yönetici(Çalışan):
    def zam_yap(self,zam_miktarı):
        self.maaş += zam_miktarı

yönetici = Yönetici("Murat Sepik",4000,"Pazarlama")
yönetici.zam_yap(2000)
yönetici.bilgileri_goster()



class Yönetici(Çalışan):
    def __init__(self,isim,maaş,departman,kişi_sayısı):

        super().__init__(isim,maaş,departman)

        print("Yonetici sınıfının init fonksiyonu")

        self.kişi_sayısı = kişi_sayısı
    def zam_yap(self,zam_miktarı):
        self.maaş += zam_miktarı

    def bilgileri_goster(self):
        print("İsim : {}\nMaaş: {}\nDepartman: {} \nSorumlu kişi sayısı: {}\n ".format(self.isim, self.maaş,
                                                                                       self.departman,
                                                                                       self.kişi_sayısı))

yönetici = Yönetici("Esra Sepik",40000,"Bilişim",5)

yönetici.bilgileri_goster()
