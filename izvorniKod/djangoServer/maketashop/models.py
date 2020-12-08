from django.db import models

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
    teksttemeid = models.ForeignKey(Media, models.DO_NOTHING, db_column='teksttemeid')

    class Meta:
        managed = True
        db_table = 'tema'

class Materijal(models.Model):
    materijalid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    ime = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'materijal'

class Maketa(models.Model):
    maketaid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    dimenzije = models.CharField(max_length=20)
    mediaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='mediaid')

    class Meta:
        managed = True
        db_table = 'maketa'

    def getDimenzije(self):
        return self.dimenzije
    
    def getMedia(self):
        return self.mediaid.putdodatoteke

class Napravljenaod(models.Model):
    maketaid = models.ForeignKey(Maketa, models.DO_NOTHING, db_column='maketaid')
    materijalid = models.ForeignKey(Materijal, models.DO_NOTHING, db_column='materijalid')
    cijena = models.FloatField()

    class Meta:
        managed = True
        db_table = 'napravljenaod'
        unique_together = (('maketaid', 'materijalid'),)

class Transakcija(models.Model):
    transakcijaid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    adresa = models.CharField(max_length=100)
    brojracuna = models.CharField(max_length=21)
    ukupaniznos = models.FloatField()

    class Meta:
        managed = True
        db_table = 'transakcija'


class Maketakupljena(models.Model):
    transakcijaid = models.ForeignKey(Transakcija, models.DO_NOTHING, db_column='transakcijaid')
    maketaid = models.ForeignKey(Maketa, models.DO_NOTHING, db_column='maketaid')
    materijalid = models.ForeignKey(Materijal, models.DO_NOTHING, db_column="materijalid")
    kolicina = models.IntegerField(default = 0)

    class Meta:
        managed = True
        db_table = 'maketakupljena'
        unique_together = (('transakcijaid', 'maketaid', 'materijalid'),)

class Korisnik(models.Model):
    korisnikid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    email = models.CharField(unique=True, max_length=100)
    korisnickoime = models.CharField(unique=True, max_length=20)
    lozinka = models.CharField(max_length=20)
    razinaautoriteta = models.IntegerField()
    adresa = models.CharField(max_length=100, default=None, blank=True, null=True)
    rodendan = models.DateField(default=None, blank=True, null=True)
    datumregistracije = models.DateField(default=None, blank=True, null=True)
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
    profilnaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='profilnaid', default=None, blank=True, null=True)
    lajkaopricu = models.ManyToManyField("Prica", related_name = "lajkaopricu")
    dislajkaopricu = models.ManyToManyField("Prica", related_name = "dislajkaopricu");
    
    class Meta:
        managed = True
        db_table = 'korisnik'

class Prica(models.Model):
    pricaid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    naslovprice = models.CharField(max_length=100,default = "Priča")
    datumprice = models.DateField(default= "1900-01-01", blank = True)
    brojlajkova = models.IntegerField(default = 0, blank = True)
    brojdislajkova = models.IntegerField(default = 0, blank = True)
    objavljena = models.BooleanField(default = False, blank = True)
    maketaid = models.ForeignKey(Maketa, models.DO_NOTHING, db_column="maketaid")
    maketaprodana = models.BooleanField(default = False, blank = True)
    autorid = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='autorid', related_name="autorid")
    predloziopricuid = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='predloziopricuid', related_name="predloziopricuid", null=True)
    tekstpriceid = models.ForeignKey(Media, models.DO_NOTHING, db_column='tekstpriceid', related_name="tekstprice")
    glavnaslikapriceid = models.ForeignKey(Media, models.DO_NOTHING, db_column='glavnaslikapriceid', related_name="glavnaslikaprice")

    class Meta:
        managed = True
        db_table = 'prica'

    def getPricaId(self):
        return self.pricaid

    def getSlika(self):
        return self.glavnaslikapriceid.putdodatoteke

    def getTekst(self):
        return self.tekstpriceid.putdodatoteke
    
    def getNaslov(self):
        return self.naslovprice


class Multimedijaprice(models.Model):
    pricaid = models.ForeignKey(Prica, models.DO_NOTHING, db_column='pricaid')
    mediaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='mediaid')
    poredakuprici = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'multimedijaprice'
        unique_together = (('pricaid', 'mediaid'),)


class Komentar(models.Model):
    komentarid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    sadrzaj = models.CharField(max_length=300)
    korisnikid = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='korisnikid')
    pricaid = models.ForeignKey(Prica, models.DO_NOTHING, db_column='pricaid')

    class Meta:
        managed = True
        db_table = 'komentar'

class Custommaketa(models.Model):
    custommaketaid = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    datumotvaranjazahtjeva = models.DateField()
    datumzatvaranjadatuma = models.DateField()
    ponudenacijena = models.FloatField(default=None, blank=True, null=True)
    prihvaceno =  models.BooleanField(default=False, blank=True, null=True)
    tekstzahtjevaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='tekstzahtjevaid')
    korisnikid = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='korisnikid')
    
    class Meta:
        managed = True
        db_table = 'custommaketa'

