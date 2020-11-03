from django.db import models

# Create your models here.

class Media(models.Model):
    mediaid = models.IntegerField(primary_key=True)
    vrstamedije = models.CharField(max_length=20)
    putdodatoteke = models.TextField(unique=True)
    
    class Meta:
        managed = False
        db_table = 'media'


class Tema(models.Model):
    temaid = models.IntegerField(primary_key=True)
    ime = models.CharField(max_length=100)
    teksttemeid = models.ForeignKey(Media, models.DO_NOTHING, db_column='teksttemeid')

    class Meta:
        managed = False
        db_table = 'tema'

class Materijal(models.Model):
    materijalid = models.IntegerField(primary_key=True)
    ime = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'materijal'

class Maketa(models.Model):
    maketaid = models.IntegerField(primary_key=True)
    dimenzije = models.CharField(max_length=20)
    mediaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='mediaid')

    class Meta:
        managed = False
        db_table = 'maketa'

class Napravljenaod(models.Model):
    maketaid = models.ForeignKey(Maketa, models.DO_NOTHING, db_column='maketaid')
    materijalid = models.ForeignKey(Materijal, models.DO_NOTHING, db_column='materijalid')
    cijena = models.FloatField()

    class Meta:
        managed = False
        db_table = 'napravljenaod'
        unique_together = (('maketaid', 'materijalid'),)

class Transakcija(models.Model):
    transakcijaid = models.IntegerField(primary_key=True)
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    adresa = models.CharField(max_length=100)
    brojracuna = models.CharField(max_length=21)
    ukupaniznos = models.FloatField()

    class Meta:
        managed = False
        db_table = 'transakcija'


class Maketakupljena(models.Model):
    transakcijaid = models.ForeignKey(Transakcija, models.DO_NOTHING, db_column='transakcijaid')
    maketaid = models.ForeignKey(Maketa, models.DO_NOTHING, db_column='maketaid')
    materijalid = models.ForeignKey(Materijal, models.DO_NOTHING, db_column="materijalid")
    kolicina = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'maketakupljena'
        unique_together = (('transakcijaid', 'maketaid', 'materijalid'),)

class Korisnik(models.Model):
    korisnikid = models.IntegerField(primary_key=True)
    email = models.CharField(unique=True, max_length=100);
    korisnickoime = models.CharField(unique=True, max_length=20)
    lozinka = models.CharField(max_length=20)
    razinaautoriteta = models.IntegerField()
    adresa = models.CharField(max_length=100)
    rodendan = models.DateField()
    datumregistracije = models.DateField()
    adresaprivatna = models.BooleanField()
    rodendanprivatan = models.BooleanField()
    datumregistracijeprivatan = models.BooleanField()
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    dozvoljenpristup = models.BooleanField()
    brojracuna = models.CharField(max_length=21)
    profilnaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='profilnaid')

    class Meta:
        managed = False
        db_table = 'korisnik'

class Prica(models.Model):
    pricaid = models.IntegerField(primary_key=True)
    brojlajkova = models.IntegerField()
    brojdislajkova = models.IntegerField()
    objavljena = models.BooleanField()
    maketaid = models.ForeignKey(Maketa, models.DO_NOTHING, db_column="maketaid")
    maketaprodana = models.BooleanField()
    autorid = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='autorid')
    tekstpriceid = models.ForeignKey(Media, models.DO_NOTHING, db_column='tekstpriceid', related_name="tekstprice")
    glavnaslikapriceid = models.ForeignKey(Media, models.DO_NOTHING, db_column='glavnaslikapriceid', related_name="glavnaslikaprice")

    class Meta:
        managed = False
        db_table = 'prica'

class Multimedijaprice(models.Model):
    pricaid = models.ForeignKey(Prica, models.DO_NOTHING, db_column='pricaid')
    mediaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='mediaid')
    poredakuprici = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'multimedijaprice'
        unique_together = (('pricaid', 'mediaid'),)


class Komentar(models.Model):
    komentarid = models.IntegerField(primary_key=True)
    sadrzaj = models.CharField(max_length=300)
    korisnikid = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='korisnikid')
    pricaid = models.ForeignKey(Prica, models.DO_NOTHING, db_column='pricaid')

    class Meta:
        managed = False
        db_table = 'komentari'

class Custommaketa(models.Model):
    datumotvaranjazahtjeva = models.DateField()
    datumzatvaranjadatuma = models.DateField()
    ponudenacijena = models.FloatField()
    prihvaceno =  models.BooleanField()
    tekstzahtjevaid = models.ForeignKey(Media, models.DO_NOTHING, db_column='tekstzahtjevaid')
    korisnikid = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='korisnikid')
    
    class Meta:
        managed = False
        db_table = 'custommaketa'

