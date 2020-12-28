from django.db import models
import datetime
# Create your models here.

class Media(models.Model):
    mediaid = models.AutoField(auto_created = True, primary_key = True, serialize = False) 
    vrstamedije = models.CharField(max_length=20)
    putdodatoteke = models.TextField(unique=True)
    
    class Meta:
        managed = True
        db_table = 'media'


class Tema(models.Model):
    temaid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    ime = models.CharField(max_length=100)
    tekstteme = models.CharField(max_length=160, default=None, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tema'
    def getIme(self):
        return self.ime
    
    def getTekst(self):
        self.tekstteme

class Materijal(models.Model):
    materijalid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    ime = models.CharField(max_length=100, default="default ime")

    class Meta:
        managed = True
        db_table = 'materijal'

    def getIme(self):
        return self.ime

    def __str__(self):
        return "{0}".format(self.ime)

class Vrstamakete(models.Model):
    vrstamaketeid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    ime = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'vrstamakete'
    
class Maketa(models.Model):
    maketaid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    ime = models.CharField(max_length=100, default="default ime")
    dimenzije = models.CharField(max_length=20)
    opis = models.CharField(max_length=160, default=None, blank=True, null=True)
    vrsta = models.ForeignKey(Vrstamakete, db_column='vrsta', on_delete=models.CASCADE)
    mediaid = models.ForeignKey(Media, db_column='mediaid', on_delete=models.CASCADE, blank = True, null = True)

    class Meta:
        managed = True
        db_table = 'maketa'

    def getId(self):
        return self.maketaid

    def getDimenzije(self):
        return self.dimenzije
    
    def getMedia(self):
        return self.mediaid.putdodatoteke

    def getIme(self):
        return self.ime

    def getOpis(self):
        return self.opis

    def getVrsta(self):
        return self.vrsta

class Napravljenaod(models.Model):
    maketaid = models.ForeignKey(Maketa, db_column='maketaid', on_delete=models.CASCADE)
    materijalid = models.ForeignKey(Materijal, db_column='materijalid', on_delete=models.CASCADE)
    cijena = models.FloatField(blank=True, null=True)
    brojuskladistu = models.IntegerField(default = 0)

    class Meta:
        managed = True
        db_table = 'napravljenaod'
        unique_together = (('maketaid', 'materijalid'),)

    def getCijena(self):
        return self.cijena

    def getMaterijalId(self):
        return self.materijalid;

    def getMaterijal(self):
        return self.materijalid.ime

    def getMaketaId(self):
        return self.maketaid

class Transakcija(models.Model):
    transakcijaid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    adresa = models.CharField(max_length=100)
    brojracuna = models.CharField(max_length=21)
    ukupaniznos = models.FloatField()
    korisnik = models.ForeignKey("Korisnik", db_column='korisnik', related_name="korisnik", default=None, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'transakcija'

    def getTransakcijaId(self):
        return self.transakcijaid;

    def getIme(self):
        return self.ime;

    def getPrezime(self):
        return self.prezime;

    def getAdresa(self):
        return self.adresa;

    def getBrojRacuna(self):
        return self.brojracuna;

    def getUkupanIznos(self):
        return self.ukupaniznos;

    def getKorisnikId(self):
        return self.korisnik;
    


class Maketakupljena(models.Model):
    transakcijaid = models.ForeignKey(Transakcija, db_column='transakcijaid', on_delete=models.CASCADE)
    maketaid = models.ForeignKey(Maketa, db_column='maketaid', on_delete=models.CASCADE)
    materijalid = models.ForeignKey(Materijal, db_column="materijalid", on_delete=models.CASCADE)
    kolicina = models.IntegerField(default = 0)

    class Meta:
        managed = True
        db_table = 'maketakupljena'
        unique_together = (('transakcijaid', 'maketaid', 'materijalid'),)

    def getTransakcijaId(self):
        return self.transakcijaid;

    def getMaketaId(self):
        return self.maketaid;

    def getMaterijalId(self):
        return self.materijalid;

    def getKolicina(self):
        return self.kolicina;
    

class Korisnik(models.Model):
    korisnikid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    email = models.CharField(unique=True, max_length=100, default='')
    korisnickoime = models.CharField(unique=True, max_length=20)
    lozinka = models.CharField(max_length=20)
    jeadmin = models.BooleanField(default=False)
    adresa = models.CharField(max_length=100, default=None, blank=True, null=True)
    rodendan = models.DateField(default=None, blank=True, null=True)
    datumregistracije = models.DateField(default=datetime.date.today, blank=True, null=True)
    adresaprivatna = models.BooleanField(default=False, blank=True, null=True)
    rodendanprivatan = models.BooleanField(default=False, blank=True, null=True)
    datumregistracijeprivatan = models.BooleanField(default=False, blank=True, null=True)
    slikaprivatna = models.BooleanField(default=False, blank=True, null=True)
    imeprezimeprivatno = models.BooleanField(default=False, blank=True, null=True)
    emailprivatan = models.BooleanField(default=False, blank=True, null=True)
    ime = models.CharField(max_length=50, default=None, blank=True, null=True)
    prezime = models.CharField(max_length=50, default=None, blank=True, null=True)
    dozvoljenpristup = models.BooleanField(default=None, blank=True, null=True)
    brojracuna = models.CharField(max_length=21, default=None, blank=True, null=True)
    profilnaid = models.ForeignKey(Media, db_column='profilnaid', default=1, blank=True, null=True, on_delete=models.CASCADE)
    lajkaopricu = models.ManyToManyField("Prica", related_name = "lajkaopricu")
    dislajkaopricu = models.ManyToManyField("Prica", related_name = "dislajkaopricu")
    kkpaypal = models.BooleanField(default=False)
    kkimeprezime = models.CharField(max_length=27, default=None, blank=True, null=True)
    kkbroj = models.CharField(max_length=16, default=None, blank=True, null=True)
    kkistek = models.CharField(max_length=5, default=None, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'korisnik'

    def getSlika(self):
        return self.profilnaid.putdodatoteke

    def getEmail(self):
        return self.email

    def getKorisnickoIme(self):
        return self.korisnickoime
    
    def getDatum(self):
        return self.datumregistracije


    def getIme(self):
        return self.ime

    def getPrezime(self):
        return self.prezime

    def getSlikaBool(self):
        return self.slikaprivatna

    def getEmailBool(self):
        return self.emailprivatan

    def getDatumBool(self):
        return self.datumregistracijeprivatan

    def getRodendanBool(self):
        return self.rodendanprivatan

    def getAdresaBool(self):
        return self.adresaprivatna

    def getImePrezimeBool(self):
        return self.imeprezimeprivatno

    def getDozvoljenPristup(self):
        return self.dozvoljenpristup

    def getJeAdmin(self):
        return self.jeadmin

    def getKorisnikId(self):
        return self.korisnikid

    

class Prica(models.Model):
    pricaid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    naslovprice = models.CharField(max_length=100,default = "Priča")
    datumprice = models.DateField(default= "1900-01-01", blank = True)
    brojlajkova = models.IntegerField(default = 0, blank = True)
    brojdislajkova = models.IntegerField(default = 0, blank = True)
    objavljena = models.BooleanField(default = False, blank = True)
    maketaid = models.ForeignKey(Maketa, db_column="maketaid", default=None, blank=True, null=True, on_delete=models.CASCADE)
    autorid = models.ForeignKey(Korisnik, db_column='autorid', related_name="autorid", on_delete=models.CASCADE)
    predloziotemuid = models.ForeignKey(Korisnik, db_column='predloziotemuid', related_name="predloziopricuid", null=True, on_delete=models.CASCADE)
    #tekstpriceid = models.ForeignKey(Media, db_column='tekstpriceid', related_name="tekstprice")
    #glavnaslikapriceid = models.ForeignKey(Media, db_column='glavnaslikapriceid', related_name="glavnaslikaprice")

    class Meta:
        managed = True
        db_table = 'prica'

    def getPricaId(self):
        return self.pricaid

    def getPredlozioPricuId(self):
        return self.predloziopricuid

    def getAutorId(self):
        return self.autorid

    def getSlika(self):
        return self.glavnaslikapriceid.putdodatoteke

    def getTekst(self):
        return self.tekstpriceid.putdodatoteke
    
    def getNaslov(self):
        return self.naslovprice

    def getDatumPrice(self):
        return self.datumprice;

    def getMaketaId(self):
        return self.maketaid;

    def getMaketaProdana(self):
        return self.maketaprodana;

    def getBrojLajkova(self):
        return self.brojlajkova;

    def getBrojDislajkova(self):
        return self.brojdislajkova;
    
class Multimedijaprice(models.Model):
    pricaid = models.ForeignKey(Prica, db_column='pricaid', on_delete=models.CASCADE)
    mediaid = models.ForeignKey(Media, db_column='mediaid', on_delete=models.CASCADE)
    poredakuprici = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'multimedijaprice'
        unique_together = (('pricaid', 'mediaid'),)

    def getMedia(self):
        return self.mediaid.putdodatoteke

class Komentar(models.Model):
    komentarid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    sadrzaj = models.CharField(max_length=300)
    korisnikid = models.ForeignKey(Korisnik, db_column='korisnikid', on_delete=models.CASCADE)
    pricaid = models.ForeignKey(Prica, db_column='pricaid', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'komentar'

    def getKorisnikId(self):
        return self.korisnikid;

##class Custommaketa(models.Model):
##    custommaketaid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
##    datumotvaranjazahtjeva = models.DateField()
##    datumzatvaranjadatuma = models.DateField()
##    ponudenacijena = models.FloatField(default=None, blank=True, null=True)
##    prihvaceno =  models.BooleanField(default=False, blank=True, null=True)
##    tekstzahtjevaid = models.ForeignKey(Media, db_column='tekstzahtjevaid')
##    korisnikid = models.ForeignKey(Korisnik, db_column='korisnikid')
##    
##    class Meta:
##        managed = True
##        db_table = 'custommaketa'

class Interakcija(models.Model):
    interakcijaid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    korisnikid = models.ForeignKey(Korisnik, db_column='korisnikid', on_delete=models.CASCADE)
    naslovinterakcije = models.CharField(max_length=100)
    vrstainterakcije = models.CharField(max_length=6)
    temaid = models.ForeignKey(Tema, db_column='temaid',blank=True, null=True, on_delete=models.CASCADE)
    maketaid = models.ForeignKey(Maketa, db_column='maketaid', blank=True, null=True, on_delete=models.CASCADE)
    pricaid = models.ForeignKey(Prica, db_column='pricaid', blank=True, null=True, on_delete=models.CASCADE)
    interakcijaotvorena = models.BooleanField(default=True, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'interakcija'

    def getId(self):
        return self.interakcijaid
    
    def getIme(self):
        return self.korisnikid.ime

    def getPrezime(self):
        return self.korisnikid.prezime
    
    def getProfilna(self):
        return self.korisnikid.profilnaid.putdodatoteke
    
    def getNaslov(self):
        return self.naslovinterakcije
    
    def getVrsta(self):
        return self.vrstainterakcije
    
    def getOtvorena(self):
        return self.interakcijaotvorena

